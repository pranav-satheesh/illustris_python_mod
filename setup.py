from setuptools import setup

setup(
    name='illustris_python_mod',
    version='1.0.0',
    packages=["illustris_python_mod"],
    install_requires=["numpy", "h5py", "six"],
    tests_require=["nose","coverage"],
)
