#_*_coding: utf-8 _*_
import sys
import base64
name = sys.argv[1]
print(base64.b64encode(name.encode('utf-8')))
