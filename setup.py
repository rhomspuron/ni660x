from setuptools import setup, find_packages

setup(name="ni660x-rpc",
    version='0.12.0',
    description="RPC server for NI660X counter application",
    author="Alba Synchrotron",
    author_email="controls@cells.es",
    extras_require={
          "server": ["nidaqmx", "click", "pyyaml"],
    },
    entry_points={
      'console_scripts': [
          'ni660x-rpc-server=ni660x.rpc.server:main',
      ]
    },
    packages=find_packages(exclude=['test']),
    classifiers=["License :: OSI Approved :: GNU General Public License v3 (GPLv3)",],
    license="GNU General Public License v3",
)
