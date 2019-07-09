#!/usr/bin/env python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)

    ## put fileobject ino helmet
    helmet = groundctrl.read()

    ## decode json to python data structure
    helmetson = json.loads(helmet.decode('utf-8'))

    ## display our pythonic data
    print ("\n\nConverted python data")
    print (helmetson)

    print ('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    # 
    for i in people:
        print (i['name'],"on the",i['craft'])
        
main()
