Author: Cibin Joseph (https://github.com/cibinjoseph)

Instructions to generate .md documentation files for JSON API links
---------------------------------------------------------------------

1. Generate the template .md file
  a. Running generateDocs.py generates all template files 
     in the current working directory.
  b. For minor changes, edit the .md files directly.
  c. To add a newly created api link, add it to the variable 
     'api' in generateDocs.py along with its filename.

2. Add additional information to the template files
  a. Once the .md files are generated, add a dataset title 
      to the header of the file.
  b. Any other extra information may be added in the tables.



Notes on working
------------------

generateDocs.py creates individual .md files by parsing the JSON api links. 
The JSON api links have to be provided inside generateDocs.py.
Each .md file contains 3 sections:
1. A header
2. A tree for depicting json hierarchy
3. A table for variable details

generateDocs.py utilizes the module json2tree for creating the 
hierarchy tree and the table for variables.
