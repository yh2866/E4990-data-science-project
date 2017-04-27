# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
# Input: (Day, Time)
# Output: (Frequency, PCT)

Dict = {


(0, 0): [

(	0.344444444	,	1	),
(	0.262962963	,	5	),
(	0.406481481	,	6	),
(	0.271296296	,	7	),
(	0.314814815	,	8	),
(	0.332407407	,	10	),
(	0.387962963	,	13	),
(	0.446296296	,	14	),
(	0.237037037	,	17	),
(	0.361111111	,	18	),
(	0.271296296	,	19	),
(	0.327777778	,	20	)


]}

app = Flask(__name__)


@app.route('/report')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 15, type=int)
    b = request.args.get('b', 0, type=int)
    re = ""
    for i in Dict[(a,b)]:
        re += "The precinct No."+ str(i[1]) + " will have "+ str(i[0]) + " frequency.<br>"
    return jsonify(result=re)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=False
    app.run(host='0.0.0.0')

