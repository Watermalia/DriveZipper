import os
from qbittorrent import Client

qb = Client('http://127.0.0.1:8080/')
username = 'admin'
password = 'password'

def download(magnet_link = None, ddl_link = None):
    qb.login(username, password)
    if magnet_link:
        qb.download_from_link(magnet_link)
    elif ddl_link:
        pass    # TODO Implement ddl support
    else:
        pass