#rm -f /Users/Sanjay/Documents/CDSAML_Project/DualGAN/datasets/gt-haze/val/B/*.jpg
cd video
python3 video_split.py
rscript classify.r
cp -R frames4foggy/*.jpg ../DualGAN/datasets/gt-haze/val/B
cd ../DualGAN
python3 main.py --phase test --dataset_name gt-haze --image_size 256 --epoch 20 --lambda_A 20.0 --lambda_B 20.0 --A_channels 3 --B_channels 3
mv test/gt-haze-img_sz_256-fltr_dim_64-L1-lambda_AB_20.0_20.0/frame*_B2A.jpg ../video/frames4clear
cd ../video/frames4clear
rename "s/_B2A.jpg/.jpg/" frame*.jpg
cd ..
python3 frames_to_video.py
python3 play_video.py