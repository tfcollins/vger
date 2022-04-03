from setuptools import setup, find_packages

setup(
    name='vger-doc-tools',
    version='0.1.0',
    packages=find_packages(),
    package_data={ "vger": ["_templates/*"] },
    include_package_data=True,
    install_requires=[
        'Click',
        "jinja2",
    ],
    entry_points={
        'console_scripts': [
            'vger = vger.cli:cli',
        ],
    },
)
