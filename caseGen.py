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


def cwd() -> pathlib.Path:
    directorioActual = os.getcwd()
    directorioActual = pathlib.Path(directorioActual)
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
    destinationFolder = os.path.join(destinationFolder, nameFile)
    if os.path.exists(destinationFolder) and not statusOverriding:
        print("{} ya existe quieres sobreEscribir?".format(nameFile))
        ans = input("[s/N]: ").lower()
        if ans == 's':
            statusOverriding = True
        else:
            print("Omitiendo {}".format(nameFile))

    if not os.path.exists(destinationFolder) or statusOverriding :
        with open(destinationFolder, "w") as caseWriting:
            caseWriting.write(buffer)



def callInputGenerator(inputGen :pathlib.Path, destinationDir:pathlib.Path, caseName : str, overridingPermision ) -> None:
    excecName = os.path.split(inputGen)
    tailName = excecName[0]
    excecName = str(excecName[1])
    executableLine = str(os.path.join(str(tailName),("./" + excecName)))
    shellArgs = shlex.split(executableLine)
    print("Ejecutando {}".format(shellArgs))
    try:
        #outBuffer = subprocess.run(shellArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) 
        outBuffer = subprocess.Popen(shellArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True).communicate()
        #Popen is best for redirect data :3
    except Exception as e:
        print("Ocurrio un error {}".format(e))

    global EXTENSIONS
    outName = caseName + EXTENSIONS[0]
    

    writeFile(destinationDir, outName, outBuffer[0] ,overridingPermision)
    
    

def callSolutionGenerator(solutionGen: pathlib.Path, destinationDir :pathlib.Path, caseInputDir:pathlib.Path, overridingPermision) -> None:
    excecName = os.path.split(solutionGen)
    tailName = excecName[0]
    excecName = str(excecName[1])
    executableLine = str(os.path.join(str(tailName),("./" + excecName)))
    shellArgs = shlex.split(executableLine)
    print("Ejecutando {}".format(shellArgs))
    try: 
        with open(caseInputDir, "rb") as fileIn:
                data = fileIn.read()
        process = subprocess.Popen(shellArgs, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outBuffer = process.communicate(input=data)
        #Popen is best for redirect data :3
    except Exception as e:
        print("Ocurrio un error {}".format(e))

    buffertype = str(type(outBuffer[0]))
    fileBuffer = outBuffer[0]
    if 'bytes' in buffertype:
       fileBuffer = outBuffer[0].decode('utf-8')
    
    global EXTENSIONS
    nameFile = os.path.basename(caseInputDir)
    nameFile = os.path.splitext(nameFile)[0]
    nameFile = nameFile+ EXTENSIONS[1]
    writeFile(destinationDir, nameFile, fileBuffer, overridingPermision)
    


def checkDirs(listDirs):
    ok = True
    notOkayDirs = [pathlib.Path(dir) for dir in listDirs if not os.path.exists(dir)]
    if len(notOkayDirs):
        ok = False
        print("Error:")
        print("los siguientes directorios o archivos no existen: ")
        for dir in notOkayDirs:
            print("\t {}".format(dir))

    return ok

def listInputs(source: pathlib.Path) -> list:
    lista = os.listdir(source)
    inputs = [str(file) for file in lista if ".in" in str(pathlib.Path(file).suffix)]
    print(*inputs, sep="\n")
    return inputs

def main():
    global EXTENSIONS
    try:
        args = cli()
        if not checkDirs([args.sourceGenerator, args.sourceSolution, args.destinationFolder]):
            exit(1)

        if args.outputs:
            if isExecutable(args.sourceGenerator):
                print("Error: {} es un ejecutable".format(args.sourceGenerator))
                exit(1)
            elif os.path.isfile(args.sourceGenerator):
                print("Error: {} es un archivo y no un directorio".format(args.sourceGenerator))
                exit(1)
            elif not isExecutable(args.sourceSolution):
                print("Error: {} No un ejecutable".format(args.sourceGenerator))
                exit(1)
            
            print(type(args.destinationFolder), type(cwd()), args.destinationFolder == cwd(), sep="\n")

            if args.destinationFolder == cwd():
                args.destinationFolder = args.sourceGenerator

            if args.total_cases != 10:
                print("El uso de -t es innecesario")

            inputsFiles = listInputs(args.sourceGenerator)
            if not len(inputsFiles):
                print("Error: No existen archivos de entrada\nen{}".format(args.sourceGenerator))
                exit(1)

            for file in inputsFiles:
                completeDir = os.path.join(args.sourceGenerator,file)
                currentInputCase = os.path.splitext(completeDir)[0]
                print("Current --> {}".format((currentInputCase + EXTENSIONS[1])))
                callSolutionGenerator(args.sourceSolution, args.destinationFolder, completeDir, args.overriding)
                print("================\n")


        else:
            for c in range(args.total_cases):
                nameFile = args.case_name + str(c+1)
                print("Current -->" , nameFile)
                callInputGenerator(args.sourceGenerator, args.destinationFolder, nameFile, args.overriding)
                currentInputDir = os.path.join(args.destinationFolder, (nameFile + EXTENSIONS[0]))
                callSolutionGenerator(args.sourceSolution, args.destinationFolder, currentInputDir, args.overriding)
                print("================\n")
    except KeyboardInterrupt:
        print("Deteniendo el programa")
        print("nos vemos luego 😎")


if __name__ == "__main__":
    main()
