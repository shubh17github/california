
from flask import Flask,request,url_for,render_template,redirect
from function import house_price

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('house_input.html')


@app.route('/house',methods=['GET','POST'])

def house():
    if request.method=='POST':
        
        data=request.form
        longitude=float(data['longitude'])
        latitude=float(data['latitude'])
        housing_median_age=int(data['housing_median_age'])
        total_rooms=int(data['total_rooms'])
        total_bedrooms=int(data['total_bedrooms'])
        population=int(data['population'])
        households=int(data['households'])
        median_income=float(data['median_income'])
        ocean_proximity=data['ocean_proximity']

    price_obj=house_price(longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity)

    predicted_price=price_obj.price_predict()
    # return 'Prediction API'
    return render_template('house_input.html',predict=predicted_price)
    # return redirect(url_for("res", predic=predicted_price[0]))

# @app.route('/result/<string:predic>', methods=['GET'])
# def res(predic):

#     return render_template('price.html',prediction=predic)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
    # app.run(debug=True)
