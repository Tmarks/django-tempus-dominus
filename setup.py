from setuptools import setup, find_packages
setup(
    name='django-tempus-dominus',
    version="0.1",
    description='',
    author='Tim Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/FlipperPA/django-tempus-dominus',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)