from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    compute = request.args.get('compute', '')
    return render_template('compute.html', computation=compute)
if __name__ == '__main__':
    app.run(debug=True)

