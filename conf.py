import os, sys
sys.path.insert(0, os.path.abspath('.'))
extensions = ['showraw']

master_doc = 'index'
# No error code 10 with:
# html_use_smartypants = False
# Error code 10 for sphinx >=1.6 with
html_use_smartypants = True
