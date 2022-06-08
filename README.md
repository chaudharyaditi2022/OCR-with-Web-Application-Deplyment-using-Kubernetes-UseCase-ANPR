# OCR-with-Web-Application-Deplyment-using-Kubernetes-UseCase-ANPR
Optical Character Recognition model(Labels [0-9] [A-Z]) is used to for Automatic Number Plate Recognition. To access this service a web application is provided which is deployed using Kubernetes.

## File Description
### 1. Dockerfile
It contains the code for creating a docker image for our web application deployment. 
- Used tensorflow/tensorflow as base image.
- Created a Working Directory with location /var/ANPR_PROJECT
- Copied the contents of web application and requirements file in the working directory
- Installed the required packages for opencv-python through apt-get
command
- Installed the required python packages
- Created an Entrypoint to run the web application back-end file.
- Expose port 80 

To build Dockerfile run the following command
` docker build -t <image_name> <path_to_Dockerfile>`


 ### 2. minikube-commands.txt
 It contains the commands for web application deployment using minikube cluster.
 Prerequisites - 
 - Install Minikube and kubectl- 
    - Installation documentation : https://kubernetes.io/docs/tasks/tools/install-minikube/
    - Link to install minikube: https://storage.googleapis.com/minikube/releases/latest/minikube-installer.exe
    - Command to install kubectl:
    ` curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.20.0/bin/windows/amd64/kubectl.exe `
 - Run minikube-installer.exe
 - Install oracle virtualbox and run it.
 - To start minikube cluster open command prompt with Administrator power and run the following command.
 ` minikube start --driver=virtualbox `
 - Run the commands given in minikube-commands.txt

### 3. requirements.txt
It contains the python packages needed by our OCR model and are installed in the final Image when Dockerfile is built.

### 4. ANPR/AlphaNumericCharacterRecognition30x30 (1).h5
It is our OCR model which is saved in this file and used for character recognition.

### 5. ANPR/Alphanumeric_Character_Recognition_CNN.ipynb
This is the python file which contains code for creation of our CNN model.

### 6. ANPR/Character_Recognition.py
This file contains the functions for image preprocessing which are needed before feeding image to our OCR Model.

### 7. ANPR/haarcascade_car.xml
Pre-built Haarcascade model for car detection.

### 8. ANPR/indian_license_plate.xml
Pre-built Haarcascade model for indian nameplate detection.

### 9. ANPR/main.py
This file contains the web application back-end code. We have used flask framework.
After getting input from web application, flask routes it to upload_image() function.
This function saves the image file in “static/images/” [kindly note the location of this folder in this file]  folder and then passes the saved Image through the user-defined image preprocessing functions and then finally passes it to OCR Model.  After getting the Vehicle information from the API. 
It redirects to the same page with the give output.

### 10. ANPR/templates/main.html
This file contains the web application front-end code. The Web application consists of one form which takes an image file as input.

### 11. ANPR/static/Images
This folder is used to save the images fed by the user as input on web page.


Thank you!!






 
 
 
 
 
 

