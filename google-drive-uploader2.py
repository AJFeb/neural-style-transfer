import json
import requests
import yaml
import os

CONFIGS = ["configs/comics_upload.yaml", "configs/movie_upload.yaml"]

ACCESS_TOKEN = "ya29.a0AfH6SMDGBgPa2FqGCfM6IB4nsUgFTud-d8iNMJn5dhARwUr-eGS5gmRE9IB96X3eGkPjCy8zUbYZbQ446M3O8cczVxfRMrvN9BGRRj2htXEUcrU_5x39NBFJjeT3XS1dcmoOKFiFH4GdQPLNvlsuEAPfj0GIssJP_9gKOZybbv4"

HEADERS = {"Authorization": "Bearer "+ACCESS_TOKEN}

def upload_images(config_file_name):
    
    config_file = open(config_file_name, 'r')
    configs = yaml.load(config_file, Loader=yaml.FullLoader)

    image_dir = configs['image_dir']
    upload_dir = configs['upload_dir']

    os.chdir(str(image_dir))

    file_list = os.listdir()

    for image in file_list:
        para = {
            "name": str(image), #file name to be uploaded
            "parents": [str(upload_dir)] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
        }
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': ('image/jpeg',open("./"+str(image), "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=HEADERS,
            files=files
        )
    #os.chdir('..')
     
def main():
    for config_file_name in CONFIGS:
        upload_images(config_file_name)

if __name__ == '__main__':
     main()

#print(os.listdir('images/comics'))