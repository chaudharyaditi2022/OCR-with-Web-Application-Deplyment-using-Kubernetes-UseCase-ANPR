# OCR-with-Web-Application-Deplyment-using-Kubernetes-UseCase-ANPR-
Optical Character Recognition model(Labels [0-9] [A-Z]) is used to for Automatic Number Plate Recognition. To access this service a web application is provided which is deployed using Kubernetes.

##File Description
#1. Dockerfile
It contains the code for creating a docker image for our web application deployment. 
1. A numbered list
  1.Used tensorflow/tensorflow as base image.
  2.Created a Working Directory with location /var/ANPR_PROJECT
  3.Copied the contents of web application and requirements file in the
working directory
  4.Installed the required packages for opencv-python through apt-get
command
  5.Installed the required python packages
  6.Created an Entrypoint to run the web application back-end file.
  7.Expose port 80 

