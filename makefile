
action_files=$(shell fd action.yml)
workflow_files=$(shell fd --no-ignore "\.yml" -- .github/workflows)
python_files=$(shell fd -tf py$$ --max-depth 1)

f format: format_workflow_files format_action_files format_python_files

format_workflow_files: $(workflow_files)
	@./format.py $^

format_action_files: $(action_files)
	@./format.py $^

format_python_files: $(python_files)
	@black $^

NAME?=
a action:
	@mkdir -p actions/$(NAME)
	@touch actions/$(NAME)/action.yml
	@echo "created actions/$(NAME)/action.yml"

m macro:
	@mkdir -p macros/$(NAME)
	@touch macros/$(NAME)/action.yml
	@echo "created macros/$(NAME)/action.yml"

j job:
	@mkdir -p jobs/$(NAME)
	@touch jobs/$(NAME)/action.yml
	@echo "created jobs/$(NAME)/action.yml"

w workflow:
	@touch .github/workflows/$(NAME).yml
	@echo "created .github/workflows/$(NAME).yml"
