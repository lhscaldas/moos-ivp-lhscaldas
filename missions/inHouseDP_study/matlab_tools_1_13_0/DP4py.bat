@echo off
set PWD=%cd%
java -Djava.library.path=%PWD%\bin -cp %PWD%\MatlabTools.jar tpn.dp.py4j.DPEntryPoint
