from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/b")
def b1():
    return render_template("home3.html")

userss = {"Pramod": "di@1234", "dis": "dis@1234", "disi": "disi@1234"}

@app.route("/c")
def b2():
    return render_template("home3.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in userss and userss[username] == password:
            session["user"] = username
            return redirect(url_for('b2'))
        else:
            return "Invalid details. Try again with correct details."

    if "user" in session:
        return redirect(url_for('b2'))

    return render_template("login1.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
