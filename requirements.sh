#!/usr/bin/env bash

conda create -n Placement-Cell-Management-System python=3.6
source activate Placement-Cell-Management-System
pip install PyQt5==5.11.3
pip install SQLAlchemy==1.2.17
pip install psycopg2-binary==2.7.7