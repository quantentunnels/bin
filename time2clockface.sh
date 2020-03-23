#!/bin/bash
# parse digital time string and output closest Unicode clockface

if [ -z "$1" ]
    then
        time="$(date +"%H:%M")"
    else
        time="$1"
fi

# Taken from https://codegolf.stackexchange.com/a/42311
date -d "$time" +%I\ 60*%M+45-30/24%%2+2~C*+C8335+0PP|dc|iconv -f ucs-4

