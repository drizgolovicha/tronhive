import sqlite3
import requests
from datetime import datetime


conn = sqlite3.connect("db/db")


def insert(balance: int):
    q = "insert into balance (balance, datetime) values ({:d}, {:d})".format(balance, int(datetime.timestamp(datetime.now())))

    try:
        cursor = conn.cursor()
        cursor.execute(q)
        conn.commit()
    except BaseException as e:
        print(str(e))


def getBalance() -> int:
    """
    get balance from tronscan
    :return: int
    """
    url = "https://apilist.tronscan.org/api/account?address=TLkyqyLBhLqYC3tvMRb41RmcudGSbxXYUH"
    r = requests.get(url)

    if r.ok:
        return r.json().get("balance")
    else:
        raise Exception("cannot get balance")


if __name__ == "__main__":
    insert(getBalance())
