#!/usr/bin/env python3
import yaml
import sys
import os
import re

errors = []

for root, dirs, files in os.walk('skills'):
    if 'SKILL.md' in files:
        file = os.path.join(root, 'SKILL.md')
        try:
            with open(file, 'r') as f:
                content = f.read()
        except Exception as e:
            print(f'Error: {file} cannot be read: {e}')
            errors.append(file)
            continue
        
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            print(f'Error: {file} missing frontmatter')
            errors.append(file)
            continue
        
        try:
            frontmatter = yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f'Error: {file} frontmatter has invalid YAML: {e}')
            errors.append(file)
            continue
        
        if not frontmatter:
            print(f'Error: {file} frontmatter is empty')
            errors.append(file)
            continue
        
        if 'name' not in frontmatter:
            print(f'Error: {file} missing name in frontmatter')
            errors.append(file)
        
        if 'description' not in frontmatter:
            print(f'Error: {file} missing description in frontmatter')
            errors.append(file)
        
        print(f'{file} frontmatter valid')

if errors:
    sys.exit(1)
