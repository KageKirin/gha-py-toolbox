#!/usr/bin/env python3

import os, sys
from pathlib import Path
import black
from ruamel.yaml import YAML

ruaml = YAML()
ruaml.default_flow_style = False
ruaml.width = 4096
ruaml.indent(mapping=2, sequence=2, offset=0)


def add_code_section_name(code, step, filename):
    section_name = f"## {filename}#{step}"
    if not code.startswith(section_name):
        return section_name + "\n" + code
    return code


def black_format(code):
    BLACK_MODE = black.Mode(target_versions={black.TargetVersion.PY311}, line_length=80)
    try:
        code = black.format_file_contents(code, fast=False, mode=BLACK_MODE)
    except black.NothingChanged:
        pass
    # except black.parsing.InvalidInput:
    finally:
        if code and code[-1] != "\n":
            code += "\n"
    return code


for arg in sys.argv[1:]:
    p = Path(arg)
    if p.suffix == ".yml":
        yaml_data = ruaml.load(p)
        if yaml_data is None:
            continue

        runs = yaml_data.get("runs")
        if runs is None:
            continue

        steps = runs.get("steps", [])
        for step in filter(lambda s: "shell" in s and s["shell"] == "python", steps):
            print(f'formatting "{p}#{step.get("id")}"')
            step["run"] = add_code_section_name(
                code=step["run"], step=step.get("id", ""), filename=str(p)
            )
            step["run"] = black_format(code=step["run"])
        for step in filter(lambda s: "shell" in s and s["shell"] == "cat {0}", steps):
            print(f'formatting "{p}#{step.get("id")}"')
            step["run"] = add_code_section_name(
                code=step["run"], step=step.get("id", ""), filename=str(p)
            )

        ruaml.dump(yaml_data, p)


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
