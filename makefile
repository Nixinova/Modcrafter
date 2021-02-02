### Make commands ###

# Initialise content mod folder
setup:
	python src/download.py

# Write mod content
#write:
#	python src/write/__main__.py

# Compile from content mod folder
compile:
	python src/compile.py

# Run all
run:
	python src/__main__.py
