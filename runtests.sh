#!/bin/bash
# Run Tests for Flaskengine


cd tests/ 
find . -name "*.pyc" -exec rm -rf {} \;
clear
nosetests --logging-level=INFO  -s -x -v --without-sandbox --with-gae
cd -