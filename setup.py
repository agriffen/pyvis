from setuptools import setup, find_packages

exec(open('pyvis/_version.py').read())
setup(
    name="pyvis_agriffen_fork",
    version=__version__,
    description="A Python network visualization library, forked by agriffen",
    url="https://github.com/agriffen/pyvis",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "jinja2 >= 2.9.6",
        "networkx >= 1.11",
        "ipython >= 5.3.0",
        "jsonpickle >= 1.4.1"
    ]
)
