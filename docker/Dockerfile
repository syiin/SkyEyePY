FROM python:3

ADD skyeye.py /

RUN pip3 install numpy opencv-python

RUN apt update
RUN apt-get install -y --force-yes libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
RUN apt-get install -y --force-yes liblog4cplus-dev libcurl3-dev
RUN apt-get install -y --force-yes beanstalkd

RUN mkdir ~/openalpr

RUN cd ~/openalpr && git clone https://github.com/openalpr/openalpr.git

RUN cd ~/openalpr/openalpr/src && mkdir build && cd build && cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..

RUN cd ~/openalpr/openalpr/src/build && make && make install


RUN cd ~/openalpr/openalpr/src/bindings/python/ && python3 setup.py install

CMD [ "python3", "./skyeye.py" ]