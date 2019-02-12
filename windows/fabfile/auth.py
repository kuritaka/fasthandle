import sys, glob, os
from fabric.api import *
from fabric.contrib import files

FHWIN=os.environ["FHWIN"]

#------------------------------------------------------------------------
# Windows
#------------------------------------------------------------------------
@task
def winpro():
    '''USER=fasthandle KEY'''
    env.user = 'fasthandle'
    env.key_filename = '$FHWIN/key/id_rsa.fasthandle.pro-fasthandle-1'

@task
def winstg():
    '''USER=fasthandle PASSWORD=fas***s'''
    env.user = 'fasthandle'
    env.password = 'fastpass'



