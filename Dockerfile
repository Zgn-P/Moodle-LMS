FROM Ubuntu:latest
RUN apt-get update && apt-get install

WORKDIR ./app
EXPOSE 8080
