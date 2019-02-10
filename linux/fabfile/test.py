import sys, os
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

FHLINUX=os.environ["FHLINUX"]

# test.local_hostname
@task
def local_hostname():
    local('hostname')

# test.hostname
@task
def hostname():
    run('hostname')


# test.sudo
@task
def sudo():
    """ sudo cat /etc/shadow """
    sudo('cat /etc/shadow')


# test.arg1:hostname
@task
def arg1(cmd):
    """ fab test.arg1:hostname """
    run('%s' % cmd)


# test.arg2:hostname,whoami
@task
def arg2(cmd1, cmd2):
    """ fab test.arg2:hostname,whoami """
    run('%s' % cmd1)
    run('%s' % cmd2)
    run('%s ; %s' % (cmd1, cmd2) )


# test.put
@task
def put():
    date = datetime.now().strftime('%Y%m%d_%H%M')
    local('hostname > /tmp/test.%s' % date)
    put('/tmp/test.%s' % date, '/tmp/test.%s' % date)
    run('ls -lh /tmp/test.%s' % date)
    run('cat /tmp/test.%s' % date)

# test.get
@task
def get():
    date = datetime.now().strftime('%Y%m%d_%H%M')
    run('hostname > /tmp/test.%s' % date)
    get('/tmp/test.%s' % date, '/tmp/test.%s' % date)
    local('ls -lh /tmp/test.%s' % date)
    local('cat /tmp/test.%s' % date)

