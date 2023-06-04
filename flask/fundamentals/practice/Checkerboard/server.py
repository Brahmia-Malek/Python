from flask import Flask, render_template
app = Flask(__name__)


@app.route("/<x>/<y>")
def chek_board(x,y):
    input1=int(x)
    input2=int(y)
    return render_template("index.html", input1=input1, input2=input2)

if __name__ == "__main__":
    app.run(debug = True)
