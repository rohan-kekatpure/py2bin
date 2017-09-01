# py2bin

`py2bin` is a working example (not an installable or a library) demonstrating how to compile multi-module Python machine
learning applications into a single binary installable. Typically, Python libraries or components are distributed as
tarballs of pure Python code or C-extensions. However, distribution of end-user _applications_ is difficult and somewhat
of an [art form](https://hackerboss.com/how-to-distribute-commercial-python-applications/). Application distribution is not 
as straightforward as in the Java, or even C world.
 
Typical path is to 'freeze' the application using the knowledge of your target system (Windows, Linux, or Mac) and using the 
appropriate freezing application. This repository is based on the [Pyinstaller](https://github.com/pyinstaller/pyinstaller/wiki)
application. 

As application developers, we desire the packaging system to be able to:

1. work with the hierarchical Python package structure
2. embed standard Python ML libraries (sklearn, keras, ...)
3. embed numerical packages (scipy, numpy)
4. embed and read non-python resource data (config files, data directories ...)
5. create a single binary

Python application packaging problem has been around. There are multiple online tutorials dealing with a subset of the 
above requirements. `py2bin` shows how to address all of the above. 

# How to run

1. Clone the repository.
2. Make sure `numpy`, `sklearn` and `pyinstaller` are installed.
3. run `./compile.sh`
4. run `dist/main <integer>` e.g. `dist/main 20`