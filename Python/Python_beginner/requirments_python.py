"""
aiohttp                3.8.6
aiosignal              1.3.1
annotated-types        0.6.0
anyio                  3.7.1
asttokens              2.2.1
async-timeout          4.0.3
attrs                  23.1.0
autopep8               1.7.0
backcall               0.2.0
BareNecessities        0.2.8
beautifulsoup4         4.12.2
blinker                1.7.0
certifi                2023.7.22
cffi                   1.16.0
chardet                5.2.0
charset-normalizer     3.3.0
click                  8.1.7
colorama               0.4.6
comm                   0.1.2
cryptography           41.0.5
debugpy                1.6.5
decorator              5.1.1
distlib                0.3.7
dnspython              2.4.2
docutils               0.20.1
email-validator        2.1.0.post1
entrypoints            0.4
et-xmlfile             1.1.0
exceptiongroup         1.1.3
executing              1.2.0
fastapi                0.104.1
filelock               3.12.4
Flask                  3.0.0
Flask-Mail             0.9.1
frozenlist             1.4.0
h11                    0.14.0
httpcore               1.0.2
httptools              0.6.1
httpx                  0.25.1
idna                   3.4
ipykernel              6.20.1
ipython                8.8.0
itsdangerous           2.1.2
jedi                   0.18.2
Jinja2                 3.1.2
jupyter_client         7.4.9
jupyter_core           5.1.3
Kivy                   2.2.1
kivy-deps.angle        0.3.3
kivy-deps.glew         0.3.1
kivy-deps.sdl2         0.6.0
Kivy-Garden            0.1.5
lxml                   4.9.3
Mail                   2.1.0
MarkupSafe             2.1.3
matplotlib-inline      0.1.6
multidict              6.0.4
mysql                  0.0.3
mysql-connector-python 8.2.0
mysqlclient            2.2.0
nest-asyncio           1.5.6
numpy                  1.26.1
openai                 0.28.1
openpyxl               3.1.2
orjson                 3.9.10
packaging              23.0
pandas                 2.1.2
parso                  0.8.3
pickleshare            0.7.5
pip                    23.3.1
platformdirs           3.11.0
prettytable            3.9.0
prettyTables           1.1.5
prompt-toolkit         3.0.36
protobuf               4.21.12
psutil                 5.9.4
pure-eval              0.2.2
pycodestyle            2.9.1
pycparser              2.21
pydantic               2.5.1
pydantic_core          2.14.3
pydantic-extra-types   2.1.0
pydantic-settings      2.1.0
Pygments               2.14.0
PyPDF2                 3.0.1
pypiwin32              223
PyQt5                  5.15.10
PyQt5-Qt5              5.15.2
PyQt5-sip              12.13.0
python-dateutil        2.8.2
python-docx            1.1.0
python-dotenv          1.0.0
python-multipart       0.0.6
pytz                   2023.3.post1
pywin32                305
PyYAML                 6.0.1
pyzmq                  25.0.0
requests               2.31.0
setuptools             58.1.0
six                    1.16.0
sniffio                1.3.0
soupsieve              2.5
spark-parser           1.8.9
stack-data             0.6.2
starlette              0.27.0
toml                   0.10.2
torado                 0.0.2
tornado                6.2
tqdm                   4.66.1
traitlets              5.8.1
typing_extensions      4.8.0
tzdata                 2023.3
ujson                  5.8.0
uncompyle6             3.9.0
urllib3                2.0.6
uvicorn                0.24.0.post1
virtualenv             20.24.5
watchfiles             0.21.0
wcwidth                0.2.5
websockets             12.0
Werkzeug               3.0.1
xdis                   6.0.5
yarl                   1.9.2


echo off

"""


"""
# /*up to date 20.11.2023


#1-to create virtual enve,
python -m venv name_virtualenv (venv name optional)
#2-activate  =>
venv\Scripts\activate
#if error => need to unrestrict  exception policy after activate should again restricted activate !!!!!
# to acitvate excettion step  1 check
Get-ExecutionPolicy
#if restricted :  step 2 unrestrict
Set-ExecutionPolicy RemoteSigned
#now u can activate Virtual env and if u finish activate : step 3 restricted ==>
Set-ExecutionPolicy Restricted


# save installation file sin a text file for the futur instalation ==>
pip freeze > requirments.txt

# to use in another project need to deactivate Virtual env .and than

#open directory where is exist the file ,  or chage directory to needed location for install =>
pip install -r name_file.txt


"""

