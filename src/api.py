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
    logging data(f"providing list of data types")



@app.route("/type/Coverage",methods = ['GET'])
def coverage_data():
    '''

    '''
    logging.info(f"obtaining coverage data")
@app.route("/type/Coverage/domain",methods= ['GET'])
def domaiin_lists():
    '''
    '''
    logging.info(f"obtaining domain lists")


@app.route('/referencing',methods = ['GET'])
def reference_list():
    '''
    '''
    logging.info(f"obtaining reference lists")

@app.route('/coordinates',methods = ['GET'])
def coordinate_data():
    '''
    '''
    logging.info(f"providing coordinates")

@app.route('/ranges',methods = ['GET'])
def range_data():
    '''
    '''
    logging.info(f"lists every possible range")
@app.route('/ALLSKY_SFC_LW_DWN',methods=['GET'])
def all_sky_down():
    ''' 
    '''
    logging.info(f"All of low sky data")

@app.route('/TOA_SW_DWN',methods = ['GET'])
def TOA_data():
    '''
    '''
    logging.info(f"TOA DATA")
