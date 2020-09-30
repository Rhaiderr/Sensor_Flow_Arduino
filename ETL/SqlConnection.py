import sqlite3
from pathlib import Path


# Diretório raiz do projeto
def dire():
    return Path("__file__").parent.absolute()


def sql_conn():
    return sqlite3.connect(fr"{dire()}\Database\sensores.db")
