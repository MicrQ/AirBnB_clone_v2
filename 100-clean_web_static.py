#!/usr/bin/python3
""" a python fabric script that deletes all old version arcives
    excluding the most recent {number} files.
    where {number} is files to be kept.
"""
from fabric import api
from os import listdir


api.env.hosts = ['18.204.8.72', '54.160.83.215']


def do_clean(number=0):
    """ a function that deletes deletes old version archives """
    if number == 0:
        number = 1
    archives = sorted(listdir('versions'), reverse=True)

    with api.lcd('versions'):
        for i in range(int(number), len(archives)):
            api.local('rm {}'.format(archives[i]))

    with api.cd('/data/web_static/releases'):
        archives = sorted(api.run('ls').split(), reverse=True)

    for i in range(int(number), len(archives)):
        api.run('rm -rf {}'.format(archives[i]))
