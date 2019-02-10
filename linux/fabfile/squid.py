import sys, os
from fabric.api import *
from fabric.contrib import files

FHHOME=os.environ["FHHOME"]

#----------------------------------------------------------------------
# Installing Squid
#----------------------------------------------------------------------
# squid.install_yum
@task
def install_yum():
    sudo("rpm -q squid        > /dev/null 2>&1 || yum -y install squid")

#----------------------------------------------------------------------
# Service
#----------------------------------------------------------------------
# squid.systemctl_restart
@task
def systemctl_restart():
    run("ps aux |grep squid")
    sudo("systemctl stauts squid")
    sudo("systemctl restart squid")
    sudo("systemctl stauts squid")
    run("ps aux |grep squid")

#----------------------------------------------------------------------
# Configuration
#----------------------------------------------------------------------
# squid.change_squidconf:test-server-01
@task
def change_squidconf(host):
    today = datetime.now().strftime('%Y%m%d')
    sudo("cp -f /etc/squid/squid.conf /etc/squid/squid.conf.`date -d '1day ago' +%Y%m%d`")
    put("%s/conf/squid/squid.conf.%s" % (FHHOME, host), "/tmp/squid.conf.%s" % date)
    sudo("mv /tmp/squid.conf.%s /etc/sysctl.conf" % date)


