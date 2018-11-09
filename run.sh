#!/bin/bash

cd `echo $0 | sed 's/\(.*\)\/.*/\1/'` # extract pathname
# check whether echo has the -e option
if test "`echo -e`" = "-e" ; then ECHO=echo ; else ECHO="echo -e" ; fi

CURR_DIR=`pwd`
$ECHO " $CURR_DIR "
$ECHO "InsightDataScience test"
$ECHO "h1b_statistics test:"
$ECHO "@pplicant: Shayan Hemmatiyan"
$ECHO "Current directory: $CURR_DIR "

INPUT=$CURR_DIR/input/h1b_input.csv
$ECHO "Input file: $INPUT"

CODE=./scr/h1b_counting.py  
$ECHO "Code: $CODE"

for DIR in "$INPUT_DIR" "$PSEUDO_DIR" ; do
    if test ! -d $DIR ; then
        $ECHO
        $ECHO "ERROR: $DIR not existent or not a directory"
        $ECHO "Aborting"
        exit 1
    fi
done

python  $CODE
#python $CODE $INPUT >out.txt
