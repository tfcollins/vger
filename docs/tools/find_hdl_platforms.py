import json
import os
import glob
from jinja2 import Environment, FileSystemLoader


def find_all_dependent_ips(carrier_root_dir):
    deps = []
    with open(os.path.join(carrier_root_dir, "Makefile"), "r") as f:
        data = f.read()
        for line in data.split("\n"):
            if "LIB_DEPS" in line:
                line = line.split("+=")[1].strip()
                deps.append(line)
    return deps


def get_hdl_readme_info(carrier_root_dir):
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
                    # line = line.split("Parts")[1].strip()
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


def find_all_hdl_platforms(hdl_root_dir):

    platforms = {}
    all_deps = []

    files = glob.glob(f"{hdl_root_dir}/**/system_project.tcl", recursive=True)
    for file in files:
        file = file.replace(f"{hdl_root_dir}/", "")
        project = file.split("/")[1]
        carrier = file.split("/")[2]
        if carrier == "system_project.tcl":
            carrier_path = f"{hdl_root_dir}/projects/{project}"
            carrier = None
        else:
            carrier_path = f"{hdl_root_dir}/projects/{project}/{carrier}"
        if project not in platforms:
            platforms[project] = {}
        if carrier not in platforms[project]:
            platforms[project][carrier] = {}
        deps = find_all_dependent_ips(carrier_path)
        platforms[project][carrier]["dependent_cores"] = deps
        for dep in deps:
            if dep not in all_deps:
                all_deps.append(dep)

        hdl_info = get_hdl_readme_info(f"{hdl_root_dir}/projects/{project}")
        platforms[project][carrier]["hdl_info"] = hdl_info

        # print("----------------")
        # print(f"{project} {carrier}")
        # find_all_dependent_ips(carrier_path)

    return platforms, all_deps


def generate_reference_design_pages():
    loc = os.path.dirname(__file__)

    with open(os.path.join(loc, "../db/hdl_platforms.json"), "r") as f:
        hdl_details = json.load(f)

    iloc = os.path.join(loc, "../source/hdl")
    loc = os.path.join(loc, "../source/hdl/reference_designs")
    if not os.path.isdir(loc):
        os.mkdir(loc)

    file_loader = FileSystemLoader("_templates")
    env = Environment(loader=file_loader)

    # Index Page
    template = env.get_template("hd_reference_design_index.tmpl")
    projects = sorted(hdl_details["platforms"].keys())
    output = template.render(projects=projects)

    with open(f"{iloc}/reference_design_index.md", "w") as f:
        f.write(output)

    # Individual pages
    template = env.get_template("hd_reference_design.tmpl")

    for project in hdl_details["platforms"]:
        projectn = project.upper()
        projectn = projectn.replace("_", "-")
        output = template.render(
            platform=hdl_details["platforms"][project], project=projectn
        )

        with open(f"{loc}/{project}.md", "w") as f:
            f.write(output)

    # Library Cores


def default():
    loc = os.path.dirname(__file__)
    hdl_root_dir = os.path.abspath(os.path.join(loc, "../../hdl"))

    platforms, all_deps = find_all_hdl_platforms(hdl_root_dir)

    hdl_details = {"platforms": platforms, "library": all_deps}

    with open(os.path.join(loc, "../db/hdl_platforms.json"), "w") as f:
        json.dump(hdl_details, f, indent=4)


if __name__ == "__main__":

    default()
    generate_reference_design_pages()