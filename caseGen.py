#!/usr/bin/python
import os
import pathlib
import argparse
from sys import stderr, stdout
#################

#----GLOBAL VARIABLES-----#
CASE_NAME="case"

#################


def cwd() -> str:
    directorioActual = os.getcwd()
    directorioActual = str(directorioActual)
    return directorioActual    

    

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="Problem Case Generator",
        description="""
            Generador de casos para problemas de Programación competitiva 
            Siguiendo el estandar .in .out de la plataforma OmegaUp
        """
        
    )

    parser.add_argument(
        '-o', '--outputs',
        action='store_true',
        help='recibe la ruta de los casos de entrada, la ruta del ejecutable de solucion y la ruta de destino(por omision=CURRENT_WORKING_DIR) y genera solo los casos de salida'
    )

    parser.add_argument(
        '-n', '--case-name',
        action='store_true',
        help="Recibe el nombre que llevaran los casos de entrada y salida (todos lo casos se nombraran como caseName#.in caseName#.out e.j casoFacil5.in casoFacil5.out)"
    )

    return parser.parse_args()
    

def main():
    agrs = cli()
    print(cwd())


if __name__ == "__main__":
    main()
