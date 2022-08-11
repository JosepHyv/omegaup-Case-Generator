#!/usr/bin/bash
for i in {1..100}
do
	./genInput.py > "case$i.in"
	./solution < "case$i.in" > "case$i.out"
	echo "Caso $i Creado!"
done
