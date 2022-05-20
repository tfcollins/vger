import os

from ipyxact.ipyxact import Component
from pytest import File


class hdl_ip:
    ips_to_build = ["axi_ad9361", "axi_clkgen"]
    vivado_version = "2021.1"

    def generate_library_ip_list(self) -> None:
        self.ips_to_build = os.listdir(os.path.join(self.hdl_repo_dir, "library"))

    def generate_ip_pages(self):

        os.chdir(self.hdl_repo_dir)
        self.generate_library_ip_list()

        ip_cores = []
        for ip in self.ips_to_build:
            # Build each IP individually
            try:
                print(f"Building {ip}")
                os.chdir(f"{self.hdl_repo_dir}/library/{ip}")
                vivado = (
                    ". /opt/Xilinx/Vivado/"
                    + str(self.vivado_version)
                    + "/settings64.sh"
                )
                os.system(f"{vivado} && make")
                print(f"Done building {ip}")

                # Parse IP-XACT XML file
                print(f"Parsing {ip} XML file")
                component = Component()
                with open("component.xml", "r") as f:
                    component.load(f)

                # Generate markdown page
                print(f"Generating {ip} page")
                ip_dir = os.path.join(self.hdl_doc_folder, "ip")
                if not os.path.isdir(ip_dir):
                    os.mkdir(ip_dir)
                loc = os.path.join(ip_dir, ip)

                # Extract data
                ip_info = {"name": component.name, "version": component.version}
                params = [
                    {"name": param.name, "d_value": param.value, "description": "NA"}
                    for param in component.parameters.parameter
                ]
                ip_info["parameters"] = params
                buses = self.get_businterfaces(component.busInterfaces)
                ip_info["buses"] = buses

                # Generate diagram
                os.system(f"symbolator --title --transparent -i {ip}.v -o {ip_dir}")

                # Generate markdown page
                self.generate_ip_core_page(ip, ip_info, loc)

                ip_cores.append(ip)
            except Exception as e:
                print(f"Error building {ip}")

        self.generate_ip_core_index_page(ip_cores)

    def generate_ip_core_index_page(self, ip_cores):
        # Index Page
        template = self._read_template("hdl_ip_core_index.tmpl")
        ip_cores = sorted(ip_cores)
        output = template.render(ips=ip_cores)

        with open(f"{self.hdl_doc_folder}/hdl_ip_core_index.md", "w") as f:
            f.write(output)

    def writel(self, f, txt):
        f.write(f"{txt}\n")

    def get_businterfaces(self, busInterfaces):
        buses = []
        for busInterface in busInterfaces.busInterface:
            # _vendor = busInterface.busType.vendor
            # _library = busInterface.busType.library
            # _name = busInterface.busType.name
            # _version = busInterface.busType.version
            port_maps = []
            if busInterface.portMaps:
                port_maps.extend(
                    {
                        "logical": portMap.logicalPort.name,
                        "physical": portMap.physicalPort.name,
                    }
                    for portMap in busInterface.portMaps.portMap
                )

            buses.append(
                {
                    "name": busInterface.name,
                    "port_maps": port_maps,
                    "type": busInterface.busType.name,
                }
            )
        return buses

    def generate_ip_core_page(self, ip_name, ip_info, page_path) -> None:
        """Generate individual HDL reference design pages for each project.
        Each page will contain:
        - A list of all supported carriers
        - A list of library cores used in each carrier design

        Args:
            ip_info (dict,str): Dictionary containing IP information.

        """
        # Individual pages
        template = self._read_template("hdl_ip_core.tmpl")

        output = template.render(ip=ip_info)
        print(f"Generating {page_path}.md")
        with open(f"{page_path}.md", "w") as f:
            f.write(output)
