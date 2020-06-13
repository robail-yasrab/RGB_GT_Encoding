from glob import glob
import os
from PIL import Image
import numpy as np
import cv2


files = glob(".././*.png") ## add path to your RGB colored Ground Truth Folder
i= len(files)
print (i)
def closetRGB(rgb_pixels):
    rgb_pixels = np.array(rgb_pixels)
    print (rgb_pixels)

    colourset = np.array([[0,0,0], [255,0,0],[255,0,255],[0,255,0], [0,255,255],[255,255,255]])  
    #List all colors present in your RGB visible Color Ground truth; in the case of RootNav 2.0, we have these color present (GT extracted from RSML to Annotation code). 

    closest = np.inf
    for i, colours in enumerate(colourset):
        d = np.sqrt(
              ((colours[0] - rgb_pixels[0]) *  (colours[0] - rgb_pixels[0]))
            + ((colours[1] - rgb_pixels[1]) *  (colours[1] - rgb_pixels[1]))
            + ((colours[2] - rgb_pixels[2]) *  (colours[2] - rgb_pixels[2]))
                                              )
        if d < closest:
            indx = i
            closest = d

    return indx



if __name__ == '__main__':

    for x in range(0, i):
        fn = files[x] 
        filename = os.path.basename(fn)
        print (filename)
        
        
        img = cv2.imread(fn)
        Z = img.reshape((-1,3))

        # convert to np.float32
        Z = np.float32(Z)

        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 7
        ret,label,center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))

        unique_pixels = np.vstack({tuple(r) for r in res2.reshape(-1, 3)})

        for rgb_pixels in unique_pixels:

            ind = closetRGB(rgb_pixels)

            res2[np.where((res2 == rgb_pixels).all(axis=2))] = [ind, ind, ind]
 
        cv2.imwrite('.././'+filename, res2) ## add path to your output folder where new RGB colored Ground Truth Folder will be stored 

        print (np.unique(res2))





 
