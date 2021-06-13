FROM ubuntu
RUN apt-get update
RUN apt-get install -y tzdata
ENV TZ=Europe/ETC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y apache2
RUN apt-get install -y apache2-utils
RUN apt-get clean
RUN sed -i 's/Listen 80/Listen 8081/g' /etc/apache2/ports.conf
RUN sed -i 's/<VirtualHost *:80>/<VirtualHost *:8081>/g' /etc/apache2/sites-enabled/000-default.conf
COPY index.html /var/www/html/
EXPOSE 8081
CMD ["apache2ctl", "-D", "FOREGROUND"]

