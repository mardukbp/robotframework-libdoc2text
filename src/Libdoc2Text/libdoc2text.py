import click
from jinja2 import Template

import json
import os
import shutil
from pathlib import Path


package_path = Path(os.path.abspath(__file__)).parent

@click.group()
@click.version_option(package_name="robotframework_libdoc2text", prog_name='libdoc2text')
def cli():
    """
    generate plain text documentation from the JSON generated by libdoc
    """
    pass


@cli.command('init.adoc', short_help='Create the Asciidoc template')
def init_adoc():
    template_path = os.path.abspath(package_path / "templates/library.adoc.jinja")
    shutil.copy(template_path, os.getcwd())


@cli.command('init.md', short_help='Create the Markdown template')
def init_md():
    template_path = os.path.abspath(package_path / "templates/library.md.jinja")
    shutil.copy(template_path, os.getcwd())


@cli.command('run', short_help='Generate the documentation from a template and a JSON file')
@click.argument('template')
@click.argument('library_json')
@click.argument('output')
def run(template: str, library_json: str, output: str):
    """
    Given a Jinja template and a JSON file generate plain text documentation.
    
    Example: libdoc2text run library.adoc.jinja Library.json Library.adoc
    """

    with open(template, encoding="utf-8") as file:
       jinja_template = Template(file.read())

    with open(library_json, encoding='utf-8') as file:
        library = json.load(file)

    text_doc = jinja_template.render(library)

    with open(output, "w+", encoding="utf-8") as file:
        file.write(text_doc)
    
    print(f"Generated {output}")
