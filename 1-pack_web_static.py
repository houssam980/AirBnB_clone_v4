#!/usr/bin/python3
"""generate tgz"""


from fabric.api import *
from datetime import datetime
import os

def do_pack():

  try:
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    run("mkdir -p versions", pty=False)
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join("versions", archive_name)
    with lcd("web_static"):
      local("tar -czf ../{}".format(archive_path), ".")
    return archive_path
  except:
    return None

