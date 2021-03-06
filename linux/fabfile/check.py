import sys, os
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

FHLINUX=os.environ["FHLINUX"]


#------------------------------------------------------------------
# check.ntpsync
#------------------------------------------------------------------
@task 
def ntpsync():
    sudo("which ntpq > /dev/null 2>&1 && ntpq -p")
    sudo("which chronyc > /dev/null 2>&1 && chronyc sources -v")


#------------------------------------------------------------------
# check.nmap
#     fab auth.pro check.nmap:22,x.x.x.x
#------------------------------------------------------------------
@task
def nmap(port, remote):
    """ope.nmap:22,x.x.x.x"""
    run("nmap -Pn -sT -p %s %s " % (port, remote))

#------------------------------------------------------------------
# check_ssh_hostname:localuser,key,remoteuser,remotehost
#------------------------------------------------------------------
@task
def check_ssh_hostname(localuser, key, remoteuser, remotehost):
    """ check_ssh_hostname:localuser,key,remoteuser,remotehost"""
    sudo ('su - %s -c "ssh -i %s %s@%s hostname"' % (localuser, key, remoteuser, remotehost))



#===============================================================================
# Check OS Status
#===============================================================================
#------------------------------------------------------------------
# check.reboot_check
#------------------------------------------------------------------
@task
def reboot_check():
    """ use  %s/scripts/check_reboot.sh """
    date = datetime.now().strftime('%Y%m%d_%H%M')
    outfile = "check_reboot.%s"  % (date)
 
    run("test -d scripts || mkdir scripts")
    put("%s/scripts/check_reboot.sh" % FHLINUX, scripts/check_reboot.sh, mode=0755)
    sudo("scripts/check_reboot.sh 1>output/%s  2>/dev/null"   % (outfile))

#------------------------------------------------------------------
# check.reboot_diff
#------------------------------------------------------------------
@task
def reboot_diff():
    run("ls -tr1 output/check_reboot.2* |tail -n 5")
    file1=run("ls -tr1 output/check_reboot.2* |tail -n 2 |head -n 1")
    file2=run("ls -tr1 output/check_reboot.2* |tail -n 1")
    local("sdiff -s -w 150 %s %s" % (file1, file2))
    run("sdiff -s -w 150 output/%s output/%s" % (file1, file2))

#------------------------------------------------------------------
# check.ping_gw
#------------------------------------------------------------------
@task
def ping_gw():
    """ use  %s/scripts/check_ping_gw.sh """
    run("test -d scripts || mkdir scripts")
    put("%s/scripts/check_ping_gw.sh" % FHLINUX, "scripts/check_ping_gw.sh", mode=0755)
    run("scripts/check_ping_gwt.sh")



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
 


