from setuptools import setup, find_packages

setup(
    name='openweather_cli',
    version='1.0.0',
    url='https://github.com/JosephDemarest/openweather_cli',
    author='Joseph Demarest',
    author_email='Joseph.Demarest@cix.csi.cuny.edu',
    description='Command-line weather application',
    packages=find_packages(),    
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'openweather_cli = openweather_cli.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
