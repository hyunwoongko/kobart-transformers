import codecs
from setuptools import setup, find_packages


def read_file(filename, cb):
    with codecs.open(filename, 'r', 'utf8') as f:
        return cb(f)


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kobart-transformers',
    version='0.1.2',
    author='Hyunwoong Ko',
    author_email='kevin.woong@kakaobrain.com',
    url='https://github.com/hyunwoongko/kss-python',
    license='BSD 3-Clause "New" or "Revised" License',
    description='Kobart model on huggingface transformers',
    long_description_content_type='text/markdown',
    platforms=['any'],
    long_description=long_description,
    packages=find_packages(exclude=[]),
    keywords=["kobart", "huggingface", "deep learning"],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
