#!/usr/bin/env python3
import urllib.request
import json

## Define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=2019-07-09'
mykey = '&api_key=1qgDvRdvdDb0AW6wZiQ6lATNTsGfz4WPOZwwohyR'

neourl = neourl + startdate + mykey

## Call the webservice
neourlobj = urllib.request.urlopen(neourl)

## read the file-like object
neoread = neourlobj.read()

## decode json to python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## display our pythonic data
print ("\n\nConverted python data")
print (decodeneo)
