import os
import urllib.request
import zipfile
import sys

BASE_URL = "https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/"
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

FILES = [
    "GTSRB-Training_fixed.zip",
    "GTSRB_Final_Test_Images.zip",
    "GTSRB_Final_Test_GT.zip"
]

def download_file(filename):
    dest_path = os.path.join(DATA_DIR, filename)
    if os.path.exists(dest_path):
        print(f"[OK] {filename} already downloaded.")
        return dest_path
    
    url = BASE_URL + filename
    print(f"Downloading {filename} from {url}...")
    
    def reporthook(blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = f"\rDownloading {filename}: {percent:5.1f}% ({readsofar / 1e6:.1f} MB / {totalsize / 1e6:.1f} MB)"
            sys.stdout.write(s)
            sys.stdout.flush()
        else:
            sys.stdout.write(f"\rDownloading {filename}: {readsofar / 1e6:.1f} MB")
            sys.stdout.flush()

    urllib.request.urlretrieve(url, dest_path, reporthook)
    print(f"\n[DONE] Downloaded {filename}")
    return dest_path

def extract_file(zip_path):
    print(f"Extracting {os.path.basename(zip_path)}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(DATA_DIR)
    print(f"[DONE] Extracted {os.path.basename(zip_path)}")

if __name__ == "__main__":
    for f in FILES:
        zip_p = download_file(f)
        extract_file(zip_p)
    print("All GTSRB files downloaded and extracted to:", DATA_DIR)

