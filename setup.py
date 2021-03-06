import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

required_packages = ['fsspec', 'gcsfs', 'google-cloud-bigquery', 'google-cloud-storage', 'pandas', 'pyarrow', 'tqdm']

setuptools.setup(
    name="gcpy", 
    version="0.0.1",
    author="stephenleo",
    author_email="stephen.leo87@gmail.com",
    description="A Python package to easily interface with Google Cloud Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stephenleo/gcpy",
    install_requires=required_packages,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <3.9',
)