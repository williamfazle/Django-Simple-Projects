# /var/www/yourusername_pythonanywhere_com_wsgi.py
import os
import sys

project_home = '/home/yourusername/django-blog'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# virtualenv
activate_this = '/home/yourusername/.virtualenvs/django-blog-venv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
os.environ.setdefault('DJANGO_SECRET_KEY', 'replace-with-secure-key-or-set-in-web-tab')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
