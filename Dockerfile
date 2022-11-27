FROM python
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN pip3 install Flask
COPY . /app
WORKDIR /app
CMD ["python3", "app"]
