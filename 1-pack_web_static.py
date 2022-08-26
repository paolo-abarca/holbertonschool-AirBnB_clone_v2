#!/usr/bin/python3
"""
Fabric script that generates a .tgz file from the contents
of the web_static folder of your AirBnB Clone repository,
using the do_pack function
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz file from the contents
    of the web_static folder of your AirBnB Clone repository"""
    file_result = "versions/web_static_{}.tgz web_static".format(
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -cvzf " + file_result + " ./web_static")
    if result.succeeded:
        return file_result
    return None
