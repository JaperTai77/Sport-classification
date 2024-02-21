# 
FROM python:3.11

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./code /code/app

# 
CMD ["python", "app/main.py"]

#
ENV http_proxy=http:...
#
ENV https_proxy=http:...
#
RUN sudo apt-get install libav-tools
#
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
