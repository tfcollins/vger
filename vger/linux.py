"""Parser and documentation generator for the ADI Linux repo"""
from .common import core
import glob
import os
import json


class linux(core):
    """Parser and documentation generator for the ADI Linux repo"""

    def __init__(
        self,
        linux_repo_dir="linux",
        repo_url="https://github.com/analogdevicesinc/linux.git",
        branch="master",
        clone=False,
        linux_doc_folder=None,
    ):
        self.linux_repo_dir = linux_repo_dir
        self.repo_url = repo_url
        self.branch = branch
        self._check_linux_repo(clone)
        if linux_doc_folder is None:
            loc = os.path.dirname(__file__)
            loc = os.path.join(loc, "..")
            loc = os.path.join(loc, "docs", "source")
            self.linux_doc_folder = os.path.join(loc, "linux")
            if not os.path.isdir(self.linux_doc_folder):
                print(
                    f"Linux documentation folder not found. Default path used {self.linux_doc_folder}"
                )
                print(
                    "Please specify the path to the folder containing the Linux documentation."
                )
                exit(1)
        else:
            self.linux_doc_folder = linux_doc_folder

    def _check_linux_repo(self, clone=False):
        if not os.path.exists(self.linux_repo_dir) and not clone:
            print("Linux repository not found. Please clone it first.")
            exit(1)
        elif os.path.exists(self.linux_repo_dir) and clone:
            print("Linux repository already exists. Please remove it first.")
            exit(1)
        elif clone:
            os.system(
                f"git clone -b {self.branch} --single-branch"
                + f" --depth 1 {self.repo}"
                + f" {self.linux_repo_dir}"
            )
        return os.path.exists(self.linux_repo_dir)

    def _find_all_referenced(self, all_dts_files, filenames):
        # Find referencing DTSs
        all = filenames
        for file in all_dts_files:
            with open(file, "r") as f:
                data = f.read()
                for filename_using_component in filenames:
                    if filename_using_component in data and file not in all:
                        all.append(file)
        return all

    def _find_referencing_dts_files(self, kernel_root_dir, dt_root, dtsi_or_header):

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
            raise Exception(f"No DTS or header files using {target_dtss}")

        print("Target DTSs: ", target_dtss)

        # Find all DTSs referencing root DTS
        found = len(target_dtss)
        while True:
            target_dtss = self._find_all_referenced(files, target_dtss)
            if len(target_dtss) != found:
                found = len(target_dtss)
            else:
                break

        # Remove full kernel path
        target_dtss[0] = f"{dt_root}/{target_dtss[0]}"
        for i, file in enumerate(target_dtss):
            target_dtss[i] = file.replace(f"{kernel_root_dir}/", "")

        return target_dtss

    def _get_platforms_info(self):
        loc = os.path.dirname(__file__)
        # Read in json file with DTS references
        platforms_json = os.path.abspath(os.path.join(loc, "db/platforms.json"))
        with open(platforms_json, "r") as f:
            platforms = json.load(f)

        return platforms

    def _find_all_dts_files_for_platform(self, platforms):

        out_platforms = {}

        for platform in platforms:
            print("----------------")
            print(f"Processing: {platform}")
            out_platforms[platform] = {"Architectures": {}}
            for arch in platforms[platform]["Architectures"]:
                dtsi_or_header = platforms[platform]["PlatformHeader"]
                path = f"{self.linux_repo_dir}/arch/{arch}/boot"
                filenames = self._find_referencing_dts_files(
                    self.linux_repo_dir, path, dtsi_or_header
                )
                print("Adding: ", filenames)
                out_platforms[platform]["Architectures"][arch] = filenames
                # fill_platform_json_with_dts_filenames(platform, filenames)

        return out_platforms

    def parse_linux_repo(self):
        """Parse the Linux repository and return the following:"""
        # self.parse_linux_doc()
        # self.parse_linux_cores()
        platforms = self._get_platforms_info()
        platforms = self._find_all_dts_files_for_platform(platforms)

        return platforms