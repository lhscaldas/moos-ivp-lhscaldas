#!/bin/bash

ROOT_DIR=$(pwd)

#java -Djava.library.path=${HOME}/local/lib -cp ${ROOT_DIR}/dist/lib/py4j0.10.9.1.jar:${HOME}/local/lib/tpn_p3d-GNU8.3-1_6_2.jar:${ROOT_DIR}/dist/lib/commons-math3-3.6.jar:${ROOT_DIR}/dist/MatlabTools.jar tpn.dp.py4j.DPEntryPoint &
java -Djava.library.path=${ROOT_DIR}/bin -cp ${ROOT_DIR}/lib/py4j0.10.9.1.jar:${ROOT_DIR}/lib/tpn_p3d-GNU8.3-1_6_2.jar:${ROOT_DIR}/lib/commons-math3-3.6.jar:${ROOT_DIR}/MatlabTools.jar tpn.dp.py4j.DPEntryPoint &
