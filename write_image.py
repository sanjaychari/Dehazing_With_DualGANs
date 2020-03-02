import cv2
f=open("input_image.txt","r")
image_path=f.read()
print(image_path)
img = cv2.imread(image_path)
#image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow(image)
cv2.imwrite("/Users/Sanjay/Documents/CDSAML_Project/DualGAN/datasets/gt-haze/val/B/test.jpg",img)