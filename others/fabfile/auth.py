import sys, glob, os
from fabric.api import *
from fabric.contrib import files

FHHOME=os.environ["FHHOME"]

#------------------------------------------------------------------------
# Linux
#------------------------------------------------------------------------
@task
def pro():
    '''Production # USER=fasthandle KEY'''
    env.user = 'fasthandle'
    env.key_filename = '$FHHOME/key/id_rsa.fasthandle.pro-fasthandle-1'
    #env.password = 'passphrase-for-key'

@task
def stg():
    '''Staging # USER=fasthandle KEY'''
    env.user = 'fasthandle'
    env.key_filename = '$FHHOME/key/id_rsa.fasthandle.stg-fasthandle-1'
    #env.password = 'passphrase-for-key'

@task
def dev():
    '''Develop # USER=fasthandle'''
    env.user = 'fasthandle'
    env.key_filename = '$FHHOME/key/id_rsa.fasthandle.dev-fasthandle-1'
    #env.password = 'passphrase-for-key'

@task
def test1():
    '''USER=fasthandle PASSWORD=fas***s'''
    env.user = 'fasthandle'
    env.password = 'fastpass'

@task
def test2():
    '''USER=user01 PASSWORD=us***01'''
    env.user = 'user01'
    env.password = 'user01'

#------------------------------------------------------------------------
# Windows
#------------------------------------------------------------------------
@task
def winpro():
    '''USER=fasthandle KEY'''
    env.user = 'fasthandle'
    env.key_filename = '$FHHOME/key/id_rsa.fasthandle.pro-fasthandle-1'

@task
def winstg():
    '''USER=fasthandle PASSWORD=fas***s'''
    env.user = 'fasthandle'
    env.password = 'fastpass'

#------------------------------------------------------------------------
# Hardware
#------------------------------------------------------------------------
@task
def ciscopro():
    '''USER=fasthandle PASSWORD=fas***s'''
    env.user = 'fasthandle'
    env.password = 'fastpass'

@task
def junospro():
    '''USER=fasthandle PASSWORD=fas***s'''
    env.user = 'fasthandle'
    env.password = 'fastpass'

@task
def netapppro():
    '''USER=root PASSWORD=fas***s'''
    env.user = 'root'
    env.password = 'fastpass'


