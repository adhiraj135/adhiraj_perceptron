import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME="adhiraj_perceptron"
USER_NAME="adhi135"
package_name="adhiraj_perceptron"


setuptools.setup(
    name=f"{package_name}-{USER_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="adhiraj.singh483@gmail.com",
    description="A small package for perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "numpy==1.23.4",
        "pandas==1.5.1",
        "joblib==1.2.0"
    ]
)