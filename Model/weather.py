from google.cloud import bigquery
import json
import pandas as pd

def getWindReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.wind_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 1000" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(query)  # API request - starts the query
    
    lng, lat = [],[]
    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        lng.append(d['longitude'])
        lat.append(d['latitude'])
    df = pd.DataFrame({'lng':lng,'lat':lat})
    return df

def getTornadoReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.tornado_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 1000" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(query)  # API request - starts the query
    lng, lat = [],[]
    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        lng.append(d['longitude'])
        lat.append(d['latitude'])
    df = pd.DataFrame({'lng':lng,'lat':lat})
    return df

def getHailReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.hail_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 1000" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(query)  # API request - starts the query

    lng, lat = [],[]
    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        lng.append(d['longitude'])
        lat.append(d['latitude'])
    df = pd.DataFrame({'lng':lng,'lat':lat})
    return df

if __name__ == '__main__':
    getTornadoReports()

