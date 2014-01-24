#!/bin/bash
VENVDIR=/home/walden/venv/bin
BASEDIR=/home/walden/walden-obtm-weblog-checkout
LIVEDIR=/var/www/walden/

source $VENVDIR/activate
cd $BASEDIR
OUTPUTDIR=$LIVEDIR make html 