# wifi-logger

### Purpose

Log wifi availability every minute and generate dataset for use with Visavail.js (Time Data Availability Chart) - https://github.com/flrs/visavail

### Setup:

* Requires Python and Git installations

* cd ~ && git@github.com:tylerhekman/wifi-logger.git

* (crontab -l 2>/dev/null; echo "* * * * * ~/wifi-logger/internet.sh $(which wget)") | crontab -