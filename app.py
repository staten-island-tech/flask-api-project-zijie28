from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
def index():
    
    cat = ["biryani", "butter-chicken", "dosa", "pasta", "rice", "burger", "dessert", "idly", "pizza", "samosa"]
    e=[]
    for i in cat:
        response = requests.get(f"https://foodish-api.com/api/images/{i}")
        data = response.json()
        e.append(data['image'])
    return render_template("index.html", picture=e, cata=i, cat=cat)
@app.route("/<catagories>")
def spec_cata(catagories):
    response = requests.get(f"https://foodish-api.com/api/images/{catagories}/")
    prop= response.json()
    pic=prop.get("image")
    try:
        if prop.get('error') == 'Not found.':
            return render_template("error.html")
        else:
            return render_template("spec.html", spec_pict=pic, food_type=catagories)
    except KeyError:
            return render_template("spec.html", spec_pict=pic, food_type=catagories)

if __name__ == '__main__':
    app.run(debug=True)