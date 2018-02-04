#!/bin/bash
#==============================================================================
# systeminfo.sh
#
# How to use
#     systeminfo.sh  2>/dev/null
#==============================================================================

LANG=C

#==============================================================================
# Function
#==============================================================================


#==============================================================================
# Main
#==============================================================================
cat << @
## hostname ####
`hostname`

## uname -a ####
`uname -a`

## cat /etc/redhat-release ####
`cat /etc/redhat-release`

#----------------------------------------------------------
# Hardware
#----------------------------------------------------------
## The number of Processors like top command
## cat /proc/cpuinfo | grep processor |wc -l ####
`cat /proc/cpuinfo | grep processor |wc -l`

## The number of total core
## cat /proc/cpuinfo |grep "cpu cores" | perl -e 'while(<>){$n+=/(\d+)/?$1:0;}print"$n\n";' ####
`cat /proc/cpuinfo |grep "cpu cores" | perl -e 'while(<>){$n+=/(\d+)/?$1:0;}print"$n\n";'`


## cat /proc/meminfo  |egrep "MemTotal|SwapTotal" ####
`cat /proc/meminfo  |egrep "MemTotal|SwapTotal"`

## df -h  |grep -v tmpfs
`df -h  |grep -v tmpfs`

## mount | egrep ^/dev ####
`mount | egrep "^/dev|nfs"`


#----------------------------------------------------------
# Networking
#----------------------------------------------------------
## cat /etc/sysconfig/static-routes ####
`cat /etc/sysconfig/static-routes`


## ip a |egrep "mtu|inet" |grep -v inet6 ####
`ip a |egrep "mtu|inet" |grep -v inet6`


#----------------------------------------------------------
# Package
#----------------------------------------------------------
## which rpm > /dev/null 2>&1 && rpm -qa --qf '%{name}\n' |sort ####
`which rpm > /dev/null 2>&1 && rpm -qa --qf '%{name}\n' |sort`

@

