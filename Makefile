VERSION = `python -m pygrading version`
PACKAGE_PATH = package/${VERSION}

setup:
	###########################################
	##         Setup PyGrading Wheel         ##
	###########################################
	python setup.py sdist bdist_wheel

	rm -rf build
	rm -rf pygrading.egg-info

	mkdir -p package
	rm -rf ${PACKAGE_PATH}
	mv dist ${PACKAGE_PATH}
	

upload: setup

	###########################################
	##         Upload PyGrading Wheel        ##
	###########################################
	python -m twine upload ${PACKAGE_PATH}/*
