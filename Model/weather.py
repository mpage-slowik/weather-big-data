from sqlobject import *
from google.cloud import bigquery
import simplejson as json
import json
import pandas as pd

def getWindReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.wind_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(query)  # API request - starts the query
    
    windData = {}
    i = 0
    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])

        windData[i] = {'longitude': [d['longitude']], 'latitude': [d['latitude']]}
        i = i +1
    df = pd.DataFrame(data=windData)
    print(df)
    return df

def getTornadoReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.tornado_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(query)  # API request - starts the query

    tornData = {}
    i = 0

    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        tornData[i] = {'longitude': [d['longitude']], 'latitude': [d['latitude']]}
        i = i +1
    df = pd.DataFrame(data= tornData)
    print(df)
    return df

def getHailReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.hail_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(query)  # API request - starts the query

    hailData = {}
    i = 0
    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        hailData[i] = {'longitude': [d['longitude']], 'latitude': [d['latitude']]}
        i = i +1
    df = pd.DataFrame(data = hailData)
    print(df)
    return df

if __name__ == '__main__':
    getTornadoReports()

