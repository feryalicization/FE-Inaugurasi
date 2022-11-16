from flask import Flask, jsonify, render_template, Response, make_response, request, url_for, flash, redirect
import os
import json
import requests
import pdfkit

app = Flask(__name__)


base = 'http://127.0.0.1:8000/api/section'

@app.route("/")
def index():
    req = requests.get(base)
    req = json.loads(req.content)
    datas = req['data']


    return render_template('index.html', data=datas)
    # return jsonify(datas)  



@app.route("/section-create", methods=['GET', 'POST'])
def section_create():

    if request.method == 'POST':
        key = request.form.get('key')
        componentsId = request.form.get('componentsId')

        url = 'http://127.0.0.1:8000/api/section'
        payload = {'key': key, 'componentsId': componentsId}
        response = requests.post(url,data=payload)
        data = json.loads(response.content)
        print(data)
    return render_template('section.html')

 
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port, debug=True)
