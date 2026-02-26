#!/usr/bin/env python3
import yaml
import sys
import os

errors = []

for root, dirs, files in os.walk('skills'):
    if 'agents' not in dirs:
        continue
    
    agents_dir = os.path.join(root, 'agents')
    if not os.path.isdir(agents_dir):
        continue
    
    for file in os.listdir(agents_dir):
        if not file.endswith(('.yaml', '.yml')):
            continue
        
        file_path = os.path.join(agents_dir, file)
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f'Error: {file_path} invalid YAML: {e}')
            errors.append(file_path)
            continue
        
        if not data:
            print(f'Error: {file_path} is empty')
            errors.append(file_path)
            continue
        
        interface = data.get('interface', {})
        required_fields = ['display_name', 'short_description', 'default_prompt']
        missing = [f for f in required_fields if f not in interface]
        
        if missing:
            print(f'Error: {file_path} missing interface fields: {missing}')
            errors.append(file_path)
        else:
            print(f'{file_path} valid')

if errors:
    sys.exit(1)
