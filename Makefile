.PHONY: notes

notes:
	pandoc workshop.md -s --css=workshop.css -o docs/workshop.html
	cp workshop.css docs
