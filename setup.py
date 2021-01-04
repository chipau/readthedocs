from setuptools import setup, find_packages

VERSION = '1.0.2'

with open("requirements.txt") as data:
    install_requires = [
        line for line in data.read().split("\n")
            if line and not line.startswith("#")
    ]

setup(
    name="mkdocs-rtd-dropdown",
    version=VERSION,
    url='https://github.com/carolynkish300/mkdocs-rtd-dropdown',
    license='DLM',
    description='Yến sào Đại Lâm Mộc',
    author='Trương Xuân Vũ',
    author_email='yensao@dlm.vn',
    packages=find_packages(),
    include_package_data=True,
    install_requires = install_requires,
    entry_points={
        'mkdocs.themes': [
            'rtd-dropdown = rtd_dropdown',
        ]
    },
    zip_safe=False
)
