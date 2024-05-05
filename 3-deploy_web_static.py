#!/usr/bin/python3
"""a Fabric script (based on the file 2-do_deploy_web_static.py)
   that creates and distributes an archive to your web servers,
   using the function deploy
"""
from fabric.api import *
from datetime import datetime
from 1 - pack_web_static import do_pack
from 2 - do_deploy_web_static import do_deploy
import os


def deploy():
    """creates and distributes an archive to your web servers"""
    arch_path = do_pack()
    if arch_path is None:
        return False
    return do_deploy(arch_path)
