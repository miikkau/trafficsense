#!/usr/bin/python

import json
from pprint import pprint
# uses https://github.com/Julian/jsonschema
from jsonschema import validate


json_data = open('journey.js')
data = json.load(json_data)
json_schema = open('route_schema.js')
schema = json.load(json_schema)

validate(data, schema)

json_data.close()
json_schema.close()
