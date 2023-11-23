SCRIPT_NAME := script.py
OUTPUT_PATH := $(CURDIR)/output

all: run_script

run_script:
	@python3 -m venv $(CURDIR)
	@. $(CURDIR)/bin/activate; \
	export OUTPUT_PATH=$(OUTPUT_PATH); \
	python3 $(SCRIPT_NAME) < input

clean:
	@rm -rf $(CURDIR)/bin $(CURDIR)/lib $(CURDIR)/include $(CURDIR)/pyvenv.cfg
