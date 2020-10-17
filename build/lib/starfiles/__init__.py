"""
Starfiles

Simplify starfiles, if it wasn't simple enough already
"""

__version__ = "1.0.0"
__author__ = 'DwifteJB'
__credits__ = 'Quixthe2nd'

import json
import requests
import re
import os
import time
import sys
  
def profile(p):
  global profile
  p = profile

def upload(filename):
  try:
    files = {
      'upload': (f'{filename}', open(f'{filename}', 'rb')),
    }
  except FileNotFoundError as e:
    print(f"[ ERROR ] : {e}")
    return f"[ ERROR ] : {e}"
  if profile is not None:
    response = requests.post('https://starfiles.co/api/upload/upload_file?profile={profile}', files=files)
  else:
    response = requests.post('https://starfiles.co/api/upload/upload_file', files=files)
    pass
  api = json.loads(response.text)
  file = api['file']
  link = f"https://starfiles.co/api/direct/{file}"
  size = round(int(os.path.getsize(filename)) / 1000000, 2)
  name = re.sub(r'^.*?/', '', filename)
  print("\n")
  print(f"------------ Uploaded {name} ------------")
  print(f"Name: {name}")
  print(f"Size: {size}mb")
  print(f"Download Link:\nRegular: https://starfiles.co/file/{file}\nDirect: {link}")
  if re.search("ipa$", filename):
    print(f"Plist: https://starfiles.co/api/installipa/{file}\nInstall URL: itms-services://?action=download-manifest&url=https://starfiles.co/api/installipa/{file}")
  return link