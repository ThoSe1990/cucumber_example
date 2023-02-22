FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install build-essential -y
RUN apt-get install gdb -y
RUN apt-get install git -y
RUN apt-get install cucumber -y
RUN apt install npm -y
RUN apt install python3-pip -y
RUN pip3 install cmake 
RUN pip3 install conan==1.57.0

RUN conan profile new default --detect
RUN conan profile update settings.compiler.libcxx=libstdc++11 default

CMD ["bash"]
