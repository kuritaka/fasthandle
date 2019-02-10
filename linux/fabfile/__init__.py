import sys, os, glob, select, importlib, re
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

#======================================================
# SSH User
#======================================================
hostname = os.uname()[1]

if hostname == "fasthandle-1":
    env.user = 'fasthandle'
    env.password = 'fastpass'
elif hostname == "stg-fasthandle-1":
    env.user = 'fasthandle'
    env.password = 'fastpass'
elif hostname == "dev-fasthandle-1":
    env.user = 'fasthandle'
    env.key_filename = '$FHLINUX/key/id_rsa.fasthandle.dev-fasthandle-1'
    #env.password = 'passphrase-for-key'

#======================================================
# Variable
#======================================================
FHLINUX=os.environ["FHLINUX"]

env.warn_only = True
env.port = 22
env.eagerly_disconnect = True

#don't create *.pyc without __init__.pyc
sys.dont_write_bytecode = True


#======================================================
#======================================================
# standard in for example echo x.x.x.x
if select.select([sys.stdin,],[],[],0.0)[0]:
    lines = sys.stdin.read().splitlines()
    env.hosts = filter(bool, lines)


#FastHandle Operation History to log file
TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
yymm = datetime.now().strftime('%Y%m')

f=open("%s/log/fab.%s.log" % (FHLINUX,yymm) ,"a")

if env.hosts == []:
  f.write("%s stdin-null " % TIME)
  f.write(' '.join(str(p) for p in sys.argv))
  f.write("\n")

for p in env.hosts:
  f.write("%s %s " % (TIME,p))
  f.write(' '.join(str(p) for p in sys.argv))
  f.write("\n")
f.close()


# auto import *.py
# Ref. https://gist.github.com/fereria/3331554f4c480679716b#file-__init__-py
pathThisFile = os.path.dirname(os.path.abspath(__file__))

def loadModule():

    myself = sys.modules[__name__]

    #print __name__

    mod_paths = glob.glob(os.path.join(pathThisFile, '*.py'))
    for py_file in mod_paths:
        mod_name = os.path.splitext(os.path.basename(py_file))[0]
        if re.search(".*__init__.*",mod_name) is None:
            mod = importlib.import_module(__name__+ "." + mod_name)
            #for m in mod.__dict__.keys():
                #if not m in ['__builtins__', '__doc__', '__file__', '__name__', '__package__']:
                    #myself.__dict__[m] = mod.__dict__[m]
loadModule()
