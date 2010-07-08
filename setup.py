from setuptools import setup, find_packages

version = __import__('cms_facebook').__version__

setup(
    name = 'django-cms-fakebook',
    version = version,
    description = 'Django CMS Facebook Plugins',
    author = 'Jonas Obrist',
    author_email = 'jonas.obrist@divio.ch',
    url = 'http://github.com/ojii/django-cms-facebook',
    packages = find_packages(),
    package_data={
        'cms_facebook': [
            'templates/cms_facebook/*.html',
        ]
    },
    zip_safe=False,
)