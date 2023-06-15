from setuptools import setup, find_packages

print(find_packages())

setup(
    name="Dharma",
    version="1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["Dharma = Dharma.main:main"]},
    install_requires=[
        "libvirt-python ==9.2.0",
        "pycairo ==1.23.0",
        "PyGObject ==3.44.1"
        ]
)
