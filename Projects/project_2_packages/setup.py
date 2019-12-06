import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wethebest[ols]", # Replace with your own username
    version="0.0.1",
    author="Evan, Anna, Franco, Gabe",
    description="Dj Khaled",
    long_description=long_description,
    long_description_content_type="We out here",
    url="https://github.com/nyupredocs/modularizationandtesting/",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
