#!/usr/bin/env python

import json
import jsonschema

res1 = json.load(open('./res/res1.json'))
res2 = json.load(open('./res/res2.json'))
schema = {'$ref': 'http://localhost:8000/schemas/schema.json'}

print jsonschema.validate(res1, schema)
print jsonschema.validate(res2, schema)

import jsonref
res = jsonref.load(open('./res/res1.json'))
print res
