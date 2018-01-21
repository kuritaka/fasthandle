import sys, os
from fabric.api import *
from fabric.contrib import files
from fabric.contrib.files import sed, append, contains

FHHOME=os.environ["FHHOME"]



#-------------------------------------------------------------------------------
#set.centos7_init
#-------------------------------------------------------------------------------
@task
def centos7_init():
    etc_sysctlconf()
    etc_security_limitsconf()
    # CentOS7
    lang_jajputf8()
    etc_selinux_config()

#-------------------------------------------------------------------------------
#set.centos6_init
#-------------------------------------------------------------------------------
@task
def centos6_init():
    etc_sysctlconf()
    etc_security_limitsconf()
    # CentOS6
    etc_sysconfig_selinux()

#-------------------------------------------------------------------------------
#set.ubuntu16_init
#-------------------------------------------------------------------------------
@task
def ubuntu16_init():
    etc_sysctlconf()
    etc_security_limitsconf()


#===============================================================================
# /etc
#===============================================================================
# set.etc_sysctlconf
@task
def etc_sysctlconf():
    '''/etc/sysctl.conf'''
    date = datetime.now().strftime('%Y%m%d_%H%M')
    sudo("cp -f /etc/sysctl.conf /etc/sysctl.conf.`date -d '1day ago' +%Y%m%d`")
    put("%s/conf/os/sysctl.conf" % FHHOME, "/tmp/sysctl.conf.%s" % date)
    sudo("mv /tmp/sysctl.conf.%s /etc/sysctl.conf" % date)

# set.etc_security_limitsconf
@task
def etc_security_limitsconf():
    '''/etc/security/limits.conf'''
    date = datetime.now().strftime('%Y%m%d_%H%M')
    sudo("cp -f /etc/security/limits.conf /etc/security/limits.conf.`date -d '1day ago' +%Y%m%d`")
    put("%s/conf/os/limits.conf" % FHHOME, "/tmp/limits.conf.%s" % date)
    sudo("mv /tmp/limits.conf.%s /etc/security/limits.conf" % date)
    #
    sudo("rm -f /etc/security/limits.d/*-nproc.conf")


# set.etc_selinux_config  CentOS7
@task
def etc_selinux_config():
    '''/etc/selinux/config CentOS7'''
    date = datetime.now().strftime('%Y%m%d_%H%M')
    sudo("cp -f /etc/selinux/config /etc/selinux/config.`date -d '1day ago' +%Y%m%d`")
    put("%s/conf/os/selinux_config.conf"  % FHHOME, "/tmp/config.%s" % date)
    sudo("mv /tmp/config.%s /etc/selinux/config" % date)

# etc_sysconfig_selinux CentOS6
@task
def etc_sysconfig_selinux():
    '''/etc/sysconfig/selinux CentOS6'''
    date = datetime.now().strftime('%Y%m%d_%H%M')
    sudo("cp -f /etc/sysconfig/selinux  /etc/sysconfig/selinux.`date -d '1day ago' +%Y%m%d`")
    put("%s/conf/os/selinux_config.conf" % FHHOME, "/tmp/selinux.%s" % date)
    sudo("mv /tmp/selinux.%s /etc/sysconfig/selinux" % date)


#===============================================================================
# Command Configuration
#===============================================================================
#--------------------------------------------------
# LANG
#--------------------------------------------------
# set.lang_ja_jputf8  #CentOS7
@task
def lang_jajputf8():
    '''LANG=ja_JP.utf8 #CentOS7'''
    sudo("localectl set-locale LANG=ja_JP.utf8")

    #/etc/profile
    sudo("cp -f /etc/profile  /etc/profile.`date -d '1day ago' +%Y%m%d`")
    if not contains('/etc/profile', 'locale.conf'):
        append('/etc/profile', '\n#LANG\ntest -f /etc/locale.conf && . /etc/locale.conf\nexport LANG', use_sudo=True)


#===============================================================================
#Service Enable/Disable
#===============================================================================
#-------------------------------------------------------------------------------
# CentOS7
#-------------------------------------------------------------------------------
# set.service_systemctl
@task
def service_systemctl():
    #enable
    sudo("systemctl enable sysstat.service")
    sudo("systemctl enable snmpd.service")
  
    #disable
    sudo("systemctl disable firewalld.service")
    sudo("systemctl disable NetworkManager.service")

#-------------------------------------------------------------------------------
# CentOS6
#-------------------------------------------------------------------------------



