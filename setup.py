from setuptools import setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession


install_reqs = parse_requirements('requirements.txt', session=PipSession())

reqs = [str(ir.req) for ir in install_reqs]

setup(
   name='download-s3-file-versions',
   version='1.0',
   description='Utility to download all s3 versions of s3 key.',
   author='Chandan Mahajan',
   author_email='mahajan.chandan18@gmail.com',
   packages=['.'],  #same as name
   install_requires=reqs, #external packages as dependencies
)