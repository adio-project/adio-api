from flask import Flask, render_template, request, redirect, url_for, session
from forms import LoginForm
import auth

import http.client

app = Flask(__name__)
app.config["DEBUG"] = True;

@app.route("/", methods=['GET'])
def login():
    conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "2fcfad9916mshd77cacb637aa3bep1484e8jsn5dda54792c11",
        'X-RapidAPI-Host': "deezerdevs-deezer.p.rapidapi.com"
        }

    conn.request("GET", "/track/3135556", headers=headers)

    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

if __name__ == "__main__":
    app.run()