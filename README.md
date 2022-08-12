# omegaup-Case-Generator
OmegaupCaseGenerator es un programa escrito en python que nos facilita la tarea de crear casos de prueba para problemas de programación competitiva, siguiendo el [estandar de archivos](https://github.com/omegaup/omegaup/wiki/C%C3%B3mo-escribir-problemas-para-Omegaup) de la plataforma [Omegaup](https://omegaup.com/)

## Constraints
Este programa fue creado en python 3.10 corriendo sobre manjaro(linux) y testeado en otras distribuciónes linux incluyendo wsl, no se asegura el correcto funcionamiento instalando y corriendo este programa de forma nativa en MacOs o Windows

## Installation

**Instalación Rapida**

| Metodo | Comando                                                                              |
| :----- | :------------------------------------------------------------------------------------|
| CURL   | `curl -fsSl https://raw.githubusercontent.com/JosepHyv/omegaup-Case-Generator/main/install.sh \| bash`    |
| WGET   | `wget -O- https://raw.githubusercontent.com/JosepHyv/omegaup-Case-Generator/main/install.sh \| bash` |


si utilizas zsh puedes reemplazar bash por zsh en las lineas anteriores 

**Instalación desde el codigo fuente**
1. Clona el repositorio

```bash
git clone https://github.com/JosepHyv/omegaup-Case-Generator.git
```

2. Cambiala ruta 
```bash
cd omegaup-Case-Generator
```

3. Ejecuta
```
./install.sh
```

## Usage

Este programa funciona llamando creando subprocesos mientras llama a los ejectubales que generan las input y outputs y genera el numero de casos que necesites en la dirección deseada, con permisos de sobreescritura
1. Uso Basico 
```bash
caseGen dir/generadorInputs dir/solucionDelProblema dirDestino(por defecto esta es la dirección actual)
```
<script id="asciicast-JlFXq3XjLQ81ugWPcsvea8ChY" src="https://asciinema.org/a/JlFXq3XjLQ81ugWPcsvea8ChY.js" async></script>

2. Uso Solo Salidas 
Esta opcion es util cuando necesitamos generar solo las salidas de cada entrada ya generada previamente
```bash
caseGen -o dirInputs dir/SolucionDelProblema dirDestino(por defecto sera igual a dirInputs)
```
<html>
<head>
  <link rel="stylesheet" type="text/css" href="asciinema-player.css" />
</head>
<body>
  <div id="player"></div>
  <script src="asciinema-player.min.js"></script>
  <script>
    AsciinemaPlayer.create(
      '514346.cast',
      document.getElementById('player'),
      { cols: 110, rows: 30 }
    );
  </script>
</body>
</html>
