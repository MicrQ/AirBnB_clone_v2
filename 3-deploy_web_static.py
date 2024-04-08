#!/usr/bin/python3
""" a fabric script that creates an archive and deployes it """


from os.path import exists
from datetime import datetime
from fabric.api import *


env.hosts = ['18.204.8.72', '54.160.83.215']


def do_pack():
    """ a function that create .tgz of
        web_static in the folder named versions
    """
    local('sudo mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local('sudo tar -cvzf {} web_static'.format(filename))
    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """ a function that distributes the archive """
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_ext = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    try:
        put(archive_path, '/tmp/')

        run('mkdir -p {}/'.format(no_ext))
        run('tar -xzf /tmp/{} -C {}'.format(filename, no_ext))
        run('rm -rf /tmp/{}'.format(filename))
        run('mv {}/web_static/* {}/'.format(no_ext, no_ext))
        run('rm -fr {}/web_static'.format(no_ext))
        run('rm -fr /data/web_static/current')

        run('ln -s {}/ /data/web_static/current'.format(no_ext))
        return True
    except:
        return False


def deploy():
    """ a function that initiates the deployment"""
    pack = do_pack()
    if exists(pack) is False:
        return False
    return do_deploy(pack)
