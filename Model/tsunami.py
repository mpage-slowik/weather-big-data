from google.cloud import bigquery
import json
import pandas as pd


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
    tsunamiData = []
    coord = {}
    i = 0

    for row in query_job:  # API request - fetches results
        js =  json.loads(row[0])
        coord[i] = {

            'longitute' : js['longitude'],
            'latitude' : js['latitude']
        }
        
        i = i + 1

    df = pd.DataFrame(data=coord)
    tsunamiData.append(df)

    return tsunamiData



def getMostOccurentTsunami():
    client = bigquery.Client()

    query = (
        "SELECT TO_JSON_STRING(t,true)" + "FROM ( "+
        "SELECT country, COUNT(*) AS cnt "+
        "FROM `bigquery-public-data.noaa_tsunami.historical_runups` " +
        "GROUP BY country "+
        "ORDER BY cnt DESC " + "LIMIT 5"+
        ") as t"
    )
    
    query_job = client.query(query)

    for row in query_job:  # API request - fetches results
        print (row[0])


            
if __name__ == '__main__':
  # d =  getDataTsunami()
  # print (d)
  getMostOccurentTsunami()

