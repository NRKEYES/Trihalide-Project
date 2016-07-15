import pandas as pd
import numpy as np
import time

import watcher


This is a test

class Wizard():
    #data frame

    def __init__(self, minima_filename= 'minima.geom' , atoms= []):   
        # Set up watcher
        TheWatch = watcher.Watcher()


        self.atoms = atoms

        # Data frame, starting points. aka MINIMA
        self.starting_points = self.read_minima(minima_filename = minima_filename, num_atoms = len(atoms))

        # Data frame, wanted points aka TBCaclulated- Perhaps this could just be the same as starting points?
        # Data frame, calculated points(including minima)

    def read_minima(self, minima_filename ='minima.geom',num_atoms = 3):
        minima = []
        
        num_lines = sum(1 for line in open(minima_filename))

        ######## POSSIBLE BUG IF MISSING BLANK LINE AT END OF FILE---Could be fixed by rounding up
        num_minima = num_lines/(num_atoms + 1)
        #print num_minima

        for j in range(0, num_lines, num_atoms + 1 ):
            with open(minima_filename, 'r') as f:

                data_frame_temp = pd.read_csv(f, nrows = 3,
                                                    skiprows = j,
                                                    header = None,
                                                    index_col = 0)
                #print data_frame_temp
                minima.append(data_frame_temp)

        f.close()
        return minima

        def generate_points(self):
            #Based on minimia generate other points to check.
            pass
        
        def queue_manager(self):
            #acutally queue the job and run it
            # Copy files back and forth- This is essentially Watcherv3

            # call PROCESS on each completed job

            pass

        def process(self):
            pass

        def visualize(self):
            #Print pretty output here
            pass
              
        def map_pes(MAXIMUM_JOBS):
            jobs = 0

            while jobs < MAXIMUM_JOBS:
                generate_points()
                queue_manager()
                
                visualize()

                sleep(10)



            




#data_frame of minima geomtries. I have to find some global frame of reference for this.
#
# Chart most direct path between minima
#
# Submit jobs along path
# Jobs around the well



atoms = ['Br','F','Cl']

run1 = Wizard(atoms = atoms, minima_filename = 'minima.geom')

print run1.starting_points



