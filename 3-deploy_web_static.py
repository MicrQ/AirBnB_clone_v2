#!/usr/bin/python3
""" a fabric script that creates an archive and deployes it """


from os.path import exists, isdir, isfile
from datetime import datetime
from fabric.api import *


env.hosts = ['18.204.8.72', '54.160.83.215']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    file = "versions/web_static_{}.tgz".format(date)
    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if sudo("mkdir -p /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return False
    if sudo("rm /tmp/{}".format(file)).failed is True:
        return False
    if sudo("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/current").failed is True:
        return False
    if sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
