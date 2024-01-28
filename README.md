# Moodle-LMS
Developing a LMS module for L&D team with Moodle and MariaDB

>>need to configure nginx, go to compose file and add:
  nginx:
        image: nginx
        depends_on:
            - moodle
        ports:
            - 127.0.0.1:8080:80
        volumes:
            - /home/data/FQDN/nginx:/etc/nginx/conf.d
            - /home/data/FQDN/src:/var/www/html
        restart: unless-stopped

>> Can also setup phpAdmin within moodle service @compose:
   phpmyadmin:
      image: docker.io/bitnami/phpmyadmin:5
      container_name: phpmyadmin
      ports:
        - '81:8080'
        - '444:8443'
      depends_on:
        - mariadb
      networks:
        - cfyd



>>For error handling @infra:
  https://github.com/bitnami/containers/blob/main/bitnami/moodle/4.2/debian-11/rootfs/opt/bitnami/scripts/libmoodle.sh#L200

After infra setup, LDAP configuration:
    Site administration >> Plugins >> enrollment >> LDAP authentication : (true)
    Site administration >> Plugins >> Authentication >> LDAP server : configure Host url and context


