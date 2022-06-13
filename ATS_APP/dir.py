import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
'''BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATIC_DIR=os.path.join(BASE_DIR,'static')'''

print(BASE_DIR)