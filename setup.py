from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask-Caching",
    install_requires=["cachelib <= 0.6.0", "Flask <= 2.1.2"],
)
