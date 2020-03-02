import cv2
img=cv2.imread("DualGAN/test/gt-haze-img_sz_256-fltr_dim_64-L1-lambda_AB_20.0_20.0/test_realB.jpg")
cv2.imshow("hazy",img)
img=cv2.imread("DualGAN/test/gt-haze-img_sz_256-fltr_dim_64-L1-lambda_AB_20.0_20.0/test_B2A.jpg")
cv2.imshow("dehazed",img)
cv2.waitKey()