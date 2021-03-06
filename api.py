from flask import Flask, request
from flask_restful import Resource, Api
import json, random

app = Flask(__name__)
api = Api(app)

class Refran:
	def get_refran(self, refranes):
		return refranes[random.randint(0,len(refranes)-1)]
	
	def generate_refran(self):
		refran = self.get_refran(json.load(open('refranes.json'))["texto"])
		return refran
		
if __name__ == '__main__':
    print(Refran().generate_refran())
