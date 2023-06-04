
from flask import Flask, render_template , redirect ,request, session
app=Flask (__name__)
app.secret_key="hhhhhh"





@app.route('/')
def index():
   return render_template("index.html")

@app.route('/process', methods=['POST'])
def display():
     session["name"] = request.form['name']
     session["location"]  = request.form['location']
     session["language"]  = request.form['language']
     session["comment"]  = request.form['comment']
     
     return redirect('/result')

@app.route('/result')
def result():
    # name = request.form['name']
    # location = request.form['location']
    # language = request.form['language']
    # comment = request.form['comment']
    print(request.form)
    return render_template("result.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')


if __name__ =='__main__':
   app.run(debug=True)