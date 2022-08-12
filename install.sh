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

git clone https://github.com/JosepHyv/omegaup-Case-Generator.git 

if [[ -d $PROJECT_FOLDER ]]
then 
	pip3 install -r "$PROJECT_FOLDER/requeriments.txt"
	sudo python3 "$PROJECT_FOLDER/setup.py" install
	caseGen --version
fi

[ -d $PROJECT_FOLDER ] && rm -r $PROJECT_FOLDER

echo "Finish"
