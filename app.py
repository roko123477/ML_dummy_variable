from distutils.log import debug
from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub",methods=['POST'])
def submit():
    area=int(request.form["area"])    
    locations=request.form['loc']

    if(locations=='monroe township'):
        locate=[1,0]
    elif(locations=='robinsville'):
        locate=[0,1]
    else:
        locate=[0,0]    
    
    out=model.predict([[area,locate[0],locate[1]]])
    output=round(out[0],2)
    return render_template("index.html",n=output)


if(__name__=="__main__"):
    app.run(debug=True)