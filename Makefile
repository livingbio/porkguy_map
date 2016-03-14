#
# Makefile
# lizongzhe, 2016-01-30 16:11
#
SHELL = /bin/bash
VPATH = .make

%.success: %
	mkdir -p .make && \
	echo "$*" > .make/$@ && \
	echo $* > .make/$*

IMAGE_FILES = $(shell find image/* -type f)
export host = $(shell echo "$(DOCKER_HOST)"|sed 's/[^:]*:\/\///'|sed 's/:[^:]*$$//')
export port = $(shell for port in $$(seq 8000 65000); do echo -ne "\035" | telnet $(host) $$port > /dev/null 2>&1; [ $$? -eq 1 ]  && break; done;echo $$port)
export IMAGE = porkman
wait_time = 5


build: $(IMAGE_FILES)
	curl https://raw.githubusercontent.com/gliacloud/deploy/new/src/build.sh -o build.sh && source build.sh && docker tag $$IMAGE_NAME $(IMAGE) && rm build.sh

MODELS_FILE=$(shell find src/**/models.py)
setup:: $(MODELS_FILE)
	docker-compose -f deploy/docker-compose.yml run main python manage.py makemigrations

MIGRATE_FILES=$(shell find src/**/migrations/**.py)
setup:: $(MIGRATE_FILES) build.success
	docker-compose -f deploy/docker-compose.yml run main python manage.py migrate

shell: setup.success
	docker-compose -f deploy/docker-compose.yml run main /bin/bash

test: setup.success
	env
	docker-compose -f deploy/docker-compose.yml run main py.test
	docker-compose -f deploy/docker-compose.yml run main flake8

runserver: setup.success
	(sleep $(wait_time) && open http://$(host):`docker-compose -f deploy/docker-compose.yml port main 80|sed 's/.*://'`)&
	docker-compose -f deploy/docker-compose.yml up main

