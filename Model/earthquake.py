from google.cloud import bigquery
import json
import pandas as pd

def getData():
    data = getJsonData()
    print(data)
def getJsonData():
    client = bigquery.Client()
    query = (
        "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
                "SELECT  * FROM `bigquery-public-data.noaa_significant_earthquakes.earthquakes` " +
                "WHERE latitude IS NOT NULL AND longitude IS NOT NULL AND ID IS NOT NULL " +
                "LIMIT 10" +
            ") as t"
    )
    query_job = client.query(query)  # API request - starts the query
    t = {}
    i = 0
    for row in query_job:  # API request - fetches results
        # Row values can be accessed by field name or index
        d = json.loads(row[0])

        t[i] = {'longitude': [d['longitude']], 'latitude': [d['latitude']]}
        i = i +1
    df = pd.DataFrame(data=t)
    return df


if __name__ == '__main__':
    getData()