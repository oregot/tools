#!/usr/bin/python

import urllib
import socket
import requests
import time
import os
import sys
import sqlite3

conn = sqlite3.connect('checker.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS logs")
c.execute("CREATE TABLE Logs(Id INT, Name TEXT, Status INT, TIMESTAMP)")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) == 1:
    raise NameError('There are not any servers as parameters')


port='4601'
status = 0

def check_url(url):
    try:
        r = requests.get(url, verify=False)
    except:
        code = "404"
    else:
        code=r.status_code
    return code

statusd={}


while True:
    for server in sys.argv[1:]:
        url = "https://{0}:{1}".format(server,port)
        status=check_url(url)
        if server not in statusd.keys():
            statusd[server] = 0
        if status == 200 and status != statusd[server]:
            print  time.strftime('%H:%M:%S') , bcolors.BOLD + url + bcolors.ENDC, bcolors.OKGREEN +  str(status) + bcolors.ENDC
            c.execute("INSERT INTO logs values (?, ?, ?, ?)", (1, url, status, time.strftime('%H:%M:%S')))
            conn.commit()

        elif status == 404 and status !=  statusd[server]:
            print  time.strftime('%H:%M:%S') , bcolors.BOLD + url + bcolors.ENDC, bcolors.FAIL +  str(status) + bcolors.ENDC
            c.execute("INSERT INTO logs values (?, ?, ?, ?)", (1, url, status, time.strftime('%H:%M:%S')))
            conn.commit()

        statusd[server] = status
    time.sleep(1)

