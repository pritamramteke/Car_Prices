from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
    if request.method == 'POST':
        symboling = int(request.form['symboling'])
        normalized_losses=float(request.form['normalized_losses'])
        
        Fuel_type=request.form['Fuel_type']
        if(Fuel_type=='gas'):
                Fuel_type=1
        else:
            Fuel_type=0

        make=request.form['make']
        if(make=='std'):
            make=0
        else:
            make=1

        num_of_doors=request.form['num_of_doors']
        if(num_of_doors=='two'):
            num_of_doors=1
        else:
            num_of_doors=0

        aspiration = request.form['aspiration']
        if (aspiration == 'convertible'):
            aspiration = 0
        elif (aspiration == 'hatchback'):
            aspiration = 2
        elif (aspiration == 'sedan'):
            aspiration = 3
        elif (aspiration == 'wagon'):
            aspiration = 4
        elif (aspiration == 'hardtop'):
            aspiration = 1

        wheel_base = request.form['wheel_base']
        if (wheel_base == 'rwd'):
            wheel_base = 2
        elif (wheel_base == 'fwd'):
            wheel_base = 1
        else:
            wheel_base = 0

        engine_location = request.form['engine_location']
        if (engine_location == 'front'):
            engine_location = 0
        else:
            engine_location = 1

        drive_wheels = int(request.form['drive_wheels'])

        body_style = request.form['body_style']
        if (body_style == 'alfa-romero'):
            body_style = 0
        elif (body_style == 'audi'):
            body_style = 1
        elif (body_style == 'bmw'):
            body_style = 2
        elif (body_style == 'chevrolet'):
            body_style = 3
        elif (body_style == 'dodge'):
            body_style = 4
        elif (body_style == 'honda'):
            body_style = 5
        elif (body_style == 'isuzu'):
            body_style = 6
        elif (body_style == 'jaguar'):
            body_style = 7
        elif (body_style == 'mazda'):
            body_style = 8
        elif (body_style == 'mercedes-benz'):
            body_style = 9
        elif (body_style == 'mercury'):
            body_style = 10
        elif (body_style == 'mitsubishi'):
            body_style = 11
        elif (body_style == 'nissan'):
            body_style = 12
        elif (body_style == 'peugot'):
            body_style = 13
        elif (body_style == 'plymouth'):
            body_style = 14
        elif (body_style == 'porsche'):
            body_style =15
        elif (body_style == 'renault'):
            body_style = 16
        elif (body_style == 'saab'):
            body_style = 17
        elif (body_style == 'subaru'):
            body_style = 18
        elif (body_style == 'toyota'):
            body_style = 19
        elif (body_style == 'avolkswagen'):
            body_style = 20
        else:
            body_style = 21

        length = int(request.form['length'])

        width = int(request.form['width'])

        height = int(request.form['height'])

        curb_weight = int(request.form['curb_weight'])

        engine_type = request.form['engine_type']
        if (engine_type == 'dohc'):
            engine_type = 0
        elif (engine_type == 'ohcv'):
            engine_type = 5
        elif (engine_type == 'ohc'):
            engine_type = 3
        elif (engine_type == 'l'):
            engine_type = 2
        elif (engine_type == 'rotor'):
            engine_type = 6
        elif (engine_type == 'ohcf'):
            engine_type = 4
        else:
            engine_type = 1

        num_of_cylinders = int(request.form['num_of_cylinders'])

        engine_size = int(request.form['engine_size'])

        fuel_system = request.form['fuel_system']
        if (fuel_system == 'mpfi'):
            fuel_system = 5
        elif (fuel_system == '2bbl'):
            fuel_system = 1
        elif (fuel_system == 'mfi'):
            fuel_system = 4
        elif (fuel_system == '1bbl'):
            fuel_system = 0
        elif (fuel_system == 'spfi'):
            fuel_system = 7
        elif (fuel_system == '4bbl'):
            fuel_system = 2
        elif (fuel_system == 'idi'):
            fuel_system = 3
        else:
            fuel_system = 6

        bore = float(request.form['bore'])

        stroke = float(request.form['stroke'])

        compression_ratio = int(request.form['compression_ratio'])

        horsepower = int(request.form['horsepower'])

        peak_rpm = int(request.form['peak_rpm'])

        city_mpg = int(request.form['city_mpg'])

        highway_mpg = int(request.form['highway_mpg'])



        prediction=model.predict([[symboling, normalized_losses, Fuel_type, make, num_of_doors,
        aspiration, wheel_base, engine_location, drive_wheels,
        body_style, length, width, height, curb_weight, engine_type,
        num_of_cylinders, engine_size, fuel_system, bore, stroke,
        compression_ratio, horsepower, peak_rpm, city_mpg,highway_mpg]])

        output=round(prediction[0],2)

        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

