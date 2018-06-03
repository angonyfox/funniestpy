from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/angonyfox/funniestpy',
      scripts=['bin/joke'],
      entry_points = {
          'console_scripts': ['joke_cmd=funniest.joke_cmd:main'],
      }
      author='Flying Circus',
      author_email='angonyfox@gmail.com',
      license='MIT',
      packages=['funniest'],
      zip_safe=False)