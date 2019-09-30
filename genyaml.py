import json
import yaml
import sys

json_file_name = sys.argv[1]
jsonf = open(json_file_name, 'r')
j = json.load(jsonf)
print(yaml.dump(j))
