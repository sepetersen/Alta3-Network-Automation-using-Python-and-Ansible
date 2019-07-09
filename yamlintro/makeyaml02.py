#!/usr/bin/env python3

## yaml is NOT part of the standard library
import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
            {"name": "Arthur Dent", "species": "Human"}]
    ## display our python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    zfile = open("galaxyguide.yaml", "w")

    ## use the yaml library
    ## usage: yaml.dump(input data, file object)
    ## unlike json, the yaml lib uses .dump() to creat yaml strings and write to files
    ## the json lib uses .dump() to create a string and .dumps() to write to files
    #yaml.dump(hitchhikers, zfile)

    ## close the file when we are done
    #zfile.close()

    ## Create a yaml string
    yamlstring = yaml.dump(hitchhikers)

    ## Display a single string of yaml
    print(yamlstring)

main()
