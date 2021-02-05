#!/usr/bin/python3
"""-- script that takes 2 arguments --"""
import sys
import os.path
import markdown

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)
elif os.path.exists(sys.argv[1]) is False:
    sys.stderr.write("Missing " + sys.argv[1])
    sys.exit(1)
else:
    with open(sys.argv[1], 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(sys.argv[2], 'w') as f:
        f.write(html)
    sys.exit(0)
