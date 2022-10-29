import cv2
import os

# System variables
sep = os.sep


# Load images
path1 = os.path.dirname(os.getcwd())
path = os.path.join(path1, "Input"+sep)
files = os.listdir(path)
outputpath = os.path.join(path1, "Output"+sep)

filesInDir = []
for f in files:
    filesInDir.append(os.path.join(path, f))

files = filesInDir

image_paths = ['1.jpg', '2.jpg', '3.jpg']
image_paths = files
print(files)
# initialized a list of images
imgs = []

for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    imgs[i] = cv2.resize(imgs[i], (0, 0), fx=0.4, fy=0.4)
    # this is optional if your input images isn't too large
    # you don't need to scale down the image
    # in my case the input images are of dimensions 3000x1200
    # and due to this the resultant image won't fit the screen
    # scaling down the images
# showing the original pictures
    #cv2.imshow(str(i+1), imgs[i])


stitchy = cv2.Stitcher.create()
(dummy, output) = stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
    # checking if the stitching procedure is successful
    # .stitch() function returns a true value if stitching is
    # done successfully
    print("stitching ain't successful")
else:
    print('Your Panorama is ready!!!')

# final output
cv2.imshow('final result', output)
cv2.imwrite(os.path.join(outputpath, "Output.jpg"), output)
cv2.waitKey(0)
