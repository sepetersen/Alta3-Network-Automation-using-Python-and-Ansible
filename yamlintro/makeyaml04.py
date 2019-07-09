#!/usr/bin/env python3

import yaml

def main():
    ## open a yaml file
    yammyfile = open("/home/student/mycode/yamlintro/myYAML.yml", "r")

    ## convert yaml inot python data structures (lists and dictionaries)
    pyyammy = yaml.load(yammyfile)

    ## close file
    yammyfile.close()

    ## display new python data
    print(pyyammy)

    ## mincraft to the list of apps
    pyyammy[0]['apps'].append('minecraft')

    ## Did the python data change?
    print(pyyammy)

    ## open a file to dump out to
    yammyfile2 = open("/home/student/mycode/yamlintro/myYAML.yml.updated", "w")

    ## use the yaml library
    yaml.dump(pyyammy, yammyfile2)

    ## close our file
    yammyfile2.close()

main()
