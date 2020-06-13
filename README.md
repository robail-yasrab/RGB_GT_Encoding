# RGB_GT_Encoding

In RootNav 2.0, if you use Cross-Entropy Loss for segmentation, you may encounter a Loss error (due to high RGB color encodings (e.g. [255,0,0]) ). To resolve that error, this script to generate RGB encoded ground truth (GT). This encoding will encode GT by giving each class a single pixel value (e.g., 0, 1, 2....). The resultant GT will look blank, but if you open those GTs in paint and drop any color, it will contain each given set of classes. 



### Usage
1- Edit the input color class according to you earlier colored GT.  
```
colourset = np.array([[0,0,0], [255,0,0],[255,0,255],[0,255,0], [0,255,255],[255,255,255]])  
#List all colors present in your RGB visible Color Ground truth; in the case of RootNav 2.0, we have these color present (GT extracted from RSML to Annotation code). 
```
2- Set input GT images directory: 
```
files = glob(".././*.png") ## add path to your RGB colored Ground Truth Folder and input image type 
```
3- Set output GT images directory: 
```
cv2.imwrite('.././'+filename, res2) ## add path to your output folder where new RGB colored Ground Truth Folder will be stored
```
4- Run File 
```
python RGB_anno.py
```

