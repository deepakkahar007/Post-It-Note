from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("signin.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/market")
def market():

    details=[
        {
            "name":"deepak",
            "role":"developer",
            "phn":70426
        },
        {
            "name":"dk1",
            "role":"front-end",
            "phn":70092
        }
    ]
    return render_template("market.html",d=details)
    





@app.route("/about/<user>")
def dyn(user):
    return f'<h1>hello {user}</h1>'


app.run(debug=True)