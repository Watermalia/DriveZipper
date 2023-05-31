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
            if qbt_client.torrents_add(urls=magnet_link, save_path=os.path.join(os.getcwd(), "download"), tags="drivezipper") != "Ok.":
                raise Exception("Failed to add torrent.")
            for torrent in qbt_client.torrents_info(tags="drivezipper"):
                return torrent
    elif ddl_link:
        pass    # TODO Implement ddl support
    else:
        pass

def is_torrent_done():
    for torrent in qbt_client.torrents_info(tags="drivezipper"):
        if(torrent.state in ["uploading", "pausedUP", "stalledUP"]):
            return True
        return False
    
def get_torrent_hash():
    for torrent in qbt_client.torrents_info(tags="drivezipper"):
        return torrent.hash
    
def remove_torrent(delete_files, torrent_hash):
    with qbittorrentapi.Client(**conn_info) as qbt_client:
        qbt_client.torrents_delete(delete_files=delete_files, torrent_hashes=torrent_hash)