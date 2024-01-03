import setuptools
import versioneer

if __name__ == "__main__":
    setuptools.setup(
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=setuptools.find_packages(exclude=['tests_libaicv']))

# To build package :
# python setup.py sdist bdist_wheel
# python setup.py bdist_wheel
# python setup.py build 