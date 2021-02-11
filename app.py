import requests, io
import pandas as pd
from flask import Flask

# initialize flask app 
app = Flask(__name__)

@app.route('/')
def default():
    # retrive data from report services
    try:
        res_csv  = requests.get('https://run.mocky.io/v3/ba026992-281a-42a6-8447-ae1c8a04106e')
        res_json = requests.get('https://run.mocky.io/v3/9a01a1b9-26e1-4c8a-84db-d534352e1461')
    except Exception as e:
        print('Error retriving data : ',e)
        return {'msg':'Error in retriving service data.'}, 500

    # converting response to dataframe
    df_csv  = pd.read_csv(io.StringIO(res_csv.text))
    df_json = pd.read_json(res_json.text)

    if df_csv.empty and df_json.empty:
        return {'msg':'DataFrames are empty'}, 200

    # concatinating impression columns in both dataframes
    impressions = df_csv['impression'].append(df_json['impressions'])

    # calculating sum and mean of combined impression
    imp_sum  = int(impressions.sum())
    imp_mean = round(float(impressions.mean()),2)

    return {'mean': imp_mean, 'sum': imp_sum},200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)