FROM tensorflow/tensorflow
WORKDIR /var/ANPR_PROJECT/
COPY requirements.txt /var/ANPR_PROJECT/requirements.txt
COPY ./Flask/ANPR /var/ANPR_PROJECT
RUN echo 'Y' | apt-get install libgl1 libglib2.0-0
RUN pip3 install -r /var/ANPR_PROJECT/requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py" ]
EXPOSE 80




