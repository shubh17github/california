
import numpy as np
import json
import config
import pickle


class house_price():


    def __init__(self,longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity):
        """ init function for accepting the User Input """     
        self.longitude=longitude
        self.latitude=latitude
        self.housing_medain_age=housing_median_age
        self.total_rooms=total_rooms
        self.total_bedrooms=total_bedrooms
        self.population=population
        self.households=households
        self.median_income=median_income
        self.ocean_proximity=ocean_proximity

    def load_model(self):
        with open(config.model_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.column_list_path,'r') as file:
            self.col_dict=json.load(file)

    def price_predict(self):

        self.load_model()

        array=np.zeros(len(self.col_dict['column']))

        array[0]=self.longitude
        array[1]=self.latitude
        array[2]=self.housing_medain_age
        array[3]=self.total_rooms
        array[4]=self.total_bedrooms
        array[5]=self.population
        array[6]=self.households
        array[7]=self.median_income

        
        ocean_proximity_index1=self.col_dict['column'].index(self.ocean_proximity)
        array[ocean_proximity_index1]=1



        #print(array)

        result =self.model.predict([array])
        #print(result)

        return result[0]

if __name__=='__main__':
  longitude=-122.23
  latitude=37.88
  housing_median_age=41
  total_rooms=880
  total_bedrooms=129
  population=322
  households=126
  median_income=8.3252
  ocean_proximity='NEAR BAY'
#   4	-122.25	37.85	52	1627	280.0	565	259	3.8462	NEAR BAY	342200

  house_price_obj=house_price(longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity)
  v=house_price_obj.price_predict()
  print(v)







