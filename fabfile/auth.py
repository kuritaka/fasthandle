import sys, glob, os
from fabric.api import *
from fabric.contrib import files

@task
def pro():
    '''production env'''
    env.user = 'fasthandle'
    env.key_filename = '$FHHOME/key/id_rsa.fasthandle.pro-fasthandle-1'
    #env.password = 'passphrase-for-key'

@task
def stg():
    '''staging env'''
    env.user = 'fasthandle'
    env.key_filename = '$FHHOME/key/id_rsa.fasthandle.stg-fasthandle-1'
    #env.password = 'passphrase-for-key'

@task
def dev():
    '''develop env'''
    env.user = 'fasthandle'
    env.key_filename = '$FHHOME/key/id_rsa.fasthandle.dev-fasthandle-1'
    #env.password = 'passphrase-for-key'

@task
def test1():
    env.user = 'fasthandle'
    env.password = 'fastpass'

@task
def test2():
    env.user = 'user01'
    env.password = 'user01'

