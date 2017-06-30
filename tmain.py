import threading
import sys
import os
import sqlite3
import time

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

dbfile = "./mydb.db"

def create_db():

    if os.path.isfile(dbfile):
        os.remove(dbfile)

    with sqlite3.connect(dbfile) as c:
        try:
            c.execute('''CREATE TABLE mytable
                    (Time DATETIME, Id INTEGER, remark VARCHAR(12))''')
        except Exception as ex:
            print (ex)
            exit(1)

def inserter(id):
    with sqlite3.connect(dbfile) as conn:
        try:
            conn.execute("INSERT INTO mytable VALUES(%d, %d, '%s')" % (time.time(), id, "aaa"))
        except Exception as ex:
            print(ex)


def main(ids):
    create_db()
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(inserter, id) for id in ids]
    for future in as_completed(futures):
        print(future.result())


if __name__ == "__main__":
    ids = range(1,2000)
    main(ids)


