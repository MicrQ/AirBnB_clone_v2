#!/usr/bin/python3
""" a python fabric script that deletes all old version arcives
    excluding the most recent {number} files.
    where {number} is files to be kept.
"""
import os
from fabric import api

api.env.hosts = ['18.204.8.72', '54.160.83.215']


def do_clean(number=0):
    """ a function that deletes unnecessary archives """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with api.lcd("versions"):
        [api.local("rm ./{}".format(a)) for a in archives]

    with api.cd("/data/web_static/releases"):
        archives = api.run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [api.run("rm -rf ./{}".format(a)) for a in archives]
