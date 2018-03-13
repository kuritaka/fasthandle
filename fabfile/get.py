import sys, os
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

FHHOME=os.environ["FHHOME"]

#------------------------------------------------------------------
# get.file_remote_local
#     get.file_remote_local:/etc/hosts,hosts
#------------------------------------------------------------------
@task
def file_remote_local(remote,local):
    """get.file_remote_local:/etc/hosts,hosts"""
    date = datetime.now().strftime('%Y%m%d_%H%M')
    hostname = run("hostname")
    outfile = "%s/tmp/%s.%s.%s"  % (FHHOME, local, hostname, date)
    
    sudo("cp %s /tmp/%s" % (remote,date))
    get("/tmp/%s, %s" % (date, outfile))
    local("ls -lh %s" % (outfile))
    run("rm -f /tmp/%s" % date)

#------------------------------------------------------------------
# get.sdiff_remote_local
#     get.sdiff_remote_local:/etc/hosts,/home/fasthandle/conf/hosts.server1
#------------------------------------------------------------------
@task
def sdiff_remote_local(remote,local):
    """get.sdiff_remote_local:/etc/hosts,/home/fasthandle/conf/etc/hosts.server1"""
    date = datetime.now().strftime('%Y%m%d_%H%M')
    hostname = run("hostname")
    outfile = "%s/tmp/%s.%s"  % (FHHOME, hostname, date)
    
    sudo("cp %s /tmp/%s" % (remote,date))
    get("/tmp/%s, %s" % (date, outfile))
    local("sdiff -s -w 150 %s %s" % (outfile, local))
    
    run("rm -f /tmp/%s" % date)
    local("rm -f %s" % outfile)


#------------------------------------------------------------------
# get.systeminfo
#------------------------------------------------------------------
@task
def systeminfo():
    hostname = run("hostname")
    date = datetime.now().strftime('%Y%m%d_%H%M')
    yearmonth = datetime.now().strftime('%Y%m')
    outfile = "systeminfo.%s.%s"  % (hostname, date)
 
    local("test -d output/%s || mkdir output/%s"    % (yearmonth, yearmonth))
    run("test -d scripts || mkdir scripts")
 
    put("%s/scripts/systeminfo.sh" % FHHOME, "scripts/systeminfo.sh", mode=0755)
    sudo("scripts/systeminfo.sh 1>output/%s  2>/dev/null"   % (outfile))
    get("output/%s", "output/%s/%s"  % (outfile, yearmonth, outfile))
 
