# P55 ⛏

<img src="https://img.shields.io/badge/version-1.2-red"> <img src="https://img.shields.io/badge/Python->=3.9.6-brightgreen"> <img src="https://img.shields.io/badge/feature-File%20organization-orange"> <img src="https://img.shields.io/badge/tools-utilities-blue">

<b><i>P55</i></b> is a bundle to center all files from a directory tree into a single folder and/or organize them by extension. The organization feature will be available soon! Meanwhile take a look at <a href="https://github.com/pzzzl/py-organizer">py-organizer</a>.

```python p55.py```

<details><summary><b>How it works?</b></summary>
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

The better way to do this is by using <b><i>P55</i></b>, making that task <i>easy as 1-2-3</i>.
</details>

<details><summary><b>Installation</b></summary>

  1. Download the file `extract.py` from this repository. You could also clone it using `git clone https://github.com/pzzzl/p55` if you have <a href="https://git-scm.com/">Git</a> installed.
  2. You'll need <a href="https://www.python.org/">Python</a> installed to run the script. The latest version was developed and tested in `Python 3.9.6`. After Python is installed you can check it's version with `python -V` on your console.
</details>

<details><summary><b>Advice</b></summary>
  The best way to work with files is <b>ALWAYS</b> by making them safe first. To guarantee data loss prevention, make sure you have a backup before running the script. The code is projected to not allow those things to happen, but you'll never know. Enjoy! 😀
</details>
