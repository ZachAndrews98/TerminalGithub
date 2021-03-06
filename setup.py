import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terminal-github", # Replace with your own username
    version="0.0.1",
    author="Zachary Andrews",
    author_email="zachandr98@gmail.com",
    description="Interactions with Github in the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points="""
    [console_scripts]
    tg = src.main:main
    """,
    python_requires='>=3.6',
)
