from flask import Flask,request, render_template
import numpy as np
import pickle
import sklearn
#loading models
model = pickle.load(open('model.pkl','rb'))
#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Item_Indentifier = request.form["Item_Identifier"]
        Item_weight = request.form["Item_weight"]
        Item_Fat_Content = request.form["Item_Fat_Content"]
        Item_visibility = request.form["Item_visibility"]
        Item_Type = request.form["Item_Type"]
        Item_MPR = request.form["Item_MPR"]
        Outlet_identifier = request.form["Outlet_identifier"]
        Outlet_established_year = request.form["Outlet_established_year"]
        Outlet_size = request.form["Outlet_size"]
        Outlet_location_type = request.form["Outlet_location_type"]
        Outlet_type = request.form["Outlet_type"]


        features = np.array([[Item_Indentifier,Item_weight,Item_Fat_Content,Item_visibility,Item_Type,Item_MPR,Outlet_identifier,Outlet_established_year, Outlet_size, Outlet_location_type,Outlet_type]],dtype=np.float32)
        transformed_feature = features.reshape(1, -1)
        prediction = model.predict(transformed_feature)[0]
        print(prediction)
        return render_template('index.html',prediction = prediction)

if __name__=="__main__":
    app.run(debug=True)