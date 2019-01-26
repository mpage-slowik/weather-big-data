from google.cloud import bigquery
import json


def getDataTsunami():
    client = bigquery.Client()
    query = (
        "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_tsunami.historical_runups` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
    )
    
    query_job = client.query(query)  # API request - starts the query
     # API request - starts the query
    tsuData = [] 

    for row in query_job:  # API request - fetches results
        js =  json.loads(row[0])
        coord = {
            'longitute' : js['longitude'],
            'latitude' : js['latitude']
        }
        print (coord)
        tsuData.append(coord)
        print("\n")

        

if __name__ == '__main__':
    getDataTsunami()

