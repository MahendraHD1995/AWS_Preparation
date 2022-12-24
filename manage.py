#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AWS_Preparation.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



# python manage.py startapp appname => create a Django app
# python manage.py runserver




# sudo systemctl status jenkins
# sudo systemctl enable --now jenkins
# sudo ufw allow 8080
# sudo ufw status
# sudo ufw enable
# http://localhost:8080
# sudo cat /var/lib/jenkins/secrets/initialAdminPassword
# ps -ef | grep -i [J]enkins
# sudo service jenkins restart
# sudo rm -rf /var/cache/jenkins/*

# jenkins integration

# virtualenv AWS_Preparation
# source AWS_Preparation/bin/activate
# pip install -r requirements.txt
# python manage.py migrate
# python manage.py runserver
# python manage.py test
# sudo service jenkins status
# sudo service jenkins start

# git add .
# git commit -m "text"
# git push