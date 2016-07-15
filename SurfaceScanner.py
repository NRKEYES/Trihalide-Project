import numpy as np
import pandas as pd





#
# PEON 
#   Creats actual job file for a given calculating and subits to appropiratie suite.
#   checks the calculation for good internal behaviour, convergence etc.
#   If behaviour looks good return the value to WIZARD, 
#

class Job(object): #Peon class
    
    #Get passed a list of atoms and their geometries. Internal? Cartesian? Cartiesian would we the easiest to pass around as a simple list...
    def __init__(self, geometry =[], ):












#
# OVERSEER
#
# Limits the numbers or jobs that are active at any given time. Has a list of all the tasks that WIZARD wants completed. 
# 
#


# Intilize atoms

atoms = ['Br','F','Cl']



#
# WIZARD
#
# Decides on what jobs need to be calulated, resposible for scanning the space of interest.
# Each job is then sent to OVERSEER for dispatching.
#