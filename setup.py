from setuptools import setup, find_packages

setup(name="ni660x",
    version="0.1",
    description="Paquete de ni",
    author="Alba sincotron",
    install_requires=["nidaqmx","click","pyyaml",],
    packages=find_packages(),
    test_suite="test",
    classifiers=["License :: OSI Approved :: GNU General Public License v3 (GPLv3)",],
    license="GNU General Public License v3"
)
