#!/usr/bin/python3
"""Adding a Fabric script (based on the 2-do_deploy_web_static.py
file) that creates and deploys a file to your web servers,
using the deploy function"""


from fabric.operations import local, run, put
from datetime import datetime
from os.path import getsize
from fabric.api import env
import os
env.hosts = ['54.147.136.182', '54.163.40.93']


def do_pack():
    """generates a .tgz file from the contents
    of the web_static folder of your AirBnB Clone repository"""
    local("mkdir -p versions")
    date = datetime.utcnow()
    format_date = "%Y%m%d%H%M%S"
    conv = date.strftime(format_date)
    path = "versions/web_static_{}.tgz".format(conv)
    localhost = local("tar -cvzf {} web_static".format(path))

    if localhost.succeeded:
        print("web_static packed: {} -> {}Bytes".format(path, getsize(path)))
        return path
    elif localhost.failed:
        return None


def do_deploy(archive_path):
    """generates a .tgz file from the contents
    of the web_static folder of your AirBnB Clone repository"""
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        filename = archive.split('.')[0]
        path = '/data/web_static/releases/'
        put(archive_path, "/tmp/{}".format(archive))
        run('mkdir -p {}{}/'.format(path, filename))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive, path, filename))
        run('rm /tmp/{}'.format(archive))
        run('mv {}{}/web_static/* {}{}/'.format(path, filename,
                                                path, filename))
        run('rm -rf {}{}/web_static'.format(path, filename))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, filename))
        print('New version deployed!')
        return True
    else:
        return False


def deploy():
    """deploys a file to your web servers, using the do_deploy function"""
    callFunction = do_pack()

    if callFunction is None:
        return False
    return do_deploy(callFunction)
