from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def rootpage():
    myheight=''
    myweight=''
    bmi=''
    fbmi=''
    h=''
    w=''
    if request.method=='POST':
        myweight=request.form.get('weight')
        myheight=request.form.get('height')
        h=float(myheight)
        w=int(myweight)
        bmi=w/(h*h)
        fbmi=str(bmi)


    return render_template("index.html",name=fbmi)

@app.route("/first")
def home1():
    return "hello from my first flask page helloooooooo"
