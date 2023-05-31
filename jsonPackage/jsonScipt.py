#!/usr/bin/env python3

from pathlib import Path
from json import dump

objs = {"name": "elgibbor", "colour": "white", "age": 100 }

jsonString = "j_file"
jsonDir = Path('jsonPackage/jsonFolder')
jsonPath = jsonDir / (jsonString + ".json")

# create directory if it doesnt exit
jsonDir.mkdir(exist_ok=True)
with open("jsonfile.json", "w") as f:
    dump(objs, f)
    # jsonPath.write_text(dumps(objs))
