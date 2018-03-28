#!/bin/bash
#===============================================
# create_ssh_keypair.sh
#
# How to use
#     create_ssh_keypair.sh   user01  test-server-01
#===============================================

if [ "$#" -ne 2 ] ; then
cat << @
ERROR : argument isn't correct.
How to use:
  create_ssh_keypair.sh  user01 test-server-01
@
exit 1
fi

USER=$1
HOST=$2

OUTFILE=id_rsa."${USER}"."${HOST}"

test -f ${OUTFILE} && mv ${OUTFILE} ${OUTFILE}.`date +%Y%m%d_%H%M`
test -f ${OUTFILE}.pub && mv ${OUTFILE}.pub ${OUTFILE}.pub.`date +%Y%m%d_%H%M`

ssh-keygen -t rsa -b 2048 -C "${USER}@${HOST}"  -N "" -f ${OUTFILE}


cat << @
==========================================================
Check
==========================================================

# ls -ltrh  ${OUTFILE}* |tail -n 2
`ls -ltrh ${OUTFILE}* |tail -n 2`

@
