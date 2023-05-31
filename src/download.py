import os
import qbittorrentapi

conn_info = dict(
    host="localhost",
    port=8080,
    username="admin",
    password="password",
)
qbt_client = qbittorrentapi.Client(**conn_info)

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

def download(magnet_link = None, ddl_link = None):
    if magnet_link:
        with qbittorrentapi.Client(**conn_info) as qbt_client:
            if qbt_client.torrents_add(urls=magnet_link) != "Ok.":
                raise Exception("Failed to add torrent.")
    elif ddl_link:
        pass    # TODO Implement ddl support
    else:
        pass