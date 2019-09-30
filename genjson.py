import yaml, json, sys, pprint
from pprint import pprint

yaml_file_name = sys.argv[1]
with open(yaml_file_name) as f:
    pprint(json.dumps(yaml.load(f, Loader=yaml.FullLoader)))


