"""Parser and doc page generator tools for HDL repo"""
from .common import core
import glob
import os
import json


class hdl(core):
    """Parser and doc page generator tools for HDL repo"""

    def __init__(
        self,
        hdl_repo_dir="hdl",
        repo_url="https://github.com/analogdevicesinc/hdl.git",
        branch="master",
        clone=False,
        hdl_doc_folder=None,
    ):
        self.hdl_repo_dir = hdl_repo_dir
        self.repo_url = repo_url
        self.branch = branch
        self._check_hdl_repo(clone)
        if hdl_doc_folder is None:
            loc = os.path.dirname(__file__)
            loc = os.path.join(loc, "..")
            loc = os.path.join(loc, "docs", "source")
            self.hdl_doc_folder = os.path.join(loc, "hdl")
            if not os.path.isdir(self.hdl_doc_folder):
                print(
                    f"HDL documentation folder not found. Default path used {self.hdl_doc_folder}"
                )
                print(
                    "Please specify the path to the folder containing the HDL documentation."
                )
                exit(1)
        else:
            self.hdl_doc_folder = hdl_doc_folder

    def _check_hdl_repo(self, clone=False):
        if not os.path.exists(self.hdl_repo_dir) and not clone:
            print("HDL repository not found. Please clone it first.")
            exit(1)
        elif os.path.exists(self.hdl_repo_dir) and clone:
            print("HDL repository already exists. Please remove it first.")
            exit(1)
        elif clone:
            os.system(
                f"git clone -b {self.branch} --single-branch"
                + f" --depth 1 {self.repo}"
                + f" {self.hdl_repo_dir}"
            )
        return os.path.exists(self.hdl_repo_dir)

    def _find_all_dependent_ips(self, carrier_root_dir):
        # Parse dependent library cores for project
        library_cores = []
        with open(os.path.join(carrier_root_dir, "Makefile"), "r") as f:
            data = f.read()
            for line in data.split("\n"):
                if "LIB_DEPS" in line:
                    line = line.split("+=")[1].strip()
                    library_cores.append(line)
        return library_cores

    def _get_hdl_readme_info(self, carrier_root_dir):
        # Parse readme file for project
        info = {}
        files = glob.glob(f"{carrier_root_dir}/*")
        readme = [f for f in files if "readme" in f.lower()][0]
        # with open(os.path.join(carrier_root_dir, "README.md"), "r") as f:
        with open(readme, "r") as f:
            data = f.read()
            for line in data.split("\n"):
                if " * " in line:
                    line = line.replace(":", "")
                    if "Parts" in line:
                        line = line[line.find("(") + 1 : line.find(")")].strip()
                        info["parts"] = line
                    elif "Project Doc" in line:
                        line = line.split("Project Doc")[1].strip()
                        info["pdoc"] = line
                    elif "HDL Doc" in line:
                        line = line.split("HDL Doc")[1].strip()
                        info["hdoc"] = line
                    elif "Linux Drivers" in line:
                        line = line.split("Linux Drivers")[1].strip()
                        info["drivers"] = line
                    elif "Board Product Page" in line:
                        line = line[line.find("(") + 1 : line.find(")")].strip()
                        info["board"] = line
        return info

    # def find_all_hdl_platforms(self, hdl_root_dir):
    def parse_hdl_repo(self) -> dict:
        """Parse HDL repository and return the following:
        - All supported projects
        - All supported carriers
        - All dependent library cores per project
        - Links to external resources/doc from each project's readme
        """
        platforms = {}
        all_deps = []

        files = glob.glob(f"{self.hdl_repo_dir}/**/system_project.tcl", recursive=True)
        for file in files:
            file = file.replace(f"{self.hdl_repo_dir}/", "")
            project = file.split("/")[1]
            carrier = file.split("/")[2]
            if carrier == "system_project.tcl":
                carrier_path = f"{self.hdl_repo_dir}/projects/{project}"
                carrier = None
            else:
                carrier_path = f"{self.hdl_repo_dir}/projects/{project}/{carrier}"
            if project not in platforms:
                platforms[project] = {}
            if carrier not in platforms[project]:
                platforms[project][carrier] = {}
            deps = self._find_all_dependent_ips(carrier_path)
            platforms[project][carrier]["dependent_cores"] = deps
            for dep in deps:
                if dep not in all_deps:
                    all_deps.append(dep)

            hdl_info = self._get_hdl_readme_info(
                f"{self.hdl_repo_dir}/projects/{project}"
            )
            platforms[project][carrier]["hdl_info"] = hdl_info

            # print("----------------")
            # print(f"{project} {carrier}")
            # find_all_dependent_ips(carrier_path)

        return {"platforms": platforms, "library": all_deps}

    def generate_reference_design_pages(self, hdl_details=None) -> None:
        """Generate individual HDL reference design pages for each project.
        Each page will contain:
        - A list of all supported carriers
        - A list of library cores used in each carrier design

        Args:
            hdl_details (dict,str): Dictionary of HDL reference design info
                or path to JSON file containing the same info. If None, an existing
                JSON file will be used internal to the library.

        """
        loc = os.path.dirname(__file__)

        if not hdl_details:
            # NEED TO FIX THIS LOCATION TO SOMETHING IN THE VGER FOLDER
            with open(
                os.path.join(self.hdl_doc_folder, "../../db/hdl_platforms.json"), "r"
            ) as f:
                hdl_details = json.load(f)
        elif isinstance(hdl_details, str):
            with open(hdl_details, "r") as f:
                hdl_details = json.load(f)

        # iloc = os.path.join(loc, "../source/hdl")
        # loc = os.path.join(loc, "../source/hdl/reference_designs")
        loc = os.path.join(self.hdl_doc_folder, "reference_designs")
        if not os.path.isdir(loc):
            os.mkdir(loc)

        # Index Page
        template = self._read_template("hdl_reference_design_index.tmpl")
        projects = sorted(hdl_details["platforms"].keys())
        output = template.render(projects=projects)

        with open(f"{self.hdl_doc_folder}/hdl_reference_design_index.md", "w") as f:
            f.write(output)

        # Individual pages
        template = self._read_template("hdl_reference_design.tmpl")

        for project in hdl_details["platforms"]:
            projectn = project.upper()
            projectn = projectn.replace("_", "-")
            output = template.render(
                platform=hdl_details["platforms"][project], project=projectn
            )
            print(f"Generating {projectn} {loc}/{project}.md")
            with open(f"{loc}/{project}.md", "w") as f:
                f.write(output)

        # Library Cores
