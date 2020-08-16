from setuptools import setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession


install_reqs = parse_requirements('requirements.txt', session=PipSession())

reqs = [str(ir.req) for ir in install_reqs]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
   name='downloads3key',
   version='1.9',
   description='Utility to download all s3 versions of s3 key.',
   author='Chandan Mahajan',
   author_email='mahajan.chandan18@gmail.com',
   packages=['downloads3key'],  #same as name
   install_requires=reqs, #external packages as dependencies
   license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
   long_description=long_description,
   long_description_content_type="text/markdown",
   keywords = ['aws s3', 'download s3 key versions'],   # Keywords that define your package best
   python_requires='>=3.6',
   entry_points={
          'console_scripts': [
              'downloads3key = downloads3key.__main__:main'
          ]
      }
)
