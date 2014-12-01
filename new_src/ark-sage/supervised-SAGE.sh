#!/bin/sh

# JAVA=/usr/java/latest/bin/java
JAVA=`which java`
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIB_DIR=${SCRIPT_DIR}/lib

$JAVA -XX:ParallelGCThreads=2 -cp ${SCRIPT_DIR}/ark-sage-0.1.jar:${LIB_DIR}/stanford-classifier.jar:${LIB_DIR}/commons-math3-3.1.1.jar:${LIB_DIR}/trove-3.0.3.jar:${LIB_DIR}/yc-config-0.2.jar:${LIB_DIR}/JSAP-2.1.jar edu.cmu.cs.ark.sage.apps.SupervisedSAGE $@

