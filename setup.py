from setuptools import setup, find_packages

version = __import__('cmsplugin_facebook').__version__

setup(
    name = 'cmsplugin-facebook',
    version = version,
    description = 'Django CMS Facebook Plugins',
    author = 'Christopher Glass, Jonas Obrist',
    author_email = 'christopher.glass@divio.ch, jonas.obrist@divio.ch',
    url = 'http://github.com/chrisglass/cmsplugin_facebook',
    packages = find_packages(),
    package_data={
        'cmsplugin_facebook': [
            'templates/cmsplugin_facebook/*.html',
        ]
    },
    zip_safe=False,
    install_requires=[
        "django-cms",
    ]
)
