import os
from qbittorrent import Client

qb = Client('http://127.0.0.1:8080/')
username = 'admin'
password = 'password'

def download(magnet_link = None, torrent_file_path = None):
    qb.login(username, password)
    if magnet_link:
        qb.download_from_link(magnet_link)
    elif torrent_file:
        torrent_file = open(torrent_file_path, 'rb')
        qb.download_from_file(torrent_file)
    else:
        pass