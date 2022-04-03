import click
from .hdl import hdl as hdlv
from .linux import linux as linuxv
import subprocess
import os


@click.group()
@click.pass_context
def cli(ctx):
    """Vger doc parse and generation tools."""
    ctx.ensure_object(dict)


@cli.command()
@click.option(
    "--clone",
    "-c",
    is_flag=True,
    default=False,
    help="Clone HDL repo",
)
@click.option(
    "--hdl-doc-folder",
    "-h",
    is_flag=False,
    type=click.Path(exists=True),
    default=None,
    help="Path to HDL documentation folder within Sphinx project",
)
@click.pass_context
def hdl(ctx, clone, hdl_doc_folder):
    """Clone, parse, and generate documentation for HDL codebase.

    \b
    """
    ho = hdlv(clone=clone)
    out = ho.parse_hdl_repo()
    ho.generate_reference_design_pages(out)


@cli.command()
@click.option(
    "--clone",
    "-c",
    is_flag=True,
    default=False,
    help="Clone Linux repo",
)
@click.option(
    "--linux-doc-folder",
    "-h",
    is_flag=False,
    type=click.Path(exists=True),
    default=None,
    help="Path to Linux documentation folder within Sphinx project",
)
@click.pass_context
def linux(ctx, clone, linux_doc_folder):
    """Clone, parse, and generate documentation for Linux codebase.

    \b
    """
    lo = linuxv(clone=clone)
    out = lo.parse_linux_repo()
    lo.generate_reference_design_pages(out)


@cli.command()
@click.pass_context
def build(ctx):
    """Build Sphinx doc."""
    here = os.getcwd()
    target_makefile_dir = os.path.join(os.getcwd(), "docs")
    if os.path.isfile(os.path.join(target_makefile_dir, "Makefile")):
        subprocess.call(["make", "-C", target_makefile_dir, "html"])
    else:
        click.echo(f"Makefile not found in {target_makefile_dir}")
