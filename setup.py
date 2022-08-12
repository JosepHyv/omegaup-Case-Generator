from setuptools import setup

setup(
    name="omegaupCaseGen",
    version='1.0.0',
    description="programa TUI que nos facilita la creacion de casos para problemas de programación competitiva siguiendo el estandar .in .out de la plataforma Omegaup",
    author="Joseph Hynimoto Aguilar Lopez",
    author_email='josephynimoto@gmail.com',
    url='https://github.com/JosepHyv/omegaup-Case-Generator',
    packages=['omegaupCaseGen'],
    install_requires=['argparse'],
    entry_points={
        "console_scripts" : ["caseGen=omegaupCaseGen.caseGen:main"]
    },
)
