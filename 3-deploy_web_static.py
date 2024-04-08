#!/usr/bin/python3
""" a fabric script that creates an archive and deployes it """


import os
from datetime import datetime
from fabric import api


api.env.hosts = ['18.204.8.72', '54.160.83.215']


def do_pack():
    """ a function that create .tgz of
        web_static in the folder named versions
    """
    api.local('sudo mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    result = api.local('sudo tar -czvf versions/web_static_{}.tgz \
                       web_static'.format(date))
    if result.succeeded:
        return "versions/web_static_{}.tgz".format(date)
    return None


def do_deploy(archive_path):
    """ a function that distributes the archive """
    if os.path.exists(archive_path) is False:
        return False
    try:
        api.put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1]

        api.run('mkdir -p /data/web_static/releases/{}'.format(filename[:-4]))
        api.run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            filename, filename[:-4]
        ))
        api.run('rm /tmp/{}'.format(filename))
        api.run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(
                    filename[:-4], filename[:-4]))
        api.sudo('rm -fr /data/web_static/releases/{}/web_static'.format(
            filename[:-4]))
        api.run('rm -fr /data/web_static/current')
        api.sudo('ln -s /data/web_static/releases/{}/ \
                /data/web_static/current'.format(filename[:-4]))
        return True
    except:
        return False


def deploy():
    """ a function that initiates the deployment"""
    pack = do_pack()
    if os.path.exists(pack):
        return do_deploy(pack)
    return False
