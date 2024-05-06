#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
   an rchive to your web servers, using the function `do_deploy`
"""

from fabric.api import *
from fabric.operations import run, put
import os

env.hosts = ['18.210.20.218', '100.25.148.64']

def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    try:
        if not os.path.isfile(archive_path):
            return False
        arch_name = os.path.basename(archive_path)
        base_name, extendion = os.path.splitext(arch_name)
        rel = "/data/web_static/releases"
        cur = "/data/web_static/current"
        run("sudo mkdir -p {}/{}".format(rel, base_name))
        run("sudo tar xvf /tmp/{} -C {}/{}".format(arch_name, rel, base_name))
        run("sudo rm /tmp/{}".format(arch_name))
        run("sudo rm -rf {}".format(cur))
        run("sudo mv {}/{}/web_static/* {}/{}"
            .format(rel, base_name, rel, base_name))
        run("sudo rm -rf {}/{}/web_static".format(rel, base_name))
        run("sudo ln -sf {}/{} {}".format(rel, base_name, cur))
        return True
    except Exception:
        return False
