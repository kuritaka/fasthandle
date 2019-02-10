import sys, os
from fabric.api import *
from fabric.contrib import files


FHLINUX=os.environ["FHLINUX"]

#----------------------------------------------------------------------
# Check PHP
#----------------------------------------------------------------------
# php.check_php_rpm
@task
def check_php_rpm():
    '''rpm -qa |grep php'''
    sudo("rpm -qa |grep  php")



#----------------------------------------------------------------------
# Installing PHP
#----------------------------------------------------------------------
# php.install_yum
@task
def install_yum():
    sudo("rpm -q php            > /dev/null 2>&1 || yum -y install php")
    sudo("rpm -q php-mbstrig    > /dev/null 2>&1 || yum -y install php-mbstrig") 

# php.install_phpfpm_yum
@task
def install_phpfpm_yum():
    sudo("yum -y install php-cli php-mbstring php-fpm")


