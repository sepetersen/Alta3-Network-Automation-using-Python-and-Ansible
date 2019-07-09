#!/usr/bin/env python3

import yaml

def main():
    ## open a yaml file
    yammyfile = open("/home/student/mycode/yamlintro/myYAML.yml", "r")

    ## convert yaml inot python data structures (lists and dictionaries)
    pyyammy = yaml.load(yammyfile)

    ## display new python data
    print(pyyammy)

main()
