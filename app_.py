from flask import Flask,redirect,url_for,render_template,request,session

app = Flask(__name__)

app.secret_key ="your secret key"

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/home")
def welcome():
    return "hi buddy!"
def about():
    return "welcome to the world"
app.add_url_rule("/about", "about", about)

def guest(guest):
    return f"{guest} as guest"
@app.route("/admin")
def admin():
    return "this is admin page"
def user(name):
    if name == "admin":
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("guest",guest=name))

app.add_url_rule("/user/<name>","user",user)
app.add_url_rule("/guest/<guest>", "guest", guest)

@app.route("/user/<string:name>")
def user_details(name):
    return f"(name) is user"

@app.route("/id_details/<int:id>")
def user_id_details(id):
    return f"{id} is integer"

@app.route("/float_details/<float:float_id>")
def float_id_details(float_id):
    return f"{float_id} is a float"


@app.route('/d')
def index():
    user = {"username":"pramod"}
    return render_template('home.html', user=user)

@app.route("/hello/<user>")
def use_details(user):
    return render_template('home.html', name=user)






@app.route('/hi')
def index1():
    return render_template("home1.html")








@app.route('/do')
def a1():
    users=[
        {
            "id": 1,
            "name":"Pramod",
            "username":"disilva",
            "email":"disilva@gmail.com"
        },
        {
            "id": 2,
            "name":"eswara",
            "username":"eswar",
            "email":"dsilva@gmail.com"
        },
        {
            "id": 3,
            "name":"Pramu",
            "username":"disiva",
            "email":"disiva@gmail.com"
        }
    ]
    return render_template("home1.html",users=users)







#http requestsssssssssssss

#get requestssssssssssssssssssssssssssssss
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