import sys, os
from fabric.api import *
from fabric.contrib import files

FHHOME=os.environ["FHHOME"]

#----------------------------------------------------------------------
# Installing TFTP
#----------------------------------------------------------------------
# squid.install_rpm
@task
def install_rpm():
    '''yum install tftp tftp-server xinetd '''
    sudo("rpm -q tftp         > /dev/null 2>&1 || yum -y install tftp")
    sudo("rpm -q tftp-server  > /dev/null 2>&1 || yum -y install tftp-server")
    sudo("rpm -q xinetd       > /dev/null 2>&1 || yum -y install xinetd")

#----------------------------------------------------------------------
# Configuration
#----------------------------------------------------------------------
# tftp.conf
@task
def conf():
    sudo("cp -p /etc/xinetd.d/tftp ~/tftp.`date -d '1day ago' +%Y%m%d`")

    #disable                 = no
    sudo("sed -i '/disable/ s/yes/no/' /etc/xinetd.d/tftp")
    #sed -i "s/\(disable[\t]*= *\).*/\1no/" /etc/xinetd.d/tftp

    #server_args             = -c -u root -s /var/lib/tftpboot
    sudo('sed -i "s/\(server_args[\t]*= *\).*/\1-c -u root -s \/home\/fasthandle\/fhhome\/tftp/" /etc/xinetd.d/tftp')
    #sed -i "s/\(server_args[\t]*= *\).*/\1-s \/opt\/Tftproot -c/" /etc/xinetd.d/tft

    sudo("test -d /home/fasthandle/fhhome/tftp || mkdir /home/fasthandle/fhhome/tftp")
    sudo("chmod 777 /home/fasthandle/fhhome/tftp")

#----------------------------------------------------------------------
# Service
#----------------------------------------------------------------------
