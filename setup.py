from setuptools import setup

setup(
    name='snapshotanalyzer-30000',
    version='0.1',
    author='casual coder',
    author_email='aaaa@aaa.com',
    description='SnapshotAnalyzer 30000 is a tool to manage EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/casualcoder1/snapshotalyzer-30000',
    install_requires=[
        'click',
        'boto3'
    ],
    # We have a console script
    # it is called shotty (shotty=), it will look inside the package called (shotty=shotty)
    # for a module called shotty (shotty=shotty.shotty)
    # it will then look for the function called cli (shotty=shotty.shotty:cli)
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
