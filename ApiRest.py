
from flask import Flask, request, Response, jsonify, json
import time


import extract_msg
import re
import pandas as pd

import psycopg2
import pandas as pd
import pandas.io.sql as psql

conn = psycopg2.connect(database="tradedetail", user="tradedetail", password="tradedetail", host="bvmnglapsboxp01.nngg.corp", port="5432",client_encoding='utf-8')
cur = conn.cursor()

app = Flask(__name__)



def find_isin(msg_message, msg_subj):
    #msg = extract_msg.Message(f)
    #msg_sender = msg.sender
    #msg_date = msg.date
    #msg_subj = msg.subject
    msg_message = msg_message
    msg_subj = msg_subj


    if msg_message == '':
        isin = re.findall('[A-Z]{2}[A-Z0-9]{9}[0-9]', msg_subj)
        date = re.findall(r"(tom|TOM|T/-|spot|spot/open)", msg_subj)
    else:
        isin = re.findall('[A-Z]{2}[A-Z0-9]{9}[0-9]', msg_message)
        date = re.findall(r"(tom|TOM|T/-|spot|spot/open)", msg_message)
    return isin, date



@app.route("/person", methods=['POST', 'GET']) # aquí especificamos que estos endpoints aceptan solicitudes. 



def handle_person(): 
    if request.method == 'POST': 
        msg_message = request.args.get('msg_message')
        msg_subj = request.args.get('msg_subj')
        print(msg_message)
        print(msg_subj)
                
        msg_message, date = find_isin(msg_message, msg_subj)
        isim = str(msg_message)
        date = str(date)
        
        isim = re.sub("\[|\]","",isim)
        date = re.sub("\[|\]","",date)
        spot=0
        tom=0
        
        print("isim, date despues del corte", isim, date)
        try:
            df = psql.read_sql("Select spot, tom from bot where seccode = " + str(isim) , conn)
            spot=str(df.iloc[0]['spot'])
            tom=str(df.iloc[0]['tom'])
        except:
            print("error")
            
        #busca_isim(msg_message, date)
        print(isim, date, spot, tom)      
        
        return(jsonify(isim=str(isim), date=str(date), spot=spot, tom=tom),200)
        #return(jsonify(isim=isim, date=date),200)
       


if __name__ == "__main__":
    app.run(host='bvmnglapsboxp01.nngg.corp', port=8080)



