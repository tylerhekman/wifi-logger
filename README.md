# wifi-logger

Setup:

Install python

cd ~ && git@github.com:tylerhekman/wifi-logger.git
(crontab -l 2>/dev/null; echo "* * * * * ~/wifi-logger/internet.sh $(which wget)") | crontab -