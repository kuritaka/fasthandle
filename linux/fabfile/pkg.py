import sys, os
from fabric.api import *
from fabric.contrib import files

FHHOME=os.environ["FHHOME"]

#===============================================================================
#Check Commands
#===============================================================================
@task
def check_cmd():
    put("%s/scripts/check_cmd.sh" % FHHOME, "scripts/check_cmd.sh", mode=0755)
    sudo("scripts/check_cmd.sh")


#===============================================================================
#Service Enable/Disable
#===============================================================================
#-------------------------------------------------------------------------------
# CentOS7
# check.systemctl_service_enable_disable
#-------------------------------------------------------------------------------
@task
def systemctl_service_enable_disable():
    sudo('systemctl list-unit-files -t service --no-pager |egrep "enable|disable" |sort -k 3')


#===============================================================================
# Installing Package
#===============================================================================
#----------------------------------------------------------------------
# CentOS7
#----------------------------------------------------------------------
#pkg.install_rpm_centos7
@task
def install_rpm_centos7():
    put("%s/scripts/rpm.sh" % FHHOME, "scripts/rpm.sh", mode=0755)
    sudo("scripts/rpm.sh centos7", pty=False)

#----------------------------------------------------------------------
#CentOS6
#----------------------------------------------------------------------
#pkg.install_rpm_centos6


#----------------------------------------------------------------------
#Ubuntu16
#----------------------------------------------------------------------
#pkg.install_dpkg_ubuntu16




