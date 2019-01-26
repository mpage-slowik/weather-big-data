from google.cloud import bigquery
def getData():
    client = bigquery.Client()
    query = (
        "SELECT * FROM `bigquery-public-data.noaa_significant_earthquakes.historical_runups` LIMIT 10"
    )
    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        # location="US",
    )  # API request - starts the query

    for row in query_job:  # API request - fetches results
        # Row values can be accessed by field name or index
<<<<<<< HEAD
        # assert row["state"]

   #     return row[7]
        print(row[9])
        #print("\n")
=======
        # assert row[0] == row.name == row["state"]

        # return row[7]
        print(row[7])
        print("\n")
>>>>>>> 4056bebf7f415a9997203148c194c6a9cb006317
        #noaa_tsunami
        #noaa_significant_earthquakes
        #noaa_spc
if __name__ == '__main__':
    getData()