entry_point = console.py
MAKEFLAGS += --silent

all: clear_screen check_style run_tests

run:
	@python3 $(entry_point)

run_tests:
	@$(MAKE) announce MESSAGE="Running unit tests - non interactive"
	python3 -m unittest discover tests
	@$(MAKE) announce MESSAGE="Running unit tests - interactive"
	echo "python3 -m unittest discover tests" | bash

announce:
	@echo "------------------------------------------"
	@printf "|%*s%s%*s|\n" $$(expr 20 - $${#MESSAGE} / 2) "" "$(MESSAGE)" $$(expr 20 - $$(($${#MESSAGE} + 1)) / 2) ""
	@echo "------------------------------------------"

check_style:
	@$(MAKE) announce MESSAGE="Checking code style"
	pycodestyle --first $(entry_point) tests && \
	($(MAKE) announce MESSAGE="Code style OK" && exit 0) || \
	($(MAKE) announce MESSAGE="Code style error" && exit 1)

clear_screen:
	clear
