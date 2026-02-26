#!/usr/bin/env python3
import sys
import re
import os
import glob

broken = []
for md_file in glob.glob("skills/**/*.md", recursive=True):
    if not os.path.isfile(md_file):
        continue
    with open(md_file, "r") as f:
        content = f.read()
    
    links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
    for text, url in links:
        if url.startswith('http') or url.startswith('#'):
            continue
        full_path = os.path.join(os.path.dirname(md_file), url)
        if not os.path.exists(full_path):
            broken.append(f'{md_file}: {url}')

if broken:
    print('Broken links found:')
    for b in broken:
        print(f'  {b}')
    sys.exit(1)
print('All markdown links valid')
