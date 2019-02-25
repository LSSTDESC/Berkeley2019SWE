.PHONY: notes

notes:
	pandoc workshop.md -s --css=workshop.css -o workshop.html
