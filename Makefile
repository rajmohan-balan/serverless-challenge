SLS := docker-compose run --rm serverless

ifdef ENVFILE
	ENVFILE_TARGET=envfile
else
	ENVFILE_TARGET=.env
endif

PYTHON_VERSION=python3.6
PACKAGE_DIR=package
PYTEST_PATH=/opt/app/tests
FLAKE8=flake8 ./src --count --statistics # add "--exit-zero" to treat errors as warnings
SET_ROLES_EVENT=$(shell cat ./tests/fixtures/payload/string/roles_request.txt)
SET_USERS_EVENT=$(shell cat ./tests/fixtures/payload/string/users_request.txt)

deps: $(ENVFILE_TARGET)
	$(SLS) make _pythonDeps _devdeps

build: $(ENVFILE_TARGET)
	docker-compose run --rm lambda-build make _build
	
offline: $(DOTENV_TARGET)
	docker-compose run -p 3000:3000 --rm serverless sls offline start --host 0.0.0.0

run_setRoles: $(ENVFILE_TARGET)
	cp -a src/. $(PACKAGE_DIR)/
	docker-compose run --rm lambda handler.setRoles '$(SET_ROLES_EVENT)'

run_setUsers: $(ENVFILE_TARGET)
	cp -a src/. $(PACKAGE_DIR)/
	docker-compose run --rm lambda handler.setUsers '$(SET_USERS_EVENT)'

run_getSubOrdinates: $(ENVFILE_TARGET)
	cp -a src/. $(PACKAGE_DIR)/
	cp -a tests/. $(PACKAGE_DIR)/tests
	docker-compose run --rm lambda handler.getSubOrdinates $(ARGS)

shell: $(ENVFILE_TARGET)
	@$(SLS) bash

checks: $(ENVFILE_TARGET)
	@$(SLS) make _lint _test

lint: $(ENVFILE_TARGET)
	@$(SLS) make _lint

flake8: $(ENVFILE_TARGET)
	@$(SLS) make _flake8

pylint: $(ENVFILE_TARGET)
	@$(SLS) make _pylint

test: $(ENVFILE_TARGET)
	@$(SLS) make _test

testUnit: $(ENVFILE_TARGET)
	@$(SLS) make _testUnit

testUnitWithCoverage: $(ENVFILE_TARGET)
	@$(SLS) make _testUnitWithCoverage

testIntegration: $(ENVFILE_TARGET)
	@$(SLS) make _testIntegration

#################
# Dot file .env #
#################

# Create .env based on .env.template if .env does not exist
.env:
	@echo "Create .env with .env.template"
	cp .env.template .env
	echo "" >> .env
	echo "BUILD_VERSION=$(BUILD_VERSION)" >> .env

# Create/Overwrite .env with $(ENVFILE)
envfile:
	@echo "Overwrite .env with $(ENVFILE)"
	cp $(ENVFILE) .env

###############################
# Python virtual environment #
##############################

venv:
	$(PYTHON_VERSION) -m venv --copies venv
	# bin/activate hardcodes the path when you create it making it unusable outside the container, this patch makes it dynamic. Double dollar signs to escape in the Makefile.
	sed -i '43s/.*/VIRTUAL_ENV="$$(cd "$$(dirname "$$(dirname "$${BASH_SOURCE[0]}" )")" \&\& pwd)"/' venv/bin/activate
	sed -i '1s/.*/#!\/usr\/bin\/env python/' venv/bin/pip*

####################
# Testing Commands #
####################

_lint: _pythonDeps _flake8 _pylint

_flake8:
	# stop the build if there are Python syntax errors or undefined names
	$(FLAKE8) --select=E9,F63,F7,F82 --show-source
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	$(FLAKE8) --max-complexity=10 --max-line-length=180

_pylint:
	pylint ./src --exit-zero --errors-only

_test: _pythonDeps
	pytest $(PYTEST_PATH)/

_testUnit:
	pytest $(PYTEST_PATH)/unit

_testUnitWithCoverage:
	pytest $(PYTEST_PATH)/unit --cov-report term --cov=/opt/app /opt/app/tests/unit

_testIntegration:
	pytest $(PYTEST_PATH)/integration

########################
# Development commands #
########################

_pythonDeps:
	python3 -m venv /opt/app/python_modules
	pip install --upgrade pip
	pip3 install flake8 pylint pytest pytest-cov

_build: venv requirements.txt
	mkdir -p $(PACKAGE_DIR)
	sh -c 'source venv/bin/activate &&pip install --upgrade pip && pip install -r requirements.txt'
	cp -a venv/lib/$(PYTHON_VERSION)/site-packages/. $(PACKAGE_DIR)/
	cp -a src/. $(PACKAGE_DIR)/
	# creates .pyc files which might speed up initial loading in Lambda
	@cd $(PACKAGE_DIR) && python -O -m compileall -q .
	
_devdeps:
	npm install --save-dev
	npm audit fix
	
_offline:
	sls offline start --host 0.0.0.0