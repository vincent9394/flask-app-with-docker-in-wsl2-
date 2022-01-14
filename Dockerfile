FROM python
WORKDIR /var/www/
ENV REDIRECT_TO=https://digitalocean.com/community/tutorials
COPY ./app.py /var/www/app.py
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
CMD python3 app.py
