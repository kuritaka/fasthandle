#!/bin/bash
#===============================================
# create_sslsan_csr_key.sh
#
# How to use
#     create_sslsan_csr_key.sh  www.example.com test.example.com
#===============================================

if [ -z $1 ]; then
cat << @
ERROR: \$1 argument is null
How to use:
  create_sslsan_csr_key.sh example.com www.example.com
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


FILE=req.txt

cat > ${FILE} <<-EOF
[req]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C  = ${C}
ST = ${ST}
L  = ${L}
O  = ${O}
OU = ${OU}
CN = ${CN}

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
EOF

NUM=1
for i in $@
do
    echo DNS.${NUM} = $i >> ${FILE}
    NUM=`expr ${NUM} + 1`
done


#Create CSR and Key
openssl req -new -newkey rsa:2048 -nodes -keyout ${CN}.key -out ${CN}.csr -config ${FILE}


#Check CSR
cat << EOF
==========================================================
Check
==========================================================
# ls -ltrh  ${CN}* |tail -n 2
`ls -ltrh ${CN}* |tail -n 2`

#openssl req -text -in ${CN}.csr |grep -E "Subject:|DNS" |grep -v Key
`openssl req -text -in ${CN}.csr |grep -E "Subject:|DNS" |grep -v Key`
EOF