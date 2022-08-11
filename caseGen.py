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
EXTENSIONS = ['.in', '.out']
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
        '-p', '--overriding',
        action='store_true',
        help="da permisos de sobre escritura de casos (ayuda a omitir el contestar [s/N] en cada pregunta de sobre escritura"
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

def isExecutable(source : pathlib.Path):
    shellArgs = shlex.split("file " + str(source))
    outputRun = subprocess.check_output(shellArgs)
    outputRun = str(outputRun).lower()
    return ("executable" in outputRun)

def writeFile(destinationFolder: pathlib.Path, nameFile :str, buffer,  overridingPermision) -> None:

    statusOverriding = overridingPermision
    if os.path.exists(destinationFolder) and not statusOverriding:
        print("{} ya existe quieres sobreEscribir?".format(nameFile))
        ans = input("[s/N]: ").lower()
        if ans == 's':
            statusOverriding = True
        else:
            print("Omitiendo {}".format(nameFile))

    if not os.path.exists(destinationFolder) or statusOverriding :
        with open(destinationFolder, "w") as caseInput:
            caseInput.write(buffer)



def callInputGenerator(inputGen :pathlib.Path, destinationDir:pathlib.Path, caseName : str, overridingPermision ) -> None:
    excecName = os.path.split(inputGen)
    tailName = excecName[0]
    excecName = str(excecName[1])
    executableLine = str(os.path.join(str(tailName),("./" + excecName)))
    shellArgs = shlex.split(executableLine)

    try:
        #outBuffer = subprocess.run(shellArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) 
        outBuffer = subprocess.Popen(shellArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True).communicate()
        #Popen is best for redirect data :3
    except Exception as e:
        print("Ocurrio un error {}".format(e))

    global EXTENSIONS
    outName = caseName + EXTENSIONS[0]
    print("esto es --->" , caseName)
    inputFileDir = os.path.join(destinationDir, outName)
    writeFile(inputFileDir, outName, outBuffer[0] ,overridingPermision)
    
    

def callSolutionGenerator(solutionGen: pathlib.Path, destinationDir :pathlib.Path, caseName:str) -> None:
    pass


def checkDirs():
    pass


def main():
    args = cli()
      #  callExecs(args.sourceGenerator, args.sourceSolution, args.case_name)
    callInputGenerator(args.sourceGenerator, args.destinationFolder, args.case_name, args.overriding)

    print(args)

if __name__ == "__main__":
    main()
