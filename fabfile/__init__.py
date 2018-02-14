import sys, select
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

env.warn_only = True
env.port = 22
env.eagerly_disconnect = True


# standard in for example echo x.x.x.x
if select.select([sys.stdin,],[],[],0.0)[0]:
    lines = sys.stdin.read().splitlines()
    env.hosts = filter(bool, lines)


#FastHandle Operation History to log file
TIME = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
yymm = datetime.now().strftime('%Y%m')

f=open("%s/log/history.%s.log" % (FHHOME,yymm) ,"a")
f.write("%s " % TIME)
f.write(' '.join(str(p) for p in sys.argv))
f.write("\n")
f.close()


#-------------------------------------------
# import 
#-------------------------------------------
import auth
import test

## OS Management
import user
import pkg
import net
import set
import get
import check
import ope

## Middleware Management
import httpd
import nginx
import postfix
import squid

## Programing Languages
import php
