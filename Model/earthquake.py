from sqlobject import *
from google.cloud import bigquery
import simplejson

class Earthquake(SQLObject):

    name = StringCol()
    artist = StringCol()
    album = StringCol()

def getData():
    client = bigquery.Client()
    query = (
        "SELECT * FROM `bigquery-public-data.noaa_significant_earthquakes.earthquakes` LIMIT 100"
    )
    query_job = client.query(
        query,
    )  # API request - starts the query

    for row in query_job:  # API request - fetches results
        # Row values can be accessed by field name or index
        assert row[0] == row.id 

        print(row)
        print(simplejson.dumps(row))
        print("\n")
        break

def getJsonData(row):
    if (1 == 1):
        print(1)

def Main():
    if (1 == 1):
        print(1)


if __name__ == '__main__':
    getData()