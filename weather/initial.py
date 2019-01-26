from google.cloud import bigquery
def getData():
    client = bigquery.Client()
    query = (
        "SELECT * FROM `bigquery-public-data.noaa_tsunami.historical_runups` LIMIT 10"
    )
    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        location="US",
    )  # API request - starts the query

    for row in query_job:  # API request - fetches results
        # Row values can be accessed by field name or index
        # assert row["state"]

   #     return row[7]
        print(row[9])
        #print("\n")
        #noaa_tsunami
        #noaa_significant_earthquakes
        #noaa_spc
if __name__ == '__main__':
    getData()