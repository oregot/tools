#!/usr/bin/python

#import urllib2
import urllib
#import httplib
import socket
import requests
import time
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


JB_PUBLIC_HOST='192.168.200.57'
JB_HTTPS_PORT='4601'


url = "https://{0}:{1}".format(JB_PUBLIC_HOST,JB_HTTPS_PORT)



JB_PUBLIC_HOST2='192.168.200.58'
url2 = "https://{0}:{1}".format(JB_PUBLIC_HOST2,JB_HTTPS_PORT)


def check_url(url):


    try:
        r = requests.get(url, verify=False)
    except:
        code = "404"
    else:
        code=r.status_code
    return code
#print check_url(url)

status1=0
status2=0
while True:
#    print(chr(27) + "[2J")
#    os.system('clear')
    status_s1=check_url(url)
    status_s2=check_url(url2)

    if status_s1 == 200 and status_s1 != status1:
        print  time.strftime('%H:%M:%S') , bcolors.BOLD +url + bcolors.ENDC, bcolors.OKGREEN +  str(status_s1) + bcolors.ENDC
    elif status_s1 == str(404) and status_s1 != status1:
        print  time.strftime('%H:%M:%S') , bcolors.BOLD +url + bcolors.ENDC, bcolors.FAIL +  str(status_s1) + bcolors.ENDC

    if status_s2 == 200 and status_s2 != status2:
        print  time.strftime('%H:%M:%S') , bcolors.BOLD +url2 + bcolors.ENDC, bcolors.OKGREEN +  str(status_s2) + bcolors.ENDC
    elif status_s2 == str(404) and status_s2 != status2:
        print  time.strftime('%H:%M:%S') , bcolors.BOLD +url2 + bcolors.ENDC, bcolors.FAIL +  str(status_s2) + bcolors.ENDC
    status1=status_s1
    status2=status_s2
#    print  time.strftime('%H:%M:%S') , bcolors.BOLD +url + bcolors.ENDC, check_url(url), "\t", url2, check_url(url2)
    time.sleep(1)
