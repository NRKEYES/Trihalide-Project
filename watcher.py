import time
import numpy as np
import subprocess as sub
from string import Template


class Watcher(object):
    def __init__(self,MaximumJobsToQueue = 40):
        self.MaximumJobs= MaximimJobs

        # Set up calculation details
        functional = "B3LYP"
        basisSet = "DefBas-6"	
        # Set up points to 
        bondRange1 = np.linspace(1.6, 8, 30) #angstrom 5 steps
        bondRange2 = np.linspace(1.6, 8, 30)  #angstrom
        anglesRange =np .linspace(0,180, 10) #Degrees

        #Set up for loop control.
        TotalNumberOfJobs = bondRange1.size * bondRange2.size * anglesRange.size
        JobList = np.zeros((TotalNumberOfJobs, 3))
            
        print "Welcome to the watch!"

    def WriteFiles(R1,R2,A, name):
        #Write the input file first
        # Read in input template
        with open('input.template','r') as template:
            temp = template.read()
            s = Template(temp)
            with open( name+'.inp' , 'w') as f:
                out = s.substitute(Level = functional,
                Basis = basisSet,
                B1 = R1,
                B2 = R2,
                A1 = A)

                f.write(out)

        #Write Orca Submit File 

        with open('submit.template' , 'r') as template:
            
            contents = template.read()
            s = Template(contents)
            substituted = s.substitute(JobName = name,
                                        InputName= name+'.inp',
                                        OutputName = name + '.out') 

            with open('orca.pbs', 'w') as f:
                f.write(substituted)


        return
    

    def Name(data): # Helper function to generate names uniformly
        first = str(data[0])[0:4]
        second = str(data[1])[0:4]
        third = str(data[2])[0:4]

        return first+'-'+second+'-'+third



    def add_tasks(self):
        pass

    def SubmitJob(num):
        WriteFiles(JobList[num][0],JobList[num][1],JobList[num][2], Name(JobList[num]))
        sub.check_output(['qsub','orca.pbs'])   #submit job

        return

    def clean_Up(self):
        print str(job) + "Job's Done!"

        try:
            sub.check_output(["cp",Name(job)+".out","output/"+Name(job)+".out"])  # copy output file into place
            sub.check_output(["cp",Name(job)+".gbw","gbw/ ."])
            sub.check_output(["rm "+Name(job)+"*"], shell = True)
            RunningJobs[i]= [0,0,0] #blanks out running spot, needed for end of queue
            CompletedJobs = CompletedJobs + 1
                    
        except sub.CalledProcessError as e:
            print e.output



    def check_running_tasks(self):
        for i , job in enumerate(RunningJobs):
        
            #Check if a specificly named job is running, techinically returns number of times it is running.
            currentCL = sub.Popen(['qstat | grep -c '+ Name(job)], shell = True, stdout = sub.PIPE)
            running, error = currentCL.communicate()



            if int(running) != 0: #string must me cast to int here. Check that at least one instance is queued
                print str(job) + 'running' #This job is still running move on
                continue

            else: #This job is dead,submit next job


                if Name(job) != Name([0.0,0.0,0.0]): # Check to make sure it wasn't a NULL JOB
                    clean_up(job)


                if SubmittedJobs < TotalNumberOfJobs:
                    SubmitJob(SubmittedJobs)
                    RunningJobs[i] = JobList[SubmittedJobs]
                    SubmittedJobs = SubmittedJobs + 1

                else:
                    #all jobs have been submitted
                    pass














