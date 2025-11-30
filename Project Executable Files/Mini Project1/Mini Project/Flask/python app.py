import numpy as np
import pandas as pd
import pickle
import os
from flask import Flask, request, render_template

app=Flask(__name__,static_url_path='/Flask/static')
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method=="POST":
        Area=float(request.form["area"])
        Perimeter=float(request.form["perimeter"])
        Major_Axis_Length=float(request.form["major_axis_length"])
        Solidity=float(request.form["solidity"])
        Extent=float(request.form["extent"])
        Roundness=float(request.form["roundness"])
        Aspect_Ration=float(request.form["aspect"])
        Compactness=float(request.form["compactness"])
        Eccentricity =float(request.form["eccentricity"])
        Minor_Axis_Length=float(request.form["minor_axis_length"])
        
        features_values=np.array([[Area,Perimeter,Major_Axis_Length,Minor_Axis_Length,Eccentricity,Solidity,Extent,Roundness,Aspect_Ration,Compactness]])
        df=pd.DataFrame(features_values,columns=['Area','Perimeter','Major_Axis_Length','Minor_Axis_Length','Eccentricity','Solidity','Extent','Roundness','Aspect_Ration','Compactness'])
        
        print(df)
        
        prediction=model.predict(df) 
        print(prediction[0])
        result=prediction[0]
        
        if prediction[0]==0:
            result="Your seed lies in cercevelik class"
        elif prediction[0]==1:
            result="Your seed lies in Urgup Sivrisi class"
            
        text="Hence,based on calculation:"
        return render_template("predict.html",prediction_text=text+str(result))
    else:
        return render_template("predict.html")

if __name__=="__main__":
      app.run(debug=True,port=5000)