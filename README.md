# comscore coding challenge

To run the import tool ./importer.py {path/to/the/file}
The file must be pipe delimited

To run the query tool ./query.py -s Columns to SELECT -o (optional) Columns to Order By -f (optional) column and value to filter by
  some examples 
      ./query -s TITLE,REV,DATE -o DATE,TITLE
      ./query -s TITLE,REV,DATE -f DATE=2014-04-01
      
 The test suite for the importer can be found in testsuite.py     
