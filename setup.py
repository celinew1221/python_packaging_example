from setuptools import setup

setup(name='python_packaging_example',
      version='1.0',
      description='To demostrate basic packaging',
      url='',
      author='Celine Wei',
      author_email='cw.git.general@gmail.com',
      license='MIT',
      packages=['package_examples'],
      install_requires=['numpy>=1.16.2'],
      dependency_links=['https://github.com/celinew1221/notifyme/tarball/master#egg=notifyme-v1.0'],
      zip_safe=False,
      package_dir={'package_examples': '.'},
      package_data={'package_examples': ['*.so']},) # this is not in this example, but if you want to include your c dynamic library, this is what you'll do
