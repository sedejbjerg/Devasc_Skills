#!/bin/bash

echo
echo $(date +"%F")
echo
echo STARTING IOS CHECK


REQUIRED_IOS='16.9.111'
HOSTNAME_SEARCH_TEXT='hostname'
VERSION_SEARCH_TEXT='version'

for f in ./ios_configs/*
do
  HOSTNAME=$(cat $f | grep $HOSTNAME_SEARCH_TEXT | cut -d' ' -f2)
  TMP_VERSION=$(cat $f | grep $VERSION_SEARCH_TEXT | cut -d' ' -f2)
  IOS_VERSION=$(echo $TMP_VERSION | sed -e 's/\r//g')
  echo Device hostname: $HOSTNAME
  echo IOS version: $IOS_VERSION
  if [ $REQUIRED_IOS != $IOS_VERSION ]
  then
    echo Upgrade ios to version: $REQUIRED_IOS
  else
    echo Upgrade not necessary
  fi
  echo
done
echo ENDING IOS CHECK

