import boto3


def handler(event, context):
    db = boto3.resource("dynamodb")
    table = db.Table("intersections_4")
    # function that returns lat/long of current location gets called
    coordinates = (41.716344, -72.685169)
    lat = coordinates[0]
    lon = coordinates[1]

    # hashing lat and long values
    hashPrecision = 2
    geohash = str(round(lat, hashPrecision)) + "-" + str(round(lon, hashPrecision))

    # getting coordinates from table using hash (primary key)
    data = table.get_item(Key=geohash)

    # filtering returned data in order to perform calculations
    return data["Item"]
