FROM python:3.11
WORKDIR /backend
COPY . /backend
RUN pip3 install --upgrade pip -r requirements.txt
EXPOSE 5000
CMD python ./app.py