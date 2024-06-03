#!/usr/bin/env python3

import os, sys
from pathlib import Path
import black
from ruamel.yaml import YAML

ryaml = YAML()

def black_format(code):
    BLACK_MODE = black.Mode(target_versions={black.TargetVersion.PY311}, line_length=80)
    try:
        code = black.format_file_contents(code, fast=False, mode=BLACK_MODE)
    except black.NothingChanged:
        pass
    finally:
        if code and code[-1] != "\n":
            code += "\n"
    return code

for arg in sys.argv[1:]:
    p = Path(arg)
    if p.suffix == ".yml":
        yaml_data = ryaml.load(p)
        # (yaml_data, doc_loaded) = Parsers.get_yaml_data(yaml, log, p)
        print(yaml_data)
        for step in filter(lambda s: s["shell"] == "python", yaml_data["runs"]["steps"]):
            step["run"] = black_format(code=step["run"])
        ryaml.dump(yaml_data, p)




"""
TODO: 
    * load YAML
    * find steps where shell is 'python'
    * copy scipt into temp source
    * black-format temp source
    * write formatted code back
    
    
runs.steps.[].run
"""

"""
from types import SimpleNamespace

from yamlpath.common import Parsers
from yamlpath.wrappers import ConsolePrinter
from yamlpath import Processor
from yamlpath import YAMLPath
from yamlpath.exceptions import YAMLPathException
yaml_path = YAMLPath("runs.steps.[].run")
logging_args = SimpleNamespace(quiet=True, verbose=False, debug=False)
log = ConsolePrinter(logging_args)
yaml = Parsers.get_yaml_editor()
#(yaml_data, doc_loaded) = Parsers.get_yaml_data(yaml, log, p)
"""
