from setuptools import setup, find_packages

version = __import__('cmsplugin_facebook').__version__

setup(
    name = 'cmsplugin_facebook',
    version = version,
    description = 'Django CMS Facebook Plugins',
    author = 'Jonas Obrist, Christopher Glass',
    author_email = 'jonas.obrist@divio.ch, christopher.glass@divio.ch',
    url = 'http://github.com/ojii/cmsplugin_facebook',
    packages = find_packages(),
    package_data={
        'cmsplugin_facebook': [
            'templates/cmsplugin_facebook/*.html',
        ]
    },
    zip_safe=False,
)
