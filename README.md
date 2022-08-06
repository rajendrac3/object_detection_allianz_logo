# object_detection_allianz_logo

Task:
To detect Allianz logo from images using webservice

Solution:
1. Dataset: Manually downloaded images having allianz logo and prepared training and validation dataset by annotating them. Also performed augmentation to increase the number of images.

2. Training: Used yolov5 to train the model with 100 epochs

3. Inference: Created fastapi to perform inference on images

Results:
To test the model: run python fast_api_call.py.
This will start the webservice
You can upload image from postman using the endpoint: localhost:8000/upload with key as 'file' and value as image file

![all40](https://user-images.githubusercontent.com/22715882/183249644-5b01324c-2597-446e-a47c-bf2a4c2287e9.png)

![all37_0_rotate](https://user-images.githubusercontent.com/22715882/183249651-265526c0-675d-4bb8-9583-3c2f921ea58d.jpeg)
