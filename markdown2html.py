from markdown2 import markdown 
from jinja2 import Environment, FileSystemLoader
from json import load
import uuid
import os
import click

@click.command()
@click.argument("file_path_of_markdown_to_convert")
@click.option("--layout", default='marquincv-skeleton-layout.html', help='The base html file to build the markdown file into')
def make_html(file_path_of_markdown_to_convert, layout):
    template_env = Environment(loader=FileSystemLoader(searchpath='./layouts/'))
    template = template_env.get_template(layout)

    with open(file_path_of_markdown_to_convert) as markdown_file:
        article = markdown(
            markdown_file.read(),
            extras=['fenced-code-blocks', 'code-friendly', 'tables'])

    filename = str(uuid.uuid4()) + '.html'

    with open(os.path.join('output', filename), 'w') as output_file:
        output_file.write(
            template.render(
                article=article
            )
        )
    print("Created html file: " + filename)

if __name__ == '__main__':
    make_html()
