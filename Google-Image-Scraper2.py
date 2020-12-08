from google_images_search import GoogleImagesSearch
from pathlib import Path
import yaml

CONFIGS = ["configs/comics.yaml", "configs/movie_phoenix.yaml"]

def get_images(gis, config_file_name):
	config_file = open(config_file_name, 'r')
	configs = yaml.load(config_file, Loader=yaml.FullLoader)

	_search_params = configs['params']
	out_dir = configs['out_dir']
	print("params: ", _search_params)
	print("image download path: ", out_dir)

	# this will only search for images:
	#gis.search(search_params=_search_params)

	# this will search and download:
	# gis.search(search_params=_search_params, path_to_dir='images/')

	# create the dir if it does not exist
	Path(out_dir).mkdir(parents=True, exist_ok=True)
	# this will search, download and resize:
	gis.search(search_params=_search_params, path_to_dir=out_dir, width=256, height=256)

	# search first, then download and resize afterwards:
	# gis.search(search_params=_search_params)
	# for image in gis.results():
	#   image.download('/Users/AndrewFebrillet/Documents/Post-Grad/Fall 2020/neural-style-transfer/img_links')
	#	image.resize(500, 500)

def main():

	# you can provide API key and CX using arguments,
	# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
	gis = GoogleImagesSearch('AIzaSyAJq0IAvV9rfCjtNUmjb_tdcTxGj-4VZFM', '18a3ed03f69d15370')
	for config_file_name in CONFIGS:
		get_images(gis, config_file_name)

if __name__ == '__main__':
	main()
    
