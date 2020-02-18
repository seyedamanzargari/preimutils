from setuptools import setup
import os

if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG']
else:
    version = os.environ['CI_JOB_ID']

setup(
    name="preimutils",
    packages=['preimutils'],
    version=version,
    description="all you need to prepare and preprocess your annotated images",
    url="https://github.com/mrl-amrl/preimutils",
    download_url='https://github.com/mrl-amrl/preimutils/archive/1.0.0.tar.gz',
    author="Amir Sharifi",
    author_email="ami_rsh@outlook.com",
    license='MIT',
    keywords=['computer vision', 'image processing', 'opencv',
              'matplotlib', 'preprocess image', 'image dataset', 'pascal voc'],
    entry_points={
        'console_scripts': ['preimutils=preimutils.run:main'],
    },
    install_requires=[
        'pascal_voc_writer',
        'tqdm',
        'pandas',
        'albumentations',
    ],
    zip_safe=False,
)
