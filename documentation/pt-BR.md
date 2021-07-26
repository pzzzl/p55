<h1 align="center">P55 ⛏</h1>

<p align="center">
    <img src="https://img.shields.io/badge/versão-2.0.0-brightgreen"> <img src="https://img.shields.io/badge/funcionalidade-Organização%20de%20arquivos-orange"> <img src="https://img.shields.io/badge/ferramentas-utilidades-blue">
</p>

<p align="center"><b><i>P55</i></b> é um pacote feito para centralizar todos os arquivos de uma árvore de diretórios em uma única pasta e também organizá-los por extensão.</p>

## Sumário

- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Como funciona?](#como-funciona)
    1. [Extração](#extração)
    2. [Organização](#organização)
- [Aviso](#aviso)

## Funcionalidades

- [x] Extração de todos os arquivos de uma árvore de diretórios para uma única pasta
- [x] Organização de arquivos pela extensão

## Instalação 

   1. Baixe o instalador <a href="https://github.com/pzzzl/p55/raw/master/installer.zip">aqui</a> 
   2. Execute o instalador e siga os passos até o final
   3. Execute o `P55.exe`

## Como funciona?

### Extração

Imagine que você tem a seguinte estrutura de pasta:

```
C:\USERS\SEU_NOME\DESKTOP\PASTA_EXTRAÍVEL
│   arquivo_1.txt
│   arquivo_2.txt
│
├───subpasta_1
│       arquivo_3.txt
│       arquivo_4.txt
│
└───subpasta_2
    │   arquivo_5.txt
    │
    └───subpasta_3
            arquivo_6.txt
            arquivo_7.txt
```

Seria um trabalho árduo procurar dentro de cada pasta da estrutura movendo tais arquivos para outra pasta "extracted", <b>um por um, pasta por pasta</b>.

Seu objetivo seria algo assim:

```
C:\USERS\SEU_NOME\DESKTOP\PASTA_EXTRAÍVEL
├───extracted
│       arquivo_1.txt
│       arquivo_2.txt
│       arquivo_3.txt
│       arquivo_4.txt
│       arquivo_5.txt
│       arquivo_6.txt
│       arquivo_7.txt
│
├───subpasta_1
└───subpasta_2
    └───subpasta_3
```

O melhor jeito de fazer isso é utilizando o <b><i>P55</i></b>, tornando esta tarefa <i>fácil como 1-2-3</i>. O programa irá verificar toda e qualquer pasta dentro da árvore do diretório especificado, movendo todos os arquivos para a mesma pasta - economizando bastante tempo principalmente em árvores maiores.

### Organização

Normalmente utilizado como um complemento para o [método de extração](#extração), este módulo também pode ser utilizado sozinho. Como exemplificado anteriormente, imagine que você tem a seguinte estrutura de pasta:

```
    arquivo (1)
    arquivo (1).cpanel
    arquivo (1).exe
    arquivo (1).gif
    arquivo (1).jpg
    arquivo (1).mp4
    arquivo (1).msi
    arquivo (1).pdf
    arquivo (1).svg
    arquivo (1).zip
    arquivo (10).exe
    arquivo (11).exe
    arquivo (2).exe
    arquivo (2).gif
    arquivo (3).exe
    arquivo (3).gif
    arquivo (4).exe
    arquivo (5).exe
    arquivo (6).exe
    arquivo (7).exe
    arquivo (8).exe
    arquivo (9).exe
```

Existem diversos arquivos no mesmo diretório, com as mais variadas extensões. Assim que você executar o módulo de organização nesta pasta, o programa irá gerar a seguinte estrutura:

```
└───organized
    │   arquivo (1)
    │
    ├───.cpanel
    │       arquivo (1).cpanel
    │
    ├───.exe
    │       arquivo (1).exe
    │       arquivo (10).exe
    │       arquivo (11).exe
    │       arquivo (2).exe
    │       arquivo (3).exe
    │       arquivo (4).exe
    │       arquivo (5).exe
    │       arquivo (6).exe
    │       arquivo (7).exe
    │       arquivo (8).exe
    │       arquivo (9).exe
    │
    ├───.gif
    │       arquivo (1).gif
    │       arquivo (2).gif
    │       arquivo (3).gif
    │
    ├───.jpg
    │       arquivo (1).jpg
    │
    ├───.mp4
    │       arquivo (1).mp4
    │
    ├───.msi
    │       arquivo (1).msi
    │
    ├───.pdf
    │       arquivo (1).pdf
    │
    ├───.svg
    │       arquivo (1).svg
    │
    └───.zip
            arquivo (1).zip
```

Cada arquivo está agora em sua respectiva pasta de extensão, portanto se torna mais fácil executar qualquer tarefa que você precisar com esses arquivos.

## Aviso 
  A melhor maneira de se trabalhar com arquivos é <b>SEMPRE</b> tornando-os seguros primeiro. Para prevenir perda de dados, tenha certeza que você tem um backup antes de executar o programa. O código foi feito para não permitir esses contratempos, mas nunca se sabe. Aproveite! 😀
