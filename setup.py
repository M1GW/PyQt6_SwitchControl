import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
	name="QSwitchControl",
	version="1.0.4",
	description="An easy-to-use and modern toggle switch for Qt Python binding PyQt",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/M1GW/QSwitchControls",
	author="M1GW",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: Implementation :: CPython"
	],
	# py_modules=["__init__", "__main__", "QSwitchControl", "QSwitchControlplugin"],
	packages=["QSwitchControl"],
	include_package_data=True,
	install_requires=["PyQt6"]
)
