import oyaml as yaml
from flask import Flask
from flask import render_template
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'))
    #print(type(website_data))
    return render_template('index.html', data=website_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
