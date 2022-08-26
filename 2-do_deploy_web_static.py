#!/usr/bin/python3
"""Fabric script (based on the 1-pack_web_static.py file)
that deploys a file to your web servers, using the do_deploy function:"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.147.136.182', '54.163.40.93']


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


def do_deploy(archive_path):
    """deploys a file to your web servers, using the do_deploy function"""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp/')
    file_result = archive_path.split("/")
    file_res = file_result[1].split(".")
    run('mkdir -p /data/web_static/releases/{}/'.format(file_res[0]))
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
        .format(file_res[0], file_res[0]))
    run('rm /tmp/{}.tgz'.format(file_res[0]))
    run('mv /data/web_static/releases/{}/web_static/* '.format(file_res[0]) +
        '/data/web_static/releases/{}/'.format(file_res[0]))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(file_res[0]))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(file_res[0]))
    print('New version deployed!')
    return True
