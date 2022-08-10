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
        default=cwd(),
        help='recibe la ruta de los casos de entrada, la ruta del ejecutable de solucion y la ruta de destino(por omision=CURRENT_WORKING_DIR) y genera solo los casos de salida'
    )

    parser.add_argument(
        '-c', '--case-name',
        action='store_true',
        default=CASE_NAME,
        help="Recibe el nombre que llevaran los casos de entrada y salida (todos lo casos se nombraran como caseName#.in caseName#.out e.j casoFacil5.in casoFacil5.out)"
    )

    parser.add_argument(
        '-t', '--total-cases',
        dest="numero de casos",
        type=int,
        default=10,
        help="denota el numero de casos que se generarán"
    )

    parser.add_argument(
        'sourceGenerator',
        type=pathlib.Path,
        help="Dirección del ejecutable/nombre ejecutable generador de las entradas"
    )

    parser.add_argument(
        'sourceSolution',
        type=pathlib.Path,
        help="Dirección del ejecutable/nombre ejecutable generador de solucion"
    )

    parser.add_argument(
        'destinationFolder',
        type=pathlib.Path,
        help="Dirección en donde se guardaran las input y outputs"
    )

    return parser.parse_args()
    

def main():
    args = cli()
    print(args)


if __name__ == "__main__":
    main()
