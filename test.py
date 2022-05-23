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
    failure = systempipe(self.command)
    return failure==0
  
  def extract_deps (self, mo):
    output_filename = mo.group(1)
    input_filename = "%s.c" % output_filename
    self.command = "gcc %s -o %s" % (input_filename, output_filename)
    return [input_filename]
  

add_recipe(RecipeC)
set_default("hello")

main()

