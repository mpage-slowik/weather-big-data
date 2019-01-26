from google.cloud import bigquery
import simplejson

# class Earthquake():

    # country = StringCol()
    # latitude = StringCol()
    # longitude = StringCol()

def getData():
    client = bigquery.Client()
    query = (
        "SELECT TO_JSON_STRING(t,true)" + "FROM ( "
        "SELECT  * FROM `bigquery-public-data.noaa_significant_earthquakes.earthquakes` " +
        "WHERE latitude IS NOT NULL AND longitude IS NOT NULL " +
        "LIMIT 10" +") as t"
    )
    query_job = client.query(query)  # API request - starts the query

    for row in query_job:  # API request - fetches results
        # Row values can be accessed by field name or index
        print(row[0])
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