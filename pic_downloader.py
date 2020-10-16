'''
Usage: python scrape_marathon_images --fname <filepath of the img_pg_links CSV>
'''

# import the necessary packages
from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import os
import argparse

#Define the argument parser to read in the URL
parser = argparse.ArgumentParser()
parser.add_argument('-fname', '--fname', help='CSV of image links')
args = vars(parser.parse_args())
f_name = args['fname']

# Create the directory name where the images will be saved
base_dir = os.getcwd()
dir_name = (f_name.split('/')[-1]).split('.')[0]
dir_path = os.path.join(base_dir, dir_name)

#Create the directory if already not there
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Read the csv with links to all the image pages
f = open(os.path.join(base_dir, f_name),'r')
links = f.read().split(',')

# Print the number of images
print ("[INFO] Downloading {} images".format(len(links)))

# Function to take an image url and save the image in the given directory
def download_image(url):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    urllib.request.urlretrieve(url,os.path.join(dir_path, name))

for href in links:
    # Extract the contents of the link
    img_page = requests.get(href)
    soup = bs(img_page.content, 'html.parser')
    img_class = soup.find_all('meta', attrs={"name":"twitter:image"})
    img_url = img_class[0].get('content')
    real_url = img_url.replace('XL', 'X3', 2)
    download_image(real_url)
