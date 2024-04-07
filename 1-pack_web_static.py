#!/usr/bin/python3
""" """

import os
from fabric import api
from datetime import datetime


def do_pack():
    """ a function that create .tgz of
        web_static in the folder named versions
    """
    if not os.path.exists('versions'):
        os.mkdir('versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    api.local('tar -czvf versions/web_static_{}.tgz web_static'.format(date))
