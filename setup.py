from setuptools import setup, find_packages

setup(
    name="vger-doc-tools",
    version="0.1.0",
    packages=find_packages(),
    package_data={"vger": ["_templates/*", "db/*"]},
    include_package_data=True,
    install_requires=[
        "Click",
        "jinja2",
        "symbolator@https://github.com/tfcollins/symbolator/tarball/main",
        "ipyxact",
    ],
    entry_points={
        "console_scripts": [
            "vger = vger.cli:cli",
        ],
    },
)
