from google_images_search import GoogleImagesSearch

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyAJq0IAvV9rfCjtNUmjb_tdcTxGj-4VZFM', '18a3ed03f69d15370')

# define search params:
_search_params = {
    'q': 'joker comic art',
    'num': 10,
    #'safe': 'high',
    'fileType': 'jpg',
    #'imgType': 'photo',
    #'imgSize': 'MEDIUM',
    #'imgDominantColor': 'white',
}


# this will only search for images:
#gis.search(search_params=_search_params)

# this will search and download:
gis.search(search_params=_search_params, path_to_dir='/Users/AndrewFebrillet/Documents/Post-Grad/Fall 2020/neural-style-transfer/img_links')

# this will search, download and resize:
#gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards:
# gis.search(search_params=_search_params)
# for image in gis.results():
#   image.download('/Users/AndrewFebrillet/Documents/Post-Grad/Fall 2020/neural-style-transfer/img_links')
#	image.resize(500, 500)

    