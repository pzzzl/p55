<h1 align="center">P55 ⛏</h1>

<p align="center">
    <img src="https://img.shields.io/badge/version-2.0.0-brightgreen"> <img src="https://img.shields.io/badge/feature-File%20organization-orange"> <img src="https://img.shields.io/badge/tools-utilities-blue">
</p>

<p align="center"><b><i>P55</i></b> is a bundle made to center all files from a directory tree into a single folder and also organize them by extension.</p>

## Summary

- [Features](#features)
- [Installation](#installation)
- [How it works?](#how-it-works)
    1. [Extract](#extract)
    2. [Organize](#organize)
- [Advice](#advice)

## Features

- [x] Extract all files from a directory tree into a single folder
- [x] Organize files by extension

## Installation 

   1. Download the installer <a href="https://github.com/pzzzl/p55/raw/master/installer.zip">here</a> 
   2. Run the installer and follow the steps until it's finished
   3. Run `P55.exe`

## How it works?

### Extract

Imagine you have the following folder structure:

```
C:\USERS\YOUR_NAME\DESKTOP\EXTRACTABLE_FOLDER
│   file_1.txt
│   file_2.txt
│
├───subfolder_1
│       file_3.txt
│       file_4.txt
│
└───subfolder_2
    │   file_5.txt
    │
    └───subfolder_3
            file_6.txt
            file_7.txt
```

It would be an extensive work to search into your tree moving those files to another "extracted" folder, <b>one by one, folder by folder</b>.

Your goal would be something like that:

```
C:\USERS\YOUR_NAME\DESKTOP\EXTRACTABLE_FOLDER
├───extracted
│       file_1.txt
│       file_2.txt
│       file_3.txt
│       file_4.txt
│       file_5.txt
│       file_6.txt
│       file_7.txt
│
├───subfolder_1
└───subfolder_2
    └───subfolder_3
```

The better way to do this is by using <b><i>P55</i></b>, making that task <i>easy as 1-2-3</i>. The program will look into every single folder in the given directory tree, moving all files to the same directory - saving a lot of time specially on bigger trees.

### Organize

Often used as a complement to the [extract module](#extract), this module can also be used alone. As exemplified before, imagine you have the following folder structure:

```
    file (1)
    file (1).cpanel
    file (1).exe
    file (1).gif
    file (1).jpg
    file (1).mp4
    file (1).msi
    file (1).pdf
    file (1).svg
    file (1).zip
    file (10).exe
    file (11).exe
    file (2).exe
    file (2).gif
    file (3).exe
    file (3).gif
    file (4).exe
    file (5).exe
    file (6).exe
    file (7).exe
    file (8).exe
    file (9).exe
```

There's a lot of files in the same directory with the most variable extensions. Once you run the organize module on that folder, the program will generate the following structure:

```
└───organized
    │   file (1)
    │
    ├───.cpanel
    │       file (1).cpanel
    │
    ├───.exe
    │       file (1).exe
    │       file (10).exe
    │       file (11).exe
    │       file (2).exe
    │       file (3).exe
    │       file (4).exe
    │       file (5).exe
    │       file (6).exe
    │       file (7).exe
    │       file (8).exe
    │       file (9).exe
    │
    ├───.gif
    │       file (1).gif
    │       file (2).gif
    │       file (3).gif
    │
    ├───.jpg
    │       file (1).jpg
    │
    ├───.mp4
    │       file (1).mp4
    │
    ├───.msi
    │       file (1).msi
    │
    ├───.pdf
    │       file (1).pdf
    │
    ├───.svg
    │       file (1).svg
    │
    └───.zip
            file (1).zip
```

Each file is now in its respective extension folder, so it's now easier to proceed with whatever task you want to do with those files.

## Advice 
  The best way to work with files is <b>ALWAYS</b> by making them safe first. To guarantee data loss prevention, make sure you have a backup before running the script. The code is projected to not allow those things to happen, but you'll never know. Enjoy! 😀
