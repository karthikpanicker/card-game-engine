import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="card-game-engine", # Replace with your own username
    version="0.0.1",
    author="Karthik Raveendran",
    author_email="karthik.panicker@gmail.com",
    description="A card game engine",
    long_description="A card game engine for creating gaming sessions for 28,56 and similar card games",
    long_description_content_type="text/markdown",
    url="https://github.com/karthikpanicker/card-game-engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)