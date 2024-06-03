from flask import Flask , render_template , request
import pickle
app = Flask(__name__)

@app.route("/")
def fun1():
    return render_template("index.html")

@app.route("/predict" , methods=["post"])
def fun2():
    name=request.form['name']

    message = f"Hello, {name}! Your Bus Ticket is Successfull--Booked"
    return render_template("output.html",name=name , message= message)

if __name__=='__main__':
    app.run(debug=True)