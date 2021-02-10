import requests, io
import pandas as pd
from flask import Flask


app = Flask(__name__)


@app.route('/')
def default():
    try:
        res_csv  = requests.get('https://run.mocky.io/v3/ba026992-281a-42a6-8447-ae1c8a04106e')
        res_json = requests.get('https://run.mocky.io/v3/9a01a1b9-26e1-4c8a-84db-d534352e1461')
    except Exception as e:
        print('Error retriving data : ',e)
        return None
    df_csv  = pd.read_csv(io.StringIO(res_csv.text))
    df_json = pd.read_json(res_json.text)

    impressions = df_csv['impression'].append(df_json['impressions'])
    imp_sum  = int(impressions.sum())
    imp_mean = round(float(impressions.mean()),2)

    return {'mean': imp_mean, 'sum': imp_sum},200



# @app.route('/')
# def default():
#     res = requests.get('https://run.mocky.io/v3/ba026992-281a-42a6-8447-ae1c8a04106e')

#     # res = requests.get('https://run.mocky.io/v3/9a01a1b9-26e1-4c8a-84db-d534352e1461')
#     isJson = False
#     # using EAFP
#     # # ref: https://docs.python.org/2/glossary.html#term-eafp
#     try:
#         df = pd.read_json(res.text)
#         impressions = df['impressions']
#         isJson = True
#     except ValueError as e:
#         print('Text is not json ',e) 
#     if not isJson:
#         try:
#             df = pd.read_csv(io.StringIO(res.text))
#             impressions = df['impression']
#         except ValueError as e:
#             print('Text is not Dataframe ',e) 

#     imp_sum  = int(impressions.sum())
#     imp_mean = round(float(impressions.mean()),2)

#     return {'mean': imp_mean, 'sum': imp_sum},200






