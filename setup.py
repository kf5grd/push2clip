from setuptools import setup

setup(
        name='push2clip',
        version='0.1',
        py_modules=
            ['push2clip'],
            install_requires=[
                'Click', 
                'requests',
            ],
            entry_points='''
               [console_scripts]
               push2clip=push2clip:cli
            ''',
    )
