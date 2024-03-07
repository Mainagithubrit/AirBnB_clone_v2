#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the
contents of the web_static folder"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """Defines a function that must return the archive path"""

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
