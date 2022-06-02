#!/usr/bin/env python3

from makeish import *
from subprocess import Popen, STDOUT, PIPE

def systempipe (command, logfile='makeish.log'):
    p = Popen('%s >> %s 2>&1' % (command, logfile), shell=True, stderr=STDOUT, stdout=PIPE)
    return_code = p.wait()
    return return_code

class RecipeC (Recipe):
  pattern = re.compile("(.+)")
  
  def __init__ (self, target):
    super(RecipeC, self).__init__(target)
  
  def build_linux(self):
    retcode = systempipe(self.command)
    return "new" if retcode==0 else "error"
  
  def extract_deps (self, mo):
    output_filename = mo.group(1)
    input_filename = "%s.c" % output_filename
    self.command = "gcc %s -o %s" % (input_filename, output_filename)
    return [input_filename]
  

class RecipeTex (Recipe):
  pattern = re.compile("(.+).pdf$")
  
  def __init__ (self, target):
    super(RecipeTex, self).__init__(target)
  
  def build_linux(self):
    retcode = systempipe(self.command)
    print("retcode", retcode, type(retcode))
    return "new" if retcode==0 else "error"
  
  def extract_deps (self, mo):
    basename = mo.group(1)
    input_filename = "%s.tex" % basename
    self.command = "pdflatex -shell-escape %s" % (input_filename)
    return [input_filename]
  

add_recipe(RecipeC)
add_recipe(RecipeTex)
set_default(["hello", "document.pdf"])

main()

