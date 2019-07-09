#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
from pprint import pprint as pp # part of the standard library

## Define APOD
NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MKEY = 'api_key=1qgDvRdvdDb0AW6wZiQ6lATNTsGfz4WPOZwwohyR'

## Call the webservice
#apodurlobj = urllib.request.urlopen(apodurl + mkey)

## read the file-like object
#apodread = apodurlobj.read()

## decode json to python data structure
#decodeapod = json.loads(apodread.decode('utf-8'))

## display our pythonic data
#print("\n\nConverted python data")
#print(decodeapod)

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MKEY) # call the webservice
    nasaread = nasaapiobj.read() # parse the json into python
    convertedjson = json.loads(nasaread.decode('utf-8')) # convert json

    # Show converted json
    print (convertedjson) # show converted json without pprint
    input('\nThis is converted json.  Press ENTER  to continue.') # pause for enter

    # Show Pretty print json
    pp(convertedjson) # this is pretty print in action

    # Print the description of the photo we are about to view
    print(convertedjson['explanation']) # display the value for the key explanation
    input ('\nPress ENTER to view this photo of the day') # pause for ENTER

    ## use firefox to open the HTTPS URL
    input('\nPress Enter to open NASA Picture of the Day in Firefox')
    webbrowser.open(decodeapod['url'])

main()
