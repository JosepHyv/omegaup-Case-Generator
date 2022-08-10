#!/usr/bin/python
import os
import json 
import pathlib
import argparse
#################

#----GLOBAL VARIABLES-----#
CASE_NAME="case"

#################


def cwd() -> str:
    directorioActual = os.getcwd()
    directorioActual = str(directorioActual)
    return directorioActual    

def dump(dest: pathlib.Path ):
    pass
    

def cli():
    pass
    

def main():
    agrs = cli()
    print(cwd())


if __name__ == "__main__":
    main()
