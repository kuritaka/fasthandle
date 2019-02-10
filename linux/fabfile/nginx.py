import sys, os
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

FHLINUX=os.environ["FHLINUX"]

#----------------------------------------------------------------------
# Installing Nginx
#----------------------------------------------------------------------
# nginx.install_yum
@task
def install_yum():
    sudo("rpm -q nginx        > /dev/null 2>&1 || yum -y install nginx")

# nginx.install_apt
@task
def install_apt():
    sudo("dpkg -l |grep nginx > /dev/null 2>&1 || apt update && apt install -y nginx")



#----------------------------------------------------------------------
# Check Configuration Files
#----------------------------------------------------------------------
# nginx.check_files_etc_nginx
@task
def check_files_etc_nginx():
    '''tree -Dpuga  /etc/nginx'''
    run("tree -Dpuga  /etc/nginx")


#----------------------------------------------------------------------
# Check Header
#----------------------------------------------------------------------
@task
def check_header():
    '''curl -I http://localhost/'''
    run("curl -I http://localhost/")



