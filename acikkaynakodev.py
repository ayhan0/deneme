from flask import Flask
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with
from datetime import datetime
import pandas as pd 

app = Flask(__name__)
api = Api(app)
#Employees.csv udemy deki kursta veri analizinden kullandığım bir csv dosyası verileri yabancı dilde ve açık kanyak
class Kullanici(Resource):
	def get(self):
		veri = pd.read_csv('employees.csv')
		veri = veri.to_dict("records")
		return {'veri':veri},200
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('First_Name',required = False)
		parser.add_argument('Gender',required = False)
		parser.add_argument('Team',required = False)
		parser.add_argument('Salary',type = int,required =False)
		parser.add_argument('BaslangicTarihi',type =strftime("%m %d %y"))
		parser.add_argument('SonGirisTarihi',type =strftime("%m %d %y %H:%M:%S"))
		args = parser.parse_args()

		veri = pd.read_csv('employees.csv')

		veriler = pd.DataFrame ({
		'First_Name'  :[args ['First_Name']],
		'Gender'  :[args ['Gender']],
		'Team'  :[args ['Team']],
		'Salary'  :[args ['Salary']],
		'BaslangicTarihi'  :[args ['BaslangicTarihi']],
		'SonGirisTarihi'  :[args ['SonGirisTarihi']]
		})

		veri = veri.append(veriler, ignore_index = True)
		veri.to_csv ('kullanici.csv',index = False)
		return {'veri': veriler.to_dict('records')},201
	def isimbul(First_Name):
		if First_Name not in veri["First_Name"]:
			abort(404,message="aradığınız isim bulunamadı")
		else:
			print("Deleted successfuly")
	def delete (self,First_Name):
		del veri[First_Name]
		return "",204

api.add_resource(Kullanici,'/kullanici')
if __name__ == "__main__":
     app.run(debug=True) 
    