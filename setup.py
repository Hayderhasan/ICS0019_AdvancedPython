import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quadratic-equation-haalsa",
    version="0.0.1",
    author="Hayder Hasan",
    author_email="hayderhasan@protonmail.com.com",
    description="A package that solves quadratic equations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hayderhasan/ICS0019_AdvancedPython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='quadratic-equation-haalsa.tests.quadratic-equation-haalsa-tests'
)