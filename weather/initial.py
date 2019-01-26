from google.cloud import bigquery
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
    assert row[0] 
    # == row.name == row["name"]
    print(row[7])
    print("\n")

#from google.cloud import storage
