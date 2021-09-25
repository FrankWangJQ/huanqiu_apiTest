import time

from httprunner import __version__
import requests
import datetime

def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def getParentId(base_url,num):
    r=requests.get(base_url+"/organizationUnit/list")
    return r.json()['data'][num]['parentId']

def getTomorrowDate():
    return datetime.date.today() + datetime.timedelta(1)