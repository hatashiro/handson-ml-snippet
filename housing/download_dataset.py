import os
import tarfile
from constants import DIR_PATH, TGZ_PATH, DOWNLOAD_URL
from six.moves import urllib

def fetch_housing_data():
    if not os.path.isdir(DIR_PATH):
        os.makedirs(DIR_PATH)
    urllib.request.urlretrieve(DOWNLOAD_URL, TGZ_PATH)
    tgz = tarfile.open(TGZ_PATH)
    tgz.extractall(path=DIR_PATH)
    tgz.close()

fetch_housing_data()
