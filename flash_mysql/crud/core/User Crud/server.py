from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route("/user/create" , methods=["Post"])
def newuser():
    #! REQUEST, REDIRECT
    # print(request.form)
    User.save(request.form)
    return redirect("/users")

@app.route('/users/new')
def displayform():
   return render_template("new_user.html")




@app.route("/users/show/<id>")
def show_user(id):

    data = {
        "id": id
    }

    result = User.show_one(data)
    print(result)

    return render_template("user_id.html", user =result)


@app.route("/user/edit" , methods=["Post"])
def edituser ():

    #! REQUEST, REDIRECT
    # print(request.form)
    test= User.update_user(request.form)
    return redirect("/users")



@app.route("/users/edit/<id>")
def edit_user(id):

    data = {
        "id": id
    }

    result = User.show_one(data)
    print(result)

    return render_template("user_edit.html", user=result)


@app.route('/users/delete/<int:id>')
def delete(id):
    data={'id':id}
    User.delete(data)
    return redirect('/users')









   





if __name__=='__main__':
 app.run(debug=True)





