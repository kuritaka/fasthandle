import sys, os
from fabric.api import *
from fabric.contrib import files

FHWIN=os.environ["FHWIN"]


#------------------------------------------------------------------
# wincheck.ipconfig_all
#------------------------------------------------------------------
@task
def chcp437():
    """chcp 437 # Change LANG To English"""
    run("chcp 437", shell=False, pty=False)


#================================================================================
# Network
#================================================================================
#------------------------------------------------------------------
# wincheck.ipconfig_all
#------------------------------------------------------------------
@task
def ipconfig_all():
    run("ipconfig /all", shell=False, pty=False)

#------------------------------------------------------------------
# wincheck.netstat_rn
#------------------------------------------------------------------
@task
def netstat_rn():
    run("netstat -rn", shell=False, pty=False)


#================================================================================
# User
#================================================================================
#------------------------------------------------------------------
# wincheck.net_user
#------------------------------------------------------------------
@task
def net_user():
    """ user list"""
    run("net user", shell=False, pty=False)

#------------------------------------------------------------------
# wincheck.net_user:
#------------------------------------------------------------------
@task
def net_user(user):
    run("net user %s" % user, shell=False, pty=False)

#------------------------------------------------------------------
# wincheck.net_user_active:
#------------------------------------------------------------------
@task
def net_user_active(user):
    """ make user active from disable"""
    run("net user %s /active" % user, shell=False, pty=False)


#------------------------------------------------------------------
# wincheck.net_localgroup_administrators
#------------------------------------------------------------------
@task
def net_localgroup_administrators():
    run("net localgroup administrators", shell=False, pty=False)

#------------------------------------------------------------------
# wincheck.net_localgroup_users
#------------------------------------------------------------------
@task
def net_localgroup_users():
    run("net localgroup users", shell=False, pty=False)



#================================================================================
# etc
#================================================================================
#------------------------------------------------------------------
# wincheck.systeminfo
#------------------------------------------------------------------
@task
def systeminfo():
    run("systeminfo", shell=False, pty=False)

#------------------------------------------------------------------
# wincheck.powershell_version
#------------------------------------------------------------------
@task
def powershell_version():
    run("PowerShell.exe -Command $PSVersionTable", shell=False, pty=False)

