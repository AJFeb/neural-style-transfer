from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import yaml
import os


# Below code does the authentication 
# part of the code 
gauth = GoogleAuth()
# Creates local webserver and auto 
# handles authentication. 
gauth.LocalWebserverAuth()        
drive = GoogleDrive(gauth) 
    

CONFIGS = ["configs/comics_upload.yaml", "configs/movie_upload.yaml"]


def upload_images(config_file_name):
    config_file = open(config_file_name, 'r')
    configs = yaml.load(config_file, Loader=yaml.FullLoader)

    path = r"."+configs['image_path']
    drive_dir = configs['drive_dir']


    for image in os.listdir(path): 

        f = drive.CreateFile({"title": image, "parents": [{"id": drive_dir, "kind": "drive#childList"}]}) 
        f.SetContentFile(os.path.join(path, image)) 
        f.Upload()
        print(image) 
      
        # Due to a known bug in pydrive if we  
        # don't empty the variable used to 
        # upload the files to Google Drive the 
        # file stays open in memory and causes a 
        # memory leak, therefore preventing its  
        # deletion 
        f = None

def main():
    for config_file_name in CONFIGS:
        upload_images(config_file_name)

if __name__ == '__main__':
     main()

#hi Hanyang
