import sys, select
from fabric.api import *
from fabric.contrib import files
   
env.warn_only = True
env.port = 22
env.eagerly_disconnect = True
 
 
if select.select([sys.stdin,],[],[],0.0)[0]:
    lines = sys.stdin.read().splitlines()
    env.hosts = filter(bool, lines)
 
 
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
import tftp
 
## Programing Languages
import php
