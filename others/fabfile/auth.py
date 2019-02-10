import sys, glob, os
from fabric.api import *
from fabric.contrib import files

FHOTHERS=os.environ["FHOTHERS"]


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


