import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='tanayResume',
     version='0.01',
     scripts=['tanayResume'] ,
     author="Tanay Mehta",
     author_email="tanaymehta28@gmail.com",
     description="Python Installable Resume of Tanay Mehta",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/heytanay",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
