FROM python
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN apk add --update python3 py-pip
RUN pip install Flask
COPY . /app
WORKDIR /app
CMD ["python", "app"]
