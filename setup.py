from distutils.core import setup

setup(
    name="APA division 44 website - quick deploy",
    packages=['app'],
    package_data={  
        'app': ['static/*','views/*.html','views/member/*.html'],
    },
    scripts=['deploy'],
    license="PSF",
)
