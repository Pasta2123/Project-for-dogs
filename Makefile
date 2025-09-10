# Makefile for Python project

VENV = venv

APP = project_pes/app.py
# check if virtual environment exists
run:
		@echo "Running the application..."
		@if [ ! -d $(VENV) ]; then \
			echo "Virtual environment not found. Creating..."; \
			python3 -m venv $(VENV); \
		fi 
		./$(VENV)/bin/python $(APP)
		@echo "Application stopped."

.PHONY: run

# Spuštění testů
test:
	@echo "Running tests..."
	@if [ ! -d $(VENV) ]; then \
		echo "Virtual environment not found. Creating..."; \
		python3 -m venv $(VENV); \
	fi
	./$(VENV)/bin/pip install -r requirements.txt
	PYTHONPATH=. ./$(VENV)/bin/pytest

