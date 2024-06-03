
action_files=$(shell fd action.yml)
python_files=$(shell fd -tf py$$ --max-depth 1)

format: format_action_files format_python_files

format_action_files: $(action_files)
	@./format.py $^

format_python_files: $(python_files)
	@black $^

NAME?=
action:
	@mkdir -p actions/$(NAME)
	@touch actions/$(NAME)/action.yml

macro:
	@mkdir -p macros/$(NAME)
	@touch macros/$(NAME)/action.yml
