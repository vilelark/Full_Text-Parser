import os
import Checkfile
import Parser

check = Checkfile.all_dir_name(os.getcwd())
correctdir = Checkfile.correct_dir(check)

Checkfile.last_file(correctdir)

Parser.Fetch('http://www.google.com/googlebooks/uspto-patents-grants-text.html')