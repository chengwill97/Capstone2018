import os

os.system('mkdir classified_images')

class_names = ['crabeater', 'weddel', 'packi-ice', 'other']

for x in class_names:
	dir = './classified_images/' + x
	os.mkdir(dir)
	#%mkdir -v $dir

