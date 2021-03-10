#!/usr/bin/python
import json, pprint

load_file="/home/saif/Documents/new_env/lib/python2.7/site-packages/pip-1.5.4.dist-info/pydist.json"

with open(load_file) as json_file:
  data = json.load(json_file)

print pprint.pprint(data)
 
