import sys, os
from fabric.api import *
from fabric.contrib import files

FHHOME=os.environ["FHHOME"]

# test.local_hostname
@task
def local_hostname():
    local('hostname')

# test.hostname
@task
def hostname():
    run('hostname')


# test.cat_etc_shadow
@task
def cat_etc_shadow():
    sudo('cat /etc/shadow')

