from markdown2 import markdown 
from jinja2 import Environment, FileSystemLoader
from json import load
import uuid
import os


template_env = Environment(loader=FileSystemLoader(searchpath='./'))
template = template_env.get_template('layout.html')

with open('example.md') as markdown_file:
    article = markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks', 'code-friendly'])

filename = str(uuid.uuid4()) + '.html'

with open(os.path.join('output', filename), 'w') as output_file:
    output_file.write(
        template.render(
            article=article
        )
    )