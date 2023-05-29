# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:12:23 2023


"""

from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'model.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
   a = request.form["gen"]
   b = request.form["sscp"]
   c = request.form["sscb"]
   d = request.form["hscp"]
   e = request.form["hscb"]
   f = request.form["hscd"]
   g = request.form["cdp"]
   h = request.form["cd"]
   i = request.form["ie"]
   j = request.form["at"]
   k = request.form["mp"]
   output= model.predict([[a,b,c,d,e,f,g,h,i,j,k]])
   print(output[0])
   print(type(output[0]))
   if(output[0]==1):
       o1="<You will be Placed"
   else:
       o1="Sorry!You cannot get placed with your current status...Work harder in your academics"
        
   return render_template("index.html",aa=o1 )


@app.route('/admin')#binds to an url
def admin():
    return "done"

if __name__ == '__main__' :
    app.run(debug= False,port=8080)
