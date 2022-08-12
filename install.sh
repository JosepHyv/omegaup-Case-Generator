#!/usr/bin/bash
PROJECT_FOLDER="omegaup-Case-Generator"
if [[ ! $(command -v git ) ]]
then 
	echo "Necesitas installar git"
	exit 1
fi

if [[ ! $(command -v python3 ) ]]
then 
	echo "Necesitas installar python >= 3.10"
	exit 1
fi


if [[ ! $(command -v pip3 ) ]]
then 
	echo "Necesitas installar pip en su versión más reciente"
	exit 1
fi

#creando carpeta temporal 
mkdir tempInstallation
cd tempInstallation

#clonando 

git clone https://github.com/JosepHyv/omegaup-Case-Generator.git 

if [[ -d $PROJECT_FOLDER ]]
then 
	pip3 install -r "$PROJECT_FOLDER/requeriments.txt"
	cd $PROJECT_FOLDER
	sudo python3 "setup.py" install
	caseGen --version
	echo "========================================="
	echo "Limpiando carpetas de instalacion"	
	cd ../..
	[ -d tempInstallation ] && sudo rm -r tempInstallation
fi


echo "Finish"
