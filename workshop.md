# DE SWE Workshop

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

## Building a Python package from scratch

Minimal structure of a package (Python 3):

```
example-package
├── README.md
├── setup.py
├── darkbox
└── └── energy.py
```

See `templates/example-package`.

**Exercise:** Construct your own package, and add a submodule called
`energy`.  Inside that submodule, add a function `abs_area`, that
takes the absolute value of an input array, and calculates its area
using
the
[trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule).

If you get stuck on the implementation, use the following (incorrect)
implementation for the time being:

```
import numpy as np

def abs_area(x):
    return np.sum(np.abs(x))
```

Make sure your package can be installed with `pip`:

```
pip install .
```

If you want to install your package, but keep developing it without
reinstalling after each change, use:

```
pip install --editable .
```

Launch IPython (or the Python interpreter, if that is not installed),
and import your new package.  Execute some of its submodule functions,
and make sure they perform according to your expectations.

## Test your code

**Exercise:** Add tests for each of the functions in your package.
Run your test suite to ensure that it passes.  Now, introduce a
breaking change in one of the functions, and run your test suite
again: it should fail.  If not, go back, update your tests, and repeat
the exercise.

## Document your code with Sphinx & numpydoc

**Exercise:** Set up Sphinx documentation for your test package.
Configure Sphinx to use `numpydoc`.  Ensure one or more of your
functions have `numpydoc`-compatible docstrings.  Compile your
documentation.

## Tracking your changes with Git

- `git init`, to start tracking current directory.
- Staging changes (concept, `git add`, `git add -p`)

For collaborative purposes, it is important to know how branching
works.

- Creating feature branches
- Switching between branches
- Merging conflicts
  - Rebasing history
  - `git reflog`

**Exercise:** Make two branches: `docs` and `add-func`.  In `docs`,
update the `README.md`, with a short description of the package and
commit.  In `add-func`, add a new function to one of the submodules,
commit.  Also on `add-func`, modify the `README.md` file to mention
the function you added.  Switch back to `master`, and merge `docs` and
then `add-func`.  Resolve any conflicts that arise to complete the
merge.

## GitHub

### Start a project and upload your source

**Exercise:** Make a new GitHub repository for your package.  Upload
your package.

### Interlude: ReadTheDocs and Travis-CI

### Social GitHub

#### Make a pull request

**Exercise:** Talk to one of your neighbors, and get their repo
location on GitHub.  **Fork** their repository, and `git clone` it
locally.  Make a feature branch `add-hello`.  Add a new function to
one of their submodules `def hello(name): ...` that prints a greeting
to the screen.  Commit, and make a pull request.

#### Review a pull request

**Exercise:** Wait for your neighbor to review your pull request.
Modify your code in response to their feedback.  Push the changes back
to GitHub.  Work with them until they merge your change.

## Additional exercises

1. PyPi

Follow the instructions at
https://packaging.python.org/guides/using-testpypi/ and upload your
library to the test packaging index.

Check whether your package can be installed, using:

```
$ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple your-package
```
