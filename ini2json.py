# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import configparser
import json
import sys

inifile = sys.argv[1]

config = configparser.RawConfigParser()
config.optionxform = str

jsonconfig = {}
config.read(inifile)

for item in config['default']:
    jsonconfig[item] = config['default'][item]

print(json.dumps(jsonconfig))