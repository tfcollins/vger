"""The purpose of these function is to parse the linux tree for example
devicetrees (DTS) file for specific ADI platforms. These will be then
used within the doc as reference examples for users
"""
import glob
import os
import json


def _find_all_referenced(all_dts_files, filenames):
    # Find referencing DTSs
    all = filenames
    for file in all_dts_files:
        with open(file, "r") as f:
            data = f.read()
            for filename_using_component in filenames:
                if filename_using_component in data and file not in all:
                    all.append(file)
    return all


def find_referencing_dts_files(kernel_root_dir, dt_root, dtsi_or_header):

    path = os.path.join(f"{dt_root}", "**/*.dts")
    files = glob.glob(path, recursive=True)

    # Find root DTS
    target_dtss = []
    for file in files:
        with open(file, "r") as f:
            data = f.read()
            if dtsi_or_header in data:
                target_dtss = [file.split("/")[-1]]
                break

    if not target_dtss:
        raise Exception(f"No DTS or header files using {dtsi}")

    # Find all DTSs referencing root DTS
    found = len(target_dtss)
    while True:
        target_dtss = _find_all_referenced(files, target_dtss)
        if len(target_dtss) != found:
            found = len(target_dtss)
        else:
            break

    # Remove full kernel path
    target_dtss[0] = f"{dt_root}/{target_dtss[0]}"
    for i, file in enumerate(target_dtss):
        target_dtss[i] = file.replace(f"{kernel_root_dir}/", "")

    return target_dtss


def fill_platform_json_with_dts_filenames(platform, filenames):
    loc = os.path.dirname(__file__)
    kernel_root_dir = os.path.abspath(os.path.join(loc, "../../linux"))
    # Read in json file with DTS references
    platforms_json = os.path.abspath(os.path.join(loc, "../db/platforms.json"))
    with open(platforms_json, "r") as f:
        platforms = json.load(f)
    platforms[platform]["ExampleDTSFiles"] = filenames
    with open(platforms_json, "w") as f:
        json.dump(platforms, f, indent=4)

# def write_devicetree_table_to_file(platform, dts_list):
#     loc = os.path.join(loc, "../source/linux/dt_bindings")

#     file_loader = FileSystemLoader("_templates")
#     env = Environment(loader=file_loader)

#     # Index Page
#     template = env.get_template("hdl_reference_design_index.tmpl")
#     projects = sorted(hdl_details["platforms"].keys())
#     output = template.render(projects=projects)

#     with open(f"{iloc}/reference_design_index.md", "w") as f:
#         f.write(output)


def default():
    loc = os.path.dirname(__file__)
    kernel_root_dir = os.path.abspath(os.path.join(loc, "../../linux"))
    # Read in json file with DTS references
    platforms_json = os.path.abspath(os.path.join(loc, "../db/platforms.json"))
    with open(platforms_json, "r") as f:
        platforms = json.load(f)

    for platform in platforms:
        print("----------------")
        print(f"Processing {platform}")
        for arch in platforms[platform]["Architectures"]:
            dtsi_or_header = platforms[platform]["PlatformHeader"]
            path = f"{kernel_root_dir}/arch/{arch}/boot"
            filenames = find_referencing_dts_files(
                kernel_root_dir, path, dtsi_or_header
            )
            print("Adding: ", filenames)
            fill_platform_json_with_dts_filenames(platform, filenames)


if __name__ == "__main__":

    path = "/tmp/vger-doc/linux/arch/arm/boot"
    # path = "/tmp/vger-doc/linux/arch/arm64/boot"

    dtsi_or_header = "dt-bindings/iio/adc/adi,ad9081.h"
    # dtsi = "zynq-zc706-adv7511-ad9081.dts"

    # find_referencing_dts_files(path, dtsi_or_header)
    default()
