import sqlite3
from pathlib import Path


# Diretório raiz do projeto
def dir():
    return Path("__file__").parent.absolute()


def sql_conn():
    return sqlite3.connect(fr"{dir()}\Database\sensores.db")
