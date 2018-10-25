from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    technology=["Phones","Laptops","Headphones"]
    return render_template("home.html",technology= technology)

@app.route('/shop')
def shop():
    return render_template("shop.html")

@app.route('/lap')
def lap():
    return render_template("laptops.html")

if __name__ == '__main__':
   app.run(debug = True)

