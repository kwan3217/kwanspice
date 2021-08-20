from setuptools import setup

setup(
    name='kwanspice',
    version='0.1.0',
    description='Python spice tools',
    url='https://github.com/kwan3217/kwanspice/',
    author='kwan3217',
    author_email='kwan3217@gmail.com',
    license='BSD 2-clause',
    packages=['kwanspice'],
    install_requires=[
                      'numpy',
                      'spiceypy',
                      ],

   entry_points={
        "console_scripts":[
            "spkdump = kwanspice.daf:spkdump",
        ]
    },
)
