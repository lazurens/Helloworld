from distutils.core import setup

setup(
    name='helloworld',
    version='0.1.0',
    author='Mohamed Jelidi',
    author_email='jelidi.mohamad@mail.com',
    scripts=['helloworld.py'],
    license='LICENSE.txt',
    description='International helloworld',
    url='http://pypi.python.org/pypi/Helloworld/',
    packages=['helloworld', 'helloworld.test'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    long_description=open('README.txt').read(),
)