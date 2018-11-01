from setuptools import setup, find_packages

setup(
    name='auroravr',
    version='0.1.3',
    description='You can use it for communicate with aws gamelift',
    license="MIT",
    author='Auroravr',
    author_email='hyunjun.jeon@ticketplace.com',
    url='https://www.auroravr.io/',
    install_requires=['boto3'],
    packages=find_packages(exclude=['docs', 'tests*']),
    keywords=['aurora', 'auroravr', 'gamelift'],
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
