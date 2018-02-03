import sys, os
from fabric.api import *
from fabric.contrib import files

FHHOME=os.environ["FHHOME"]

#----------------------------------------------------------------------
# Installing Apache httpd
#----------------------------------------------------------------------
# httpd.install_yum
@task
def install_yum():
    sudo("rpm -q httpd        > /dev/null 2>&1 || yum -y install httpd")

# httpd.install_apt
@task
def install_apt():
    sudo("dpkg -l |grep apache    > /dev/null 2>&1 || apt install apahce2")



#----------------------------------------------------------------------
# Check Files
#----------------------------------------------------------------------
#RHEL/CentOS
# httpd.check_files_etc_httpd
@task
def check_files_etc_httpd():
    '''tree -Dpuga  /etc/httpd #centos'''
    run("tree -Dpuga  /etc/httpd")

#Debian/Ubuntu
# httpd.check_files_etc_apache2
@task
def check_files_etc_apache2():
    '''tree -Dpuga  /etc/apache2  #ubuntu'''
    run("tree -Dpuga  /etc/apache2")


#----------------------------------------------------------------------
# Check Modules
#----------------------------------------------------------------------
#RHEL/CentOS
@task
def check_modules_pkg():
    '''/usr/sbin/httpd -M  # Package'''
    run("/usr/sbin/httpd -M")

@task
def check_modules_src():
    '''/usr/local/apache2/bin/httpd -M  # SRC'''
    run("/usr/local/apache2/bin/httpd -M")


#----------------------------------------------------------------------
# Check Server-Status
#----------------------------------------------------------------------
@task
def check_server_satus():
    '''curl http://localhost/server-status?auto'''
    run("curl  http://localhost/server-status?auto")


#----------------------------------------------------------------------
# Check Header
#----------------------------------------------------------------------
@task
def check_header():
    '''curl -I http://localhost/'''
    run("curl -I http://localhost/")



