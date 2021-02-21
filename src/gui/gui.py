"""Run GUI"""

import re
import yaml
from flask import Flask, render_template, request
from flaskwebgui import FlaskUI

import runner
from globals import *

app = Flask(__name__, static_url_path='', static_folder='', template_folder='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

ui = FlaskUI(app)


@app.route('/')
def index():
    """Create index page"""

    files = ['index.js', 'style.css', 'favicon.ico']
    for file in files:
        app.send_static_file(file)

    config = {}

    if os.path.exists('Modcrafter.yml'):
        with open('Modcrafter.yml', 'r') as file:
            config = yaml.safe_load(file.read())

    html = render_template('index.jinja')
    html = html.replace('{VERSION}', VERSION)
    html = html.replace('{CONFIG}', str(config))
    return html


@app.route('/process', methods=['GET', 'POST'])
def process():
    """Complete form input"""

    args = request.form.to_dict()
    config = {'version': {'modcrafter': VERSION}, 'mod': {}, 'blocks': {}, 'items': {}}

    lastID = ''
    for arg, val in args.items():
        section, key = arg.split('.')
        if re.search(r'\d', section):
            section = re.sub(r'\d', '', section)
            if key == 'id':
                lastID = val
                config[section][lastID] = {}
            else:
                if re.search(r'^\d+$', val):
                    val = int(val)
                elif re.search(r'^\d+\.\d+$', val):
                    val = float(val)
                elif val == 'on':
                    val = True
                config[section][lastID][key] = val
        elif section in config:
            config[section][key] = val

    yaml_content = re.sub(r' {8}|\\r', '', f"""
        {yaml.dump({'version': config['version']})}
        {yaml.dump({'mod': config['mod']})}
        {yaml.dump({'blocks': config['blocks']})}
        {yaml.dump({'items': config['items']})}
    """.rstrip())

    with open('Modcrafter.yml', 'w') as file:
        file.write(yaml_content)

    runner.run()

    html = render_template('process.jinja')
    html = html.replace('{YAML}', yaml_content)
    return html


def run():
    """Run GUI"""
    ui.run()
