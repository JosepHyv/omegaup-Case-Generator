#!/usr/bin/env python
import os
import shlex
import pathlib
import argparse
import subprocess
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
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )

    parser.add_argument(
        '-o', '--outputs',
        action='store_true', #me permite guardar el input despues de la bandera
        help='Nos permite generar solo las salidas dadas las entradas ya generadas, toma la ruta del generador de entradas como la ruta de todas las entradas almacenadas, la ruta del ejecutable de solucion y la ruta de destino(por omision=CURRENT_WORKING_DIR) y genera solo los casos de salida'
    )

    parser.add_argument(
        '-c', '--case_name',
        action='store',
        default=CASE_NAME,
        help="Recibe el nombre que llevaran los casos de entrada y salida (todos lo casos se nombraran como caseName#.in caseName#.out e.j casoFacil5.in casoFacil5.out)"
    )

    parser.add_argument(
        '-t', '--total_cases',
        action='store',
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
        nargs='?',
        default=cwd(),
        help="Dirección en donde se guardaran las input y outputs (por omision=CURRENT_WORKING_DIR)"
    )

    return parser.parse_args()

def callExecs(inputGen : pathlib.Path, solGen : pathlib.Path, nameCase : str):
    print(type(inputGen))
    print(type(solGen))
    print(nameCase)
    pass

def main():
    args = cli()
    
    callExecs(args.sourceGenerator, args.sourceSolution, args.case_name)

    print(args)

if __name__ == "__main__":
    main()
