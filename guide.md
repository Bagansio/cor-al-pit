# Installation

Install the environment:

REQUIREMENTS:

- Python3
- Pref. Linux (Virtual, WSL, ...)
- Theseract (https://tesseract-ocr.github.io/)

- .env file (with variable: TESSERACT_EXE=<path_to_theseract.exe>)



```sh
#In project root dir use
python3 -m venv venv
source ./$virtual_name/bin/activate

pip install -r ./requirements.txt

```

<br>


# Use

You need to activate the environment:

```sh
source ./.venv/bin/activate

#after that you will see something like:
(.env) bagansio@Bagansio: 

----

python main.py

#If you want to deactivate the environment, just use:
deactivate
```
