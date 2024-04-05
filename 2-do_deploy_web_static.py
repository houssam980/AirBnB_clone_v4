#!/usr/bin/python3


from fabric.api import *
import os

env.hosts = ['100.26.49.131', '54.197.89.103'] 

def do_deploy(archive_path):
    """Distributes an archive to web servers."""

    if not os.path.isfile(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        release_name = archive_name.split('.')[0]

        put(archive_path, '/tmp/{}'.format(archive_name))

        with cd('/data/web_static/releases'):
            run('mkdir -p {}'.format(release_name))  # Ensure directory exists
            run('tar -xzf /tmp/{} -C {}'.format(archive_name, release_name))

        run('rm /tmp/{}'.format(archive_name))
        run('mv {}/web_static/* {}/'.format(release_name, release_name))
        run('rm -rf {}/web_static'.format(release_name))

        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/{} /data/web_static/current'.format(release_name))

        return True

    except Exception as e:
        print("Error during deployment:", e)
        return False

