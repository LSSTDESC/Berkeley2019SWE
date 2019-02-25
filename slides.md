---
# To use reveal-md, first install it using npm:
# $ npm install -g reveal-md
# Then run it, pointing to this slide deck:
# $ reveal-md slides.md
title: Collaborative software development in Python
theme: simple
highlightTheme: rainbow
---

## Collaborative software development in Python

DE School, Berkeley 2019

---

### Setting up Travis CI

---

The *.travis.yml* script:

```yaml
language: python
python:
  - "2.7"
  - "3.5"
  - "3.6"

# command to install dependencies
install:
  - pip install -r requirements.txt

# command to run tests
script:
  - pytest
```

---

### Documentation

Check out this [link](https://numpydoc.readthedocs.io/en/latest/format.html)


Note: speaker notes FTW!
