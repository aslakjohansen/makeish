TARGETS = \
	check \
	sdist \
	wheel \
	upload \


all: ${TARGETS}


check:
	python3 setup.py check

sdist:
	python3 setup.py sdist

wheel:
	pip3 install wheel

upload:
	twine upload --verbose --repository-url https://upload.pypi.org/legacy/ dist/*

