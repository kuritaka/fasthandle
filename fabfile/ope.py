import sys
from fabric.api import *
from fabric.contrib import files
from fabric.operations import open_shell

FHHOME=os.environ["FHHOME"]

#------------------------------------------------------------------
# ope.put
#     fab auth.pro ope.put:/home/fasthandle/rpm/abc.rpm,/tmp/abc.rpm
#------------------------------------------------------------------
@task
def put(local,remote):
    """fab auth.pro ope.scp:/home/fasthandle/rpm/abc.rpm,/tmp/abc.rpm"""
    put("%s", "%s" % (local,remote))


#------------------------------------------------------------------
# ope.ssh
#     fab auth.pro ope.ssh:"sudo vi /etc/hosts"
# WARNING: This is too late for copy and past. So you use usually fhssh.sh
#------------------------------------------------------------------
@task
def ssh():
    '''fab auth.pro ope.ssh '''
    open_shell("hostname")


#------------------------------------------------------------------
# ope.sshcmd
#     fab auth.pro ope.ssh:"sudo vi /etc/hosts"
#------------------------------------------------------------------
@task
def sshcmd(cmd):
    '''fab auth.pro ope.sshcmd:"sudo vi /etc/hosts" '''
    open_shell("%s" % cmd)


#------------------------------------------------------------------
# ope.sudo_vi
#     fab -H x.x.x.x auth.pro ope.vi:/etc/hosts
#
# WARNING: open_shell didn't use 'echo x.x.x.x |fab ' and 'fhghost.sh'
#
#------------------------------------------------------------------
@task
def sudo_vi(file):
    """fab auth.pro ope.vi:/etc/hosts"""
    open_shell("sudo_vi %s && exit" % (file))



#------------------------------------------------------------------
# ope.cp_p_1dayago(file)
#     fab auth.pro ope.cp_p_1dayago:/etc/hosts
#------------------------------------------------------------------
@task
def cp_p_1dayago(file):
    """fab auth.pro  cp_p_1dayago:/etc/host,/etc/hosts"""
    sudo("cp -p %s %s.`date -d '1day ago' +%Y%m%d`") % (file, file))



#------------------------------------------------------------------
# ope.reboot
#------------------------------------------------------------------
@task 
def reboot():
    sudo("shutdown -r now", warn_only=True)

#------------------------------------------------------------------
# ope.shutdown
#------------------------------------------------------------------
@task 
def shutdown():
    run("shutdown -h now", warn_only=True)


