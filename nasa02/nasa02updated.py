#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # api url
    startdate = 'start_date=2019-06-01' ## start date for data
    enddate = '&end_date=2019-07-09' ## end date
    mykey = '&api_key=1qgDvRdvdDb0AW6wZiQ6lATNTsGfz4WPOZwwohyR' # api key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print (neojson)

## call main
main()
