#!/bin/bash
# rpm-centos.sh 
#
# How to use
#     rpm.sh centos7
#     rpm.sh centos6

if [ -z $1 ]; then
    echo "Error:  argument is null"
    exit 1
fi

centos7() {
    rpm -q epel-release      > /dev/null 2>&1 || yum -y install epel-release
    rpm -q bash-completion   > /dev/null 2>&1 || yum -y install bash-completion
    rpm -q traceroute        > /dev/null 2>&1 || yum -y install traceroute
    rpm -q vim-enhanced      > /dev/null 2>&1 || yum -y install vim-enhanced
    rpm -q tree              > /dev/null 2>&1 || yum -y install tree
    rpm -q telnet            > /dev/null 2>&1 || yum -y install telnet
    rpm -q bind-utils        > /dev/null 2>&1 || yum -y install bind-utils
    rpm -q tcpdump           > /dev/null 2>&1 || yum -y install tcpdump
    rpm -q sysstat           > /dev/null 2>&1 || yum -y install sysstat
    rpm -q tcpdump           > /dev/null 2>&1 || yum -y install tcpdump
    rpm -q net-snmp          > /dev/null 2>&1 || yum -y install net-snmp
    rpm -q net-snmp-utils    > /dev/null 2>&1 || yum -y install net-snmp-utils
    rpm -q wget              > /dev/null 2>&1 || yum -y install wget
    rpm -q rsync             > /dev/null 2>&1 || yum -y install rsync
    rpm -q nmap              > /dev/null 2>&1 || yum -y install nmap
    rpm -q net-tools         > /dev/null 2>&1 || yum -y install net-tools
    rpm -q mailx             > /dev/null 2>&1 || yum -y install mailx
    rpm -q nmap-ncat         > /dev/null 2>&1 || yum -y install nmap-ncat
}


#----------------------------------------------------
case ${1} in
    centos7) centos7
        ;;
    centos6) centos6
        ;;
    *) echo "$1 option is valid"
    ;;
esac