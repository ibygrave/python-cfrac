cfrac: Example Python Project
=============================

This is a simple example Python3 project using
[tox](https://tox.readthedocs.io/en/latest/) and
[pytest](https://pytest.org).

The package is built and tested by running:

    $ tox

The `tox.ini` configuration:
 * Performs linting and testing of a [development mode](https://setuptools.readthedocs.io/en/latest/userguide/development_mode.html) install of the package.
 * Builds and tests a source distribution of the project.

To use wheels instead of a source distribution install the [tox-wheel](https://pypi.org/project/tox-wheel/) plugin and run:

    $ tox --wheel

The content of this example project converts between
[continued fractions](https://en.wikipedia.org/wiki/Continued_fraction) and
[Python fractions](https://docs.python.org/3/library/fractions.html).
