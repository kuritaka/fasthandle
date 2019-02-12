import sys, os
from fabric.api import *
from fabric.contrib import files

FHWIN=os.environ["FHWIN"]


#------------------------------------------------------------------
# winope.cmd
#------------------------------------------------------------------
@task
def cmd(cmd):
    """winope.cmd:hostname"""
    run("%s" % cmd, shell=False, pty=False)

#------------------------------------------------------------------
# winope.powershell:'$PSVersionTable'
#------------------------------------------------------------------
@task
def powershell(cmd):
    """winope.powershell:'$PSVersionTable' """
    run("PowerShell.exe -Command %s" % cmd, shell=False, pty=False)


#------------------------------------------------------------------
# winope.put:local, remote
#------------------------------------------------------------------
@task
def put(local, remote):
    """ winope.put:local,remote  # /tmp/test.txt C:\\tmp\\ """
    put("%s" % local, "%s" % remote)

#------------------------------------------------------------------
# winope.get:remote, local
#------------------------------------------------------------------
@task
def get(remote, local):
    """ winope.get:remote, local # C:\\tmp\\test.txt , /tmp/ """
    get("%s" % remote, "%s" % local)

