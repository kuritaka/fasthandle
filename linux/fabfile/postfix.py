import sys, os
from fabric.api import *
from fabric.contrib import files

FHLINUX=os.environ["FHLINUX"]

#----------------------------------------------------------------------
# Installing Postfix
#----------------------------------------------------------------------
# postfix.install_yum
@task
def install_yum():
    sudo("rpm -q postfix        > /dev/null 2>&1 || yum -y install postfix")


