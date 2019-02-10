import sys, os
from fabric.api import *
from fabric.contrib import files
from fabric.utils import abort

FHHOME=os.environ["FHHOME"]

#====================================================================
#check
#====================================================================
#------------------------------------------------
#user.check_user:user01
#------------------------------------------------
@task 
def check_user(user):
    """user.check_user:user01"""
    res = run("id %s" % user, warn_only=True)
    if res.failed is True:
        puts(red("There isn't %s in %s." % (user, env.host_string)))
        return
    run("cat /etc/passwd| grep %s" % user) #check login shell

#------------------------------------------------
#user.check_group:group01
#------------------------------------------------
@task 
def check_group(group):
    """user.check_group:group01"""
    res = run("grep %s /etc/group" % group, warn_only=True)
    if res.failed is True:
        puts(red("There isn't %s in %s." % (group, env.host_string)))
        return


#====================================================================
# user.useradd
#    useradd -m -u UID -g GROUP -G GROUP1,GROUP2 -s /bin/bash -d HOME_DIR LOGIN
#    -m : create the user's home directory
#====================================================================
#------------------------------------------------
#user.useradd_dev_all
#------------------------------------------------
@task
def useradd_dev_all():
    useradd_devuser01()
    useradd_devuser02()
    useradd_devuser03()

#------------------------------------------------
#user.useradd_devuser01
#------------------------------------------------
@task
def useradd_devuser01():
    res = run("id devuser01", warn_only=True)
    if res.failed is True:
        sudo("useradd -m -u 1101 -g dev  devuser01")
        return

@task
def useradd_devuser02():
    res = run("id devuser02", warn_only=True)
    if res.failed is True:
        sudo("useradd -m -u 1102 -g dev devuser02")
        return


#------------------------------------------------
#user.useradd_opeuser
#------------------------------------------------
@task
def useradd_opeuser01():
    res = run("id opeuser01", warn_only=True)
    if res.succeeded is True:
        abort("You already have opeuser01.")
    sudo("useradd -m -u UID -g GROUP opeuser01")


#====================================================================
#chpasswd
#    Dont't use '$' , '#' in password. Because '$' is needed escape.
#====================================================================

#------------------------------------------------
# chpasswd root
#------------------------------------------------
# user.chpasswd_root_pro
@task 
def chpasswd_root_pro():
    ''' PASSWORD is E5*******5 '''
    sudo("echo 'root:$1$0u422IQv$YSGCzz8mesPzCaWxHCxit.' | chpasswd -e")

# user.chpasswd_root_stg
@task 
def chpasswd_root_stg():
    ''' PASSWORD is S3*******! '''
    sudo("echo 'root:$1$0u333IQv$YSGCzz8mesPzCaWxHCxit.' | chpasswd -e")

# user.chpasswd_root_qa
@task 
def chpasswd_root_qa():
    ''' PASSWORD is AW*******5 '''
    sudo("echo 'root:$1$0u444IQv$YSGCzz8mesPzCaWxHCxit.' | chpasswd -e")


#------------------------------------------------
# chpasswd devuser01
#------------------------------------------------
# user.chpasswd_devuser01_pro
@task
def chpasswd_devuser01_pro():
    sudo("id devuser01 && echo 'devuser01:PASS' | chpasswd", warn_only=True)

# user.chpasswd_devuser01_stg
@task
def chpasswd_devuser01_stg():
    sudo("id devuser01 && echo 'devuser01:PASS' | chpasswd", warn_only=True)

# user.chpasswd_devuser01_qa
@task
def chpasswd_devuser01_qa():
    sudo("id devuser01 && echo 'devuser01:PASS' | chpasswd", warn_only=True)


#------------------------------------------------
# chpasswd devuser02
#------------------------------------------------
# user.chpasswd_devuser02_pro
@task
def chpasswd_devuser02_pro():
    sudo("id devuser02 && echo 'devuser02:PASS' | chpasswd", warn_only=True)


# user.chpasswd_devuser02_stg
@task
def chpasswd_devuser02_stg():
    sudo("id devuser02 && echo 'devuser02:PASS' | chpasswd", warn_only=True)

#------------------------------------------------
# chpasswd devuser03
#------------------------------------------------
# user.chpasswd_devuser03_pro
@task
def chpasswd_devuser03_pro():
    sudo("id devuser03 && echo 'devuser03:PASS' | chpasswd", warn_only=True)




#====================================================================
# userdel
#    -r, --remove : Files in the user's home directory will be removed
#====================================================================
# user.userdel_devuser01
@task
def userdel_devuser01():
    sudo("id devuser01 && userdel -r devuser01")

# user.userdel_devuser02
@task
def userdel_devuser02():
    res = run("id devuser02", warn_only=True)
    if res.succeeded is True:
        sudo("tar zcf /tmp/devuser02.tar.gz /home/devuser02")
        sudo("userdel -r devuser02")
        return



