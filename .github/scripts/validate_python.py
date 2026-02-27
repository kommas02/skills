#!/usr/bin/env python3
import py_compile
import sys
import os
import glob

errors = []

for py_file in glob.glob("skills/**/*.py", recursive=True):
    if not os.path.isfile(py_file):
        continue
    try:
        py_compile.compile(py_file, doraise=True)
        print(f'{py_file} syntax valid')
    except py_compile.PyCompileError as e:
        print(f'Error: {py_file} has syntax error: {e}')
        errors.append(py_file)

if errors:
    sys.exit(1)
print('All Python files valid')
