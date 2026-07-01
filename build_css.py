#!/usr/bin/env python3
"""Minify CSS files for production."""
import re
from pathlib import Path

def minify_css(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Remove unnecessary whitespace
    css = re.sub(r'\s+', ' ', css)
    # Remove spaces around special characters
    css = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css)
    # Remove trailing semicolons before closing braces
    css = re.sub(r';(?=\})', '', css)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(css)
    
    return len(css)

if __name__ == '__main__':
    src = Path('apps/static/css/style.src.css')
    out = Path('apps/static/css/style.css')
    
    if src.exists():
        size = minify_css(src, out)
        print(f"✓ Built: {out} ({size} bytes)")
    else:
        print(f"✗ Source file not found: {src}")
