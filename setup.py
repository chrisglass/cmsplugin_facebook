from setuptools import setup, find_packages

version = __import__('cmsplugin_facebook').__version__

setup(
    name = 'cmsplugin_facebook',
    version = version,
    license= 'BSD',
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
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
