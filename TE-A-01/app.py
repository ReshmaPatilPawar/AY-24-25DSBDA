from flask import Flask, request, render_template
import joblib
import numpy as np
import datetime

app = Flask(__name__)

model  = joblib.load('Prediction_Model')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        price = float(request.form['price'])
        kms = float(request.form['kms'])
        fuel = request.form['fuel']
        seller = request.form['seller']
        mode = request.form['mode']
        own = int(request.form['own'])
        year = request.form['year']
        current_year = datetime.datetime.now().year
        age = current_year - int(year)

        
        #fuel
        
        if(fuel == 'CNG'):
            fuel=2
        elif(fuel == 'Diesel'):
            fuel=1    
        else:
            fuel=0
            
        
        #seller
        
        if(seller == 'Dealer'):
            seller=0
        else:
            seller=1
            
        #mode
        
        if(mode == 'Manual'):
            mode=0
        else:
            mode=1
            
            
        prediction = model.predict([[price,kms,fuel,seller,mode,own,age]])
        final_price= round(prediction[0],2)
        
        return render_template("prediction.html", prediction_text=" {}".format(final_price))    
        
    else:
        return render_template("prediction.html")  
            
            
           
            
        
        




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')