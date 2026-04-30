# Chapter 11 - Testing your code

This one will be a bit different. No print()'s etc.
Just follow the instructions below and look through tests

installed with pip as part of this chapter as well

Ensure you are in the chapter11 folder when running commands below

## Installation / Virtual Environments

First create a virtual environment and enter it

```bash
p -m venv .venv
source .venv/bin/activate
```

Then installed pytest (this was being shit so just use venv's below)

```bash
python3 -m pip install pytest
```

- there is the option to `install --user` which says its just for this user only
- -m = module

https://www.youtube.com/watch?v=4GT8fPvZDv8
Virtual environments exist to allow a single environment for your project
$ python3 -m <module-name> <virtual-env-name> (optional: python3.x)
venv is a common name for a virtual environment
I've commonly seen this:

```bash
python3 -m venv .venv
```

So this creates a folder called '.venv' if it's at the end

Activating a venv (mac)

```bash
source .venv/bin/activate
```

To leave your venv:

```bash
deactivate
```

The video link above says that 'requests' exists as package like axios

Now just install packages as such

```bash
python3 -m pip install pytest
```

## Testing / Modules

### Basic Testing

See that there is a [./tests/test_name_function.py](./tests/test_name_function.py) and a [./src/name_function.py](./src/name_function.py)

Common testing convention in python is that a test is written as such:
`test_<name-of-function-tested>.py`
easy

Now see that the testing function `assert`'s the value expected back. This is how the most basic test in Python is formed. Much shorter than JS's `expect(x)toBe(y)` however, Pytest can get more complicated than we're stating here

### Running The test files - Caveats to current setup

If all tests and files are in the same folder, we could just run:

```bash
$ pytest
```

But it's not that easy here...

### Modules

In Python you sometimes need to run your files or dependencies as modules.

This means running a test with the testable function in a different folder is not just as simple as running `pytest` alone

In our case to run a specific test file, you need to run with a `-m` flag
Now Python treats `tests/<files>` like a package and includes the root in `sys.path`.

To run the tests in one of our specific files, now (from the chapter11 folder) we run the following:

```bash
python -m pytest tests/test_name.py
```

This runs `pytest` as a module (`-m`) and then `tests/test_name.py` is an argument passed to it.

Python now can also run regular files as if they're modules.

However, this is a bit different as the file becomes a module itself and is called differently

Try running the following

```bash
python -m tests.test_survey
```

Here we have a **module path**, which follows similar rules that have been seen for imports in previous chapters.

Know that there's a distinction between a module path and a file path

### Why can't I just run `pytest` again?

When you run a file like this:

```bash
python tests/test_survey.py
```

Python sets:

```bash
sys.path[0] = "tests/"
```

Not your project root.

So Python will look for `survey.py` inside tests/, not alongside it.

## Using Fixtures

Fixtures can be used to help set up test environments. The example in [./tests/test_survey.py](./tests/test_survey.py) shows how this can be used to setup a classes instance automatically.

These are made with a `@pytest.fixture` decorator and applied as through the first argument of your test function.

A **decorator** is a directive placed just before a function definition - This alters how the code behaves depending on the decorator

Unlike with tests ran so far, you need to `import pytest` so that the decorator required for the fixture is added.

## BONUS: Test Markers

Another example of a decorator decorator is a [test marker](https://docs.pytest.org/en/stable/example/markers.html#mark-examples).

These can be used to group Python functions together. For example, all unit tests could have a `@pytest.mark.unit`. These would then be ran with... (don't run this code as there are no unit tests)

```bash
`python -m pytest -m unit`
```

**Remember:** the first `-m` is an argument for `python` that is for modules. The second `-m` is an argument for `pytest` that runs all functions with the unit test marker.

Notice how in [./tests/test_survey.py](./tests/test_survey.py), there are markers for `classes`. This code can actually be run.

```bash
`python -m pytest -m classes`
```

If you want to run all other tests, you could do...

```bash
`python -m pytest -m "not classes"`
```

Also notice how there is a `pytest.toml` file in the root of this project. In this, I have declared `classes` as a custom marker (i.e. one that doesn't already come with Pytest).

Without this config, there would be a warning when runnning the above commands.
