from flask import Flask, redirect, render_template, session
app = Flask(__name__)
app.secret_key='hfeirfbgefuioe'

@app.route('/')
def index():

    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html", count= session['count'])


@app.route('/addtwo')
def addtwo():
    session['count']+=0
    return redirect('/')

@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')






if __name__=="__main__":    
    app.run(debug=True)    

