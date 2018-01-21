import sys, os
from fabric.api import *
from fabric.contrib import files

FHHOME=os.environ["FHHOME"]

# net.backup_config
@task
def backup_config():
    date = datetime.now().strftime('%Y%m%d_%H%M')
    run("test -d /tmp/nwconf_%s || mkdir /tmp/nwconf_%s" % date)
    # RHEL/CentOS
    run("cp -f /etc/sysconfig/network-scripts/ifcfg* /tmp/nwconf_%s/" % date)
    # Debian/Ubuntu
    run("cp -f /etc/network/interfaces /tmp/nwconf_%s/" % date)
    run("cp -f /etc/sysconfig/static-routes /tmp/nwconf_%s/" % date)


# net.set_bond:192.168.0.10,bond0,eth0,eth2
@task
def set_bond(ip,bond,nic1,nic2):
    backup_config()
    date = datetime.now().strftime('%Y%m%d_%H%M')
    # put
    put("%s/etc/sysconfig/network-scripts/ifcfg-bond.tpl" % FHHOME, "/tmp/ifcfg-%s.%s" % (bond,date))
    put("%s/etc/sysconfig/network-scripts/ifcfg-bond_nic.tpl" % FHHOME, "/tmp/ifcfg-%s.%s" % (nic1,date))
    put("%s/etc/sysconfig/network-scripts/ifcfg-bond_nic.tpl" % FHHOME, "/tmp/ifcfg-%s.%s" % (nic2,date))

    # bond
    sed("/tmp/ifcfg-%s.%s" % (bond,date), before="DEVICE=bondX", after="DEVICE=%s" % ip)
    sed("/tmp/ifcfg-%s.%s" % (bond,date), before="IPADDR=x.x.x.x", after="IPADDR=%s" % ip)
    # nic1
    sed("/tmp/ifcfg-%s.%s" % (nic1,date), before="DEVICE=X", after="DEVICE=%s" % nic1)
    sed("/tmp/ifcfg-%s.%s" % (nic1,date), before="MASTER=X", after="MASTER=%s" % bond)
    # nic2
    sed("/tmp/ifcfg-%s.%s" % (nic2,date), before="DEVICE=X", after="DEVICE=%s" % nic2)
    sed("/tmp/ifcfg-%s.%s" % (nic2,date), before="MASTER=X", after="MASTER=%s" % bond)

    run("diff /tmp/ifcfg-%s.%s  /etc/sysconfig/network-scripts/ifcfg-%s" % (bond,date,bond))
    run("diff /tmp/ifcfg-%s.%s  /etc/sysconfig/network-scripts/ifcfg-%s" % (nic1,date,nic1))
    run("diff /tmp/ifcfg-%s.%s  /etc/sysconfig/network-scripts/ifcfg-%s" % (nic2,date,nic2))

    sudo("mv /tmp/ifcfg-%s.%s  /etc/sysconfig/network-scripts/ifcfg-%s" % (bond,date,bond))
    sudo("mv /tmp/ifcfg-%s.%s /etc/sysconfig/network-scripts/ifcfg-%s" % (nic1,date.nic1))
    sudo("mv /tmp/ifcfg-%s.%s /etc/sysconfig/network-scripts/ifcfg-%s" % (nic2,date,nic2))


