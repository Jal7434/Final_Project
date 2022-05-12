import json 
import csv
import redis 
from typing import List
from flask import Flask, request, jsonify
import logging 

logging.basicConfig(level= logging.DEBUG)

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def help() -> str:
    """
 
    """
    if(request.method == 'GET'):


@app.route('/data',methods =['POST'] )
def loading_data():
    '''
    ''' 
    data = {}
    count = 0 
    data['rad_data'] =[]
    with open("power_901_annual_radiation_utc.nc.covjson",'r') as f:
         dataset = json.load(f)
         
   return f'File has been upload'

@app.route("/type",methods =['GET'])
def data_type():
    '''
    '''




@app.route("/type/Coverage",methods = ['GET'])
def coverage_data():




@app.route("/type/Coverage/domain",methods= ['GET'])
def domaiin_lists():





