
action_files=$(shell fd action.yml)
format: $(action_files)
	@./format.py $^
