from flask import Flask,redirect,url_for,render_template,request,session

app = Flask(__name__)

app.secret_key ="your secret key"

@app.route("/b")
def b1():
    return render_template("home2.html")





userss=[{"Pramod":"di@1234"},{"dis":"dis@1234"},{"disi":"disi@1234"}]
@app.route("/c")
def b2():
    return render_template("home2.html")
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password=request.form['password']
        user_exists = False

        for user in userss:
            if username in user:
                user_exists=True

            if userss[username] == password:
                session["user"]=username
                return redirect(url_for('b2'))
            else:
                return "invalid details try again with correct details"
            

        if not user_exists:
            return "user does not exist"
    elif "user" in session:
        return redirect(url_for('b2'))
            
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))





if __name__=="__main__":
    app.run(debug=True)