from sqlobject import *
from google.cloud import bigquery
import simplejson as json

def getWindReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.wind_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        location="US",
    )  # API request - starts the query

    windData = []

    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        cords = {
            'longitude': d['longitude'],
            'latitude': d['latitude']
        }
        print(cords)
        winData.append(cords)
        print("\n")

    return windData

def getTornadoReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.tornado_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        location="US",
    )  # API request - starts the query

    tornData = []

    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        cords = {
            'longitude': d['longitude'],
            'latitude': d['latitude']
        }
        print(cords)
        tornData.append(cords)
        print("\n")

    return tornData

def getHailReports():
    client = bigquery.Client()
    query = (
             "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_spc.hail_reports` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
        # "SELECT * FROM `bigquery-public-data.noaa_spc.wind_reports` LIMIT 1"
    )
    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        location="US",
    )  # API request - starts the query

    hailData = []

    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        cords = {
            'longitude': d['longitude'],
            'latitude': d['latitude']
        }
        print(cords)
        hailData.append(cords)
        print("\n")

    return hailData

if __name__ == '__main__':
    getHailReports()

