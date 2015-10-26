#!/usr/bin/env python
#using the Facebook SDK for Python
import facebook
import requests
import sys
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
#access_token = ''
access_token = sys.argv

graph = facebook.GraphAPI(access_token, version='2.2')
print (graph.version)

# Return all connected photos for me. 
# By default, reading from the photos edge includes all photos a person has been tagged in.
photosedge = graph.get_connections(id='me', connection_name='photos')


#for each object in photosedge print the img source url and unique photo id
for p in photosedge['data']:	
	url = (p['source'])
	print(url)
	id = (p['id'])
	print(id)
	filepath = id  + '.jpg'
	#filepath = '/cygdrive/c/Users/sean/photoframe/' + id  + '.jpg'
	#filepath = '/home/pi/photoframe/fb/' + id  + '.jpg'
	print(filepath)
	r = requests.get(url)
	print(r.status_code)	
	try:
		image_file = open(filepath, 'wb')
	except IOError:		
		image_file = open(filepath, 'wb')
		image_file.write(r.content)
		image_file.close()

	#image_file = open(filepath)
        #print ("---> Already have file")
    	#except IOError:
        #print ("---> Downloading %s" % url)

    
    

#TODO
# use the Linux framebuffer app to render the image
# sample: fbi -noverbose -m 640x480 -a -u -t 6 /home/pi/art/**/*

# use the links2 browser to render the img urls