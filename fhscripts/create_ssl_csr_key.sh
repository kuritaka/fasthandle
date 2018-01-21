#!/bin/bash
#===============================================
# create_ssl_csr_key.sh
#
# How to use
#     create_ssl_csr_key.sh  example.com
#     create_ssl_csr_key.sh  192.168.0.10
#===============================================

if [ -z $1 ]; then
cat << @
ERROR: \$1 argument is null
How to use:
  create_csr_key.sh 192.168.0.10
@
exit 1
fi

C="JP"
ST="Tokyo"
L="Shibuya-ku"
O="Example, Inc."
OU="IT"
CN="$1"


test -f ${CN}.csr && mv ${CN}.csr ${CN}.csr.`date +%Y%m%d_%H%M`
test -f ${CN}.key && mv ${CN}.key ${CN}.key.`date +%Y%m%d_%H%M`

openssl req -new -newkey rsa:2048 -nodes -out ${CN}.csr -keyout ${CN}.key -sha256 -subj "/C=${C}/ST=${ST}/L=${L}/O=${O}/OU=${OU}/CN=${CN}"

cat << @
==========================================================
Check
==========================================================

# ls -ltrh  ${CN}* |tail -n 2
`ls -ltrh ${CN}* |tail -n 2`

#openssl req -text -in ${CN}.csr |grep "Subject:"
`openssl req -text -in ${CN}.csr |grep "Subject:"`

@
