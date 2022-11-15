#!/bin/bash

if [ $# -eq 0 ];
then
    echo "Please specify a folder which to parse"
    exit 1
fi

archiso=$(curl -s https://archlinux.org/download/ | grep 'magnet' | cut -d '"' -f 2 | sed 2d)
archisoVer=$(echo "$archiso" | cut -d '=' -f 3)



echo $archisoVer
