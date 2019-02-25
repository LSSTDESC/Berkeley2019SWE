---
title: DE SWE Workshop
---

Collaborative software development in Python.

## Introduction

In the next two hours, we are going to build our own Python package.
This package will be installable via the standard installation
mechanism (`pip`), and will be tested and documented.  We will host
the source code for our project online, on GitHub, and use the `git`
tool to track changes to our package as it evolves.  We will also see
how to make modifications to others' software, as well as how to have
them contribute to ours.

Each lesson is broken up into a short lecture, followed by hands-on
exercise time.

The goal of today's workshop is for you to *leave with practices
skills*, not to cover as much ground as possible—so, we may not get
through the entire schedule.  If you already understand what is being
taught, please take a walk around and help others complete the
exercises.

##  Before we begin

Make sure to setup your environment for the workshop by following [these instructions](https://lsstdesc.github.io/Berkeley2019SWE/slides.html#/1)

## Building a Python package from scratch

<div class="live-demo">
**Demonstration:** Building a Python package
</div>

Minimal package structure:

```
example-package
├── README.md
├── LICENSE.txt
├── requirements.txt
├── setup.py
├── darkbox
└── └── energy.py
```

See `templates/*-example-package-*`.

<div class="exercise">
**Exercise:** Construct your own package, and add a submodule called
`energy`.  Inside that submodule, add a function `abs_area`, that
takes the absolute value of an input array, and calculates its area
using
the
[trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule).

If you get stuck on the implementation, use the following (incorrect)
implementation for the time being:

```python
import numpy as np

def abs_area(x):
    return np.sum(np.abs(x))
```

Make sure your package can be installed with `pip`:

```bash
$ pip install .
```

If you want to install your package while developing it, and without
reinstalling after each change, use:

```bash
$ pip install --editable .
```

Launch a Python terminal (IPython, Python, or Jupyter) and import your
new package.  Execute your submodule function, and make sure it
performs according to your expectation.

</div>

## Test your code

<div class="live-demo">
**Demonstration:** Writing a test suite
</div>

<div class="exercise">
**Exercise:** Add tests for each function in your package.  You may
use all
the
[`assert_` functions inside `numpy.testing`](https://docs.scipy.org/doc/numpy/reference/routines.testing.html).
Run your test suite to ensure that it passes:

```bash
# Execute this from one directory above your package

$ PYTHONPATH=. pytest
```

Now, introduce a breaking change in one of the functions, and run your
test suite again: it should fail.  If it does not, go back, improve
your tests, and repeat the exercise.

</div>

## Document your code with Sphinx & numpydoc

<div class="live-demo">
**Demonstration:** Documenting with Sphinx
</div>

<div class="exercise">

**Exercise:** Set up Sphinx documentation for your test package using
`sphinx-quickstart`.  In the generated `docs/conf.py`, ensure you have
the following extensions enabled:

```python
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'numpydoc'
]
```

Optionally, you can enable Markdown rendering:

```python
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
```

Ensure one or more of your functions
have
[`numpydoc`-compatible docstrings](https://numpydoc.readthedocs.io).
Execute the following command to generate API docs:

```bash
$ sphinx-apidoc --module-first --no-toc --separate --force -o api ../<your-package-name>
```

Compile your documentation using `make html`.

</div>

## Tracking your changes with Git

<div class="live-demo">
**Demonstration:** git: feature branches
</div>

- `git init`, to start tracking current directory.
- Staging changes (concept, `git add`, `git add -p`)

For collaborative purposes, it is important to know how branching
works.

- Creating feature branches
- Switching between branches
- Merging branches

<!--
- Merging conflicts
  - Rebasing history
  - `git reflog`
-->

<div class="exercise">

**Exercise:** From the `master` (default) branch, make two branches:
`docs` and `add-func` using `git checkout -b <branch_name>`.  In
`docs`, update the `README.md`, with a short description of the
package and commit.  In `add-func`, add a new function to one of the
submodules, commit.  Switch back to `master`, and merge the `docs`
branch, and then the `add-func` branch.

</div>

## GitHub

### Start a project and upload your source

<div class="live-demo">
**Demonstration:** GitHub: starting a project
</div>

<div class="exercise">
**Exercise:** Make a new GitHub repository for your package.  Upload
your package.
</div>

### Interlude: ReadTheDocs and Travis-CI

<div class="live-demo">
**Demonstration:** How to set up ReadTheDocs and Travis-CI for your repo
Slides are [here](https://lsstdesc.github.io/Berkeley2019SWE/slides.html#/2)
</div>

### Social GitHub

<div class="live-demo">
**Demonstration:** GitHub: Making and reviewing a Pull Request
</div>

One example
of
[a good quality PR](https://github.com/scikit-image/scikit-image/pull/2327).

#### Make a pull request

**Exercise:** Talk to one of your neighbors, and get their repo
location on GitHub.  **Fork** their repository, and `git clone` it
locally.  Make a feature branch `add-hello`.  Add a new function to
their `energy` submodule (or anywhere else, if that doesn't exist):
`def norm(x): ...`, that calculates the Euclidean norm,
$\left\|{\boldsymbol {x}}\right\|_{2}:= \textrm{sqrt} \left( x_{1}^{2} + \cdots +
x_{n}^{2} \right)$.  Commit, and make a pull request.

<div class="exercise"> **Exercise:** Wait for your neighbor to review
your pull request.  Modify your code in response to their feedback.
Push the changes back to GitHub.  Work with them until they are happy
to merge your change.
</div>

## Additional exercises

<div class="exercise">

1. **PyPi (Python Packaging Index) publication**

   Follow the instructions at
   https://packaging.python.org/guides/using-testpypi/ and upload your
   library to the test packaging index.

   Check whether your package can be installed, using:

   ```bash
   $ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple your-package
   ```

</div>
