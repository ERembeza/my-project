# my-project
**The aim of the code is to list pH values of media of interests.**

The input file contains examples of data I worked on; it carries various information about microorganisms, among other things: url link to the website with culture media pdf files.

The first step is to download all media files.

The second step is to look for pH values in those files and write them down in a txt file.



Some of the packages used:
- **requests**: HTTP library, getting acces to url links
- **PyPDF2**: operation on pdf files, such as extracting text
