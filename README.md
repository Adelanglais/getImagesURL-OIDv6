# getImagesURL - OIDv6
This code allows you to access image URLs in OpenImages Dataset with a single command line.

## Installation 
_Python3 is required_
1. Clone this repository
```bash
git clone https://github.com/Adelanglais/getImagesURL-OIDv6
```
2. In the **same** repository, download the followings files and put it in a csv_fils repository
* https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv
* https://appen.com/datasets/open-images-annotated-with-bounding-boxes/#download-preview-1
* https://storage.googleapis.com/openimages/2018_04/image_ids_and_rotation.csv

3. Installed the required packages
```bash
pip3 install -r requirements.txt
```
## Utilisation
```bash
python3 getImagesUrl.py getURL
```
**Arguments**
* **--classes**: Name of the class you want
* **--limit**: number of image's URL you want


