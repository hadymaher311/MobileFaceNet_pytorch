from imutils import paths
import random
import sys

data_path = sys.argv[1]


images_paths = list(paths.list_images(data_path))
random.shuffle(images_paths)

labels = []
for image_path in images_paths:
    labels.append(image_path.split("/")[-2])

unique_labels = list(set(labels))

train_indeces = [unique_labels.index(x) for x in labels]

with open("./data/CASIA-WebFace-112X96.txt", "w+") as input_file:
    for i in range(len(images_paths)):
    	input_file.write(images_paths[i].split("/")[-2] + "/" + images_paths[i].split("/")[-1] + " " + str(train_indeces[i]) + "\n")
    	#if i > 1000:
    	#	break

with open("./data/map.txt", "w+") as input_file:
    for i in range(len(unique_labels)):
    	input_file.write(unique_labels[i] + " " + str(i) + "\n")

with open("./data/faces_count.txt", "w+") as input_file:
    input_file.write(str(len(unique_labels)) + "\n")
