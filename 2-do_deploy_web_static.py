#!/usr/bin/python3
""" a program that distributes a archived file to my web servers """
from fabric import api
from os import path


api.env.hosts = ['18.204.8.72', '54.160.83.215']


def do_deploy(archive_path):
    """ a function that distributes the archive """
    if not path.exists(archive_path):
        return False
    try:
        api.put(archive_path, '/tmp/', True)
        filename = archive_path.split('/')[-1]

        api.sudo('mkdir -p /data/web_static/releases/{}'.format(filename[:-4]))
        api.sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            filename, filename[:-4]
        ))
        api.sudo('rm /tmp/{}'.format(filename))
        api.sudo('rm -fr /data/web_static/current')
        api.sudo('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(
                    filename[:-4], filename[:-4]))
        api.sudo('rm -fr /data/web_static/releases/{}/web_static'.format(
            filename[:-4]))
        api.sudo('ln -fs /data/web_static/releases/{} \
                /data/web_static/current'.format(filename[:-4]))
        return True
    except:
        return False
