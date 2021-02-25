
FORCE:

tests: FORCE
	nosetests --with-coverage --cover-package=.

prod: tests
	git commit -a
	git push origin main
