#!/usr/bin/env python

import commentjson as json
import jsonschema

res = json.load(open('./res.json'))
schema = json.load(open('./schema.json'))

print jsonschema.validate(res, schema)
