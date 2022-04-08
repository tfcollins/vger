"""Parser and documentation generator for the ADI No-OS repo"""
from .common import core
import glob
import os
import json


class no_os(core):
    """Parser and documentation generator for the ADI No-OS repo"""

    def __init__(
        self,
        no_os_repo_dir="no-OS",
        repo_url="https://github.com/analogdevicesinc/no-OS.git",
        branch="master",
        clone=False,
        no_os_doc_folder=os.path.join("docs", "source", "no_os"),
    ):
        self.no_os_repo_dir = no_os_repo_dir
        self.repo_url = repo_url
        self.branch = branch
        self._check_no_os_repo(clone)
        if no_os_doc_folder is None:
            loc = os.path.dirname(__file__)
            loc = os.path.join(loc, "..")
            loc = os.path.join(loc, "docs", "source")
            self.no_os_doc_folder = os.path.join(loc, "no_os")
            if not os.path.isdir(self.no_os_doc_folder):
                print(
                    f"no-OS documentation folder not found. Default path used {self.no_os_doc_folder}"
                )
                print(
                    "Please specify the path to the folder containing the no-OS documentation."
                )
                exit(1)
        else:
            self.no_os_doc_folder = no_os_doc_folder

    def _check_no_os_repo(self, clone=False):
        if not os.path.exists(self.no_os_repo_dir) and not clone:
            print("no_os repository not found. Please clone it first.")
            exit(1)
        elif os.path.exists(self.no_os_repo_dir) and clone:
            print("no_os repository already exists. Please remove it first.")
            exit(1)
        elif clone:
            os.system(
                f"git clone -b {self.branch} --single-branch"
                + f" --depth 1 {self.repo_url}"
                + f" {self.no_os_repo_dir}"
            )
        return os.path.exists(self.no_os_repo_dir)

    def _parse_all_project_jsons(self):
        all_jsons = glob.glob(
            os.path.join(self.no_os_repo_dir, "projects", "**", "builds.json")
        )
        all_projects = {}
        for json_file in all_jsons:
            with open(json_file, "r") as f:
                data = json.load(f)
            project = json_file.split("/")[-2]
            all_projects[project] = data
        return all_projects

    def generate_no_os_project_table(self, projects):
        """Generate the no-OS project table"""
        # Index Page
        # loc = os.path.dirname(__file__)
        # tloc = os.path.join(loc, )
        template = self._read_template("noos_project_index.tmpl")
        output = template.render(projects=projects)

        with open(f"{self.no_os_doc_folder}/no_os_project_index.md", "w") as f:
            f.write(output)

    def parse_no_os_repo(self):
        """Parse the no-OS repository"""
        all_projects = self._parse_all_project_jsons()
        # for project in all_projects:
        #     print(f"Parsing project {project}")
        #     self._parse_project(project, all_projects[project])
        # self._parse_no_os_doc()
        return all_projects
