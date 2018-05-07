#!/bin/sh
#=======================================================
# check_cmd.sh
#=======================================================


which rsync       >/dev/null 2>&1 || echo "rsync NG"
which vim         >/dev/null 2>&1 || echo "vim   NG"
which tree        >/dev/null 2>&1 || echo "tree  NG"
which wget        >/dev/null 2>&1 || echo "wget  NG"

#-----------------------------------------------------
#Netowrk
#-----------------------------------------------------
which ifconfig    >/dev/null 2>&1 || echo "ifconfig NG"
which netstat     >/dev/null 2>&1 || echo "netstat  NG"
which dig         >/dev/null 2>&1 || echo "dig      NG"
which host        >/dev/null 2>&1 || echo "host     NG"
which nmap        >/dev/null 2>&1 || echo "nmap     NG"
which nc          >/dev/null 2>&1 || echo "nc       NG"
which traceroute  >/dev/null 2>&1 || echo "traceroute  NG"
which tcpdump     >/dev/null 2>&1 || echo "tcpdump  NG"
which snmpget     >/dev/null 2>&1 || echo "snmpget  NG"
which snmpwalk    >/dev/null 2>&1 || echo "snmpwalk  NG"

#-----------------------------------------------------
#Peformance
#-----------------------------------------------------
which dstat       >/dev/null 2>&1 || echo "dstat    NG"
which iperf       >/dev/null 2>&1 || echo "iperf    NG"



#-----------------------------------------------------
#etc
#-----------------------------------------------------
which ccze       >/dev/null 2>&1 || echo "ccze    NG   # ccze is log colorizer"