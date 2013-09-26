#from stackoverflow/python2to3
#used to run python scripts interactively in the shell
def execfile(thefile, global_vars=None, local_vars=None):
   with open(thefile) as f:
       code = compile(f.read(), thefile, 'exec')
       exec(code, global_vars, local_vars)
#shorter name
def xfile(thefile, global_vars=None, local_vars=None):
   with open(thefile) as f:
       code = compile(f.read(), thefile, 'exec')
       exec(code, global_vars, local_vars)
       
#needs work: want to be able to setup variables, extract from array
#for key in global_vars.keys():
#  key = global_vars[key]
#for key in local_vars.keys():
#  key = local_vars[key]
