# python image
FROM public.ecr.aws/lambda/python:3.8

# make the dir
RUN mkdir -p /app

# copy files
COPY app.py /app/
COPY Makefile /app/
COPY klargest.py /app/
COPY test_app.py /app/
COPY requirements.txt /tmp/requirements.txt

# install all packages
RUN pip install -r /tmp/requirements.txt

# set working dir
WORKDIR /app

# expose to ports
EXPOSE 80
EXPOSE 8080

# entry point
ENTRYPOINT [ "python" ]
CMD [ "/app/app.py" ]