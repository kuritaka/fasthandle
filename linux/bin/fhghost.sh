#!/bin/bash
#===========================================================
# fhghost.sh    FastHandle Grep Host
#
# How to use
#   Help
#     fhghost.sh  -h
#   Test
#     fhghost.sh -a FILE
#   pipe to Fabric
#     fhghost.sh  FILE | fab xxx
#     fhghost.sh  "*"  hosts/xxxx |fab xxx  <- like grep PATTERN FILE
#     fhghost.sh  PATTERN FILE |fab xxx     <- like grep PATTERN FILE
#
#===========================================================

help(){
cat << @
Example
  fhghost.sh  FILE
  fhghost.sh  PATTERN FILE
  fhghost.sh  "*" FILE
@
}

if [ "$#" -eq 0 ] ; then
    help
    exit 0
fi


if [ "$#" -eq 1 ] ; then

    case "$1" in
        -h | --help )
            help
            exit 0
            ;;
        * )
            FILE="$1"
            grep -Ev "^#|^$" "${FILE}"  | awk {'print $1'}
            ;;
    esac
fi

if [ "$#" -eq 2 ] ; then

    case "$1" in
        -a | --all | -t | --test | -v )
            FILE="$2"
            grep -Ev "^#|^$" "${FILE}"
            ;;
        * )
            PATTERN="$1"
            FILE="$2"
            grep -Ev "^#|^$" "${FILE}"  | grep -E "${PATTERN}" | awk {'print $1'}
            ;;
    esac

fi
