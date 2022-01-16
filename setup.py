#uploaded this as... it was difficult for me to make. so now others can copy this format (and hopefully credit me)
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ScraGet",
    version="0.2.3",
    #author="QuantumCodes",
    #author_email="author@example.com",
    description="A package that makes interacting with Scratch API easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quantum-Codes/ScraGet",
    license='MIT',#added
    packages=['ScraGet'],#added
    install_requires=["requests"],
    keywords="Scratch, ScraGet, API, ScratchAPI, Scratch-API, Scratch3, ScratchCloud, Cloud",
    project_urls={
        "Source": "https://github.com/Quantum-Codes/ScraGet/tree/master/ScraGet",
        "Bug Tracker": "https://github.com/Quantum-Codes/ScraGet/issues",
        "Documentation": "https://github.com/Quantum-Codes/ScraGet/wiki"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
