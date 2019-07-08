#!/usr/bin/env python3
"""using csv datat"""
import csv

def main():
    # open the csv data set
    with open("vendor.csv", "r") as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=",")
        # the csv data is now nicely prepared
        # each new row is a python list
        # we can reference the items we want to print
        # as we loop over the data
        for row in vendata:
            print ("The IP address " + row[2] + \
                    " requires the driver " + row[3])

main()
