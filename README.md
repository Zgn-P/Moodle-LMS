# Moodle-LMS
Developing a LMS module for L&D team with Moodle and MariaDB

need to configure nginx, go to compose file and add:
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
---------------------------------------------------------------

Can also setup phpAdmin within moodle service @compose:
   phpmyadmin:
      image: docker.io/bitnami/phpmyadmin:5
      container_name: phpmyadmin
      ports:
        - '81:8080'
        - '444:8443'
      depends_on:
        - mariadb
      networks:
        - xyz
---------------------------------------------------------------

For error handling @infra:
  https://github.com/bitnami/containers/blob/main/bitnami/moodle/4.2/debian-11/rootfs/opt/bitnami/scripts/libmoodle.sh#L200

After infra setup, LDAP configuration:
    Site administration >> Plugins >> enrollment >> LDAP authentication : (true)
    Site administration >> Plugins >> Authentication >> LDAP server : configure Host url and context

----------------------------------------------------------------

Ad-hoc database queries: Creates view either run on demand, or scheduled to run automatically

Webinar Plugin:
The Webinar activity module includes the following functionality:
	Add/edit/delete webinar session
	Assign a host user to a session - based on 'teacher' system role
	Register for session / assign students to a session
	Unregister for session / unassign students from a session
	Automated email notifications to registered students
	Join session
	View / record webinar
	Run attendance report

LDAP Sync Plugin:
	LDAP PLUS: https://moodle.org/plugins/auth_ldap_syncplus/v3.0-r3/10842
	Doc: https://docs.moodle.org/403/en/LDAP_authentication
	MS AD


things to look into: 
	Open to all enrollement(course enrollment)
	sequential course
	corporate structure
	Certify'em


