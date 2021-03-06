import json
import os

from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/legends")
def legends():
    legends = []
    with open("data/legends.json", "r") as my_json:
        legends = json.load(my_json)
    return render_template( "legends.html", legends = legends )


@app.route("/legends/<creature>")
def creature():
    legends.creature = {}
    with open("data/legends.json", "r") as json_data:
        creature = json.load(json_data)
        for creature in legends.creature:
    return render_template("creature.html", page_title="creature",
                           creature=creature)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
