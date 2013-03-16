from flask import Flask
from flask import render_template
from flask import request

import re

app = Flask(__name__)

compute_re = re.compile("""(?P<x>[0-9]+)[ ]*(?P<op>[\+\-\*\/\^])[ ]*(?P<y>[0-9]+)""")

def get_result(compute):
    m = compute_re.match(compute)
    if m:
        x = m.group('x')
        op = m.group('op')
        y = m.group('y')
        if op == "/":
            x = float(x)
            y = float(y)
            result = x / y
        else:
            x = int(x)
            y = int(y)
            if op == "*":
                result = x * y
            elif op == "+":
                result = x + y
            elif op == "-":
                result = x - y
            elif op == "^":
                result = x ** y
            else:
                # this statement should not be reachable
                assert(False)
        return result
    else:
        return "error"

@app.route('/')
def hello_world():
    compute = request.args.get('compute', '2 + 2')
    result = get_result(compute)
    return render_template(
        'hacker_puzzle_1.html',
        compute=compute,
        result=result)
if __name__ == '__main__':
    app.run()

