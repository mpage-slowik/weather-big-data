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

    data = []

    for row in query_job:  # API request - fetches results
        d = json.loads(row[0])
        cords = {
            'longitude': d['longitude'],
            'latitude': d['latitude']
        }
        print(cords)
        data.append(cords)
        print("\n")

    return data


if __name__ == '__main__':
    getWindReports()

