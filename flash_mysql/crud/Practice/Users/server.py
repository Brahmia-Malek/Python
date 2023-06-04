from flask import Flask, redirect, render_template, request  
from users import Users
app=Flask(__name__)





@app.route("/users")
def index():
    # call the get all classmethod to get all users
    users = Users.get_all()
    print(users)
    return render_template("users.html")

@app.route("/users/new")
def new():
     return render_template("new_user.html")

@app.route('/create',methods=["post"])
def new():
     print(request.form)
     
     return redirect("/users")
     












if __name__=="__main__":
     app.run(debug=True)