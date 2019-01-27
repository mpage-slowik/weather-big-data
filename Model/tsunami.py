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

    lng, lat = [],[]
    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        lng.append(d['longitude'])
        lat.append(d['latitude'])
    df = pd.DataFrame({'lng':lng,'lat':lat})

    return df



def getMostOccurentTsunami():
    client = bigquery.Client()

    query = (
        "SELECT TO_JSON_STRING(t,true)" + "FROM ( "+
        "SELECT country, COUNT(*) AS cnt "+
        "FROM `bigquery-public-data.noaa_tsunami.historical_runups` " +
        "GROUP BY country "+
        "ORDER BY cnt DESC " + "LIMIT 1000"+
        ") as t"
    )
    
    query_job = client.query(query)

    for row in query_job:  # API request - fetches results
        print (row[0])


            
if __name__ == '__main__':
  # d =  getDataTsunami()
  # print (d)
  #make pi chart with
  getMostOccurentTsunami()

