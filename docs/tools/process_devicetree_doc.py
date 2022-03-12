"""Generate MD pages for DT yaml files and create mkdocs.yml"""
import glob
from jinja2 import Environment, FileSystemLoader
import yaml
import os

from pprint import pprint

db = {}

def test_yaml(filename):
    try:
        with open(filename, "r") as stream:
            data = yaml.safe_load(stream)
        return True
    except:
        return False

def build_common_dt_bindings_reference(kernel_root_dir, target_dir):
    global db
    files = ["Documentation/devicetree/bindings/spi/spi-controller.yaml","Documentation/devicetree/bindings/clock/fixed-clock.yaml"]
    for file in files:
        with open(f"{kernel_root_dir}/{file}", "r") as stream:
            data = yaml.safe_load(stream)

        if "properties" in data:
            props = data["properties"]
            for prop in props:
                db[prop] = {}
                if "$ref" in props[prop]:
                    ptype = props[prop]["$ref"].split("/")[-1]
                    db[prop] = {"type": ptype}
                if "description" in props[prop]:
                    db[prop]["description"] = props[prop]["description"].replace("\n", " ")
        if "patternProperties" in data:
            for key in data["patternProperties"]:
                if "properties" in data["patternProperties"][key]:
                    props = data["patternProperties"][key]["properties"]
                    for prop in props:
                        db[prop] = {}
                        if "$ref" in props[prop]:
                            ptype = props[prop]["$ref"].split("/")[-1]
                            db[prop] = {"type": ptype}
                        db[prop]["description"] = props[prop]["description"].replace("\n", " ")
    # pprint(db)
    with open(os.path.join(target_dir,"common_dt_bindings_reference.yaml"), "w") as f:
        yaml.dump(db, f)

def generate_md_files(kernel_root_dir, target_dir, stop_bad_yaml=False, limit_to_adi=True):
    """Generate MD files for all DT yaml files"""

    if not os.path.isdir(kernel_root_dir):
        raise Exception(f"{kernel_root_dir} not a directory")
    if not os.path.isdir(target_dir):
        raise Exception(f"{target_dir} not a directory")

    path = os.path.join(
        kernel_root_dir, "Documentation/devicetree/bindings/iio/**/*.yaml"
    )
    print(path)
    files = glob.glob(path)
    filenames = []

    for file in files:
        if not limit_to_adi or "adi," in file:
            if not test_yaml(file):
                if stop_bad_yaml:
                    raise Exception(f"Invalid yaml file found: {file}")
                print(f"BAD YAML: {file}")
                continue
            filename = file.split("/")[-1]
            filename = filename.replace(",", "_").replace("yaml", "md")
            filename = filename.upper()
            filename = filename.replace(".MD", ".md")
            with open(f"{target_dir}/devs/{filename}", "w") as f:
                cmd = f"# {filename[:-3].split('_')[1]}"
                cmd += "\n\n```{devicetree} "+f"{file}"
                cmd += "\n```"
                f.write(cmd)
            # print(filename)
            filenames.append(filename)

    return filenames


def create_mkdocs_yml(filenames: list):
    """Gernerate mkdocs.yml file based on generated md files"""

    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)

    template = env.get_template("temp.yml")

    output = template.render(devs=filenames)

    with open("mkdocs.yml", "w") as f:
        f.write(output)

def create_md_index(filenames: list, target_dir):
    """Gernerate mkdocs.yml file based on generated md files"""

    file_loader = FileSystemLoader("_templates")
    env = Environment(loader=file_loader)

    template = env.get_template("device_tree_index.tmpl")

    output = template.render(devs=filenames)

    with open(f"{target_dir}/device_tree_index.md", "w") as f:
        f.write(output)


def default():
    loc = os.path.dirname(__file__)
    kernel_root_dir = os.path.abspath(os.path.join(loc, "../../linux"))
    target_dir = os.path.abspath(os.path.join(loc, "../source/linux/dt_bindings"))
    # fns = generate_md_files(kernel_root_dir,target_dir)

    # target_dir = os.path.abspath(os.path.join(loc, "../source/linux/dt_bindings"))
    # create_md_index(fns, target_dir)

    build_common_dt_bindings_reference(kernel_root_dir, target_dir)


if __name__ == "__main__":
    default()