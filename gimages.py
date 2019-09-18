from google_images_download import google_images_download   #importing the library
import requests
import urllib3
urllib3.disable_warnings()
response = google_images_download.googleimagesdownload()
v1 = input('Enter a search term : ')
arguments = {"keywords":v1,"limit":20,"print_urls":True}
path = response.download(arguments)
