#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
   the contents of the web_static folder of your AirBnB
   Clone repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Function generates a .tgz archive from
       the contents of the web_static folder
    """
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions")
    arch_path = "versions/web_static_{}.tgz".format(date)
    content_archive = local('tar cfvz {} web_static'.format(arch_path))
    if content_archive.failed:
        return None
    return arch_path
