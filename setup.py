from setuptools import setup, find_packages

setup(name='unictelecome',
      version='1.0',
      url='#',
      license='MIT',
      author='Wardak Ahmad Samir',
      author_email='wardag.as@gmail.com',
      description='Send sms from unictelecome.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      install_requires=[
            'requests',
        ],
      zip_safe=False)