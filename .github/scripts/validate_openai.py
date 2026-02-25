#!/usr/bin/env python3
import yaml
import sys
import os

required_fields = ['interface']
interface_fields = ['display_name', 'short_description', 'default_prompt']

errors = []

for root, dirs, files in os.walk('skills'):
    if 'openai.yaml' in files:
        file = os.path.join(root, 'openai.yaml')
        try:
            with open(file) as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f'Error: {file} has invalid YAML: {e}')
            errors.append(file)
            continue
        
        if not data:
            print(f'Error: {file} is empty')
            errors.append(file)
            continue
        
        for field in required_fields:
            if field not in data:
                print(f'Error: {file} missing required field: {field}')
                errors.append(file)
                continue
        
        if 'interface' in data:
            for field in interface_fields:
                if field not in data['interface']:
                    print(f'Error: {file} interface missing required field: {field}')
                    errors.append(file)
        
        print(f'{file} structure valid')

if errors:
    sys.exit(1)
