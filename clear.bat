attrib +r *.tex
attrib +r *.bat
attrib +r *.bib
attrib +r .gitignore
attrib +r .gitattributes
del /q *
attrib -r *.tex
attrib -r *.bat
attrib -r *.bib
attrib -r .gitignore
attrib -r .gitattributes