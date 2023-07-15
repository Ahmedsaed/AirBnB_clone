entry_point = console.py
MAKEFLAGS += --silent
PYTHON := python3

all: clear_screen check_style run_tests

run:
	@$(PYTHON) $(entry_point)

run_tests:
	@$(MAKE) announce MESSAGE="Running unit tests - non interactive"
	$(PYTHON) -m unittest discover tests
	@$(MAKE) announce MESSAGE="Running unit tests - interactive"
	echo "$(PYTHON) -m unittest discover tests" | bash

announce:
	@echo "------------------------------------------"
	@printf "|%*s%s%*s|\n" $$(expr 20 - $${#MESSAGE} / 2) "" "$(MESSAGE)" $$(expr 20 - $$(($${#MESSAGE} + 1)) / 2) ""
	@echo "------------------------------------------"

check_style:
	@$(MAKE) announce MESSAGE="Checking code style"
	pycodestyle --first $(entry_point) models tests && \
	($(MAKE) announce MESSAGE="Code style OK" && exit 0) || \
	($(MAKE) announce MESSAGE="Code style error" && exit 1)

clear_screen:
	clear
