from setuptools import setup, find_packages


long_description = '''# List DLLs
Get Process Signatures'''

setup(
    name="listdlls",
    version="0.0.5",
    author="Pixelsuft",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pixelsuft/listdlls/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.5',
    license='MIT',
    keywords='listdlls',
    install_requires=[''],
    py_modules=["listdlls"]
)