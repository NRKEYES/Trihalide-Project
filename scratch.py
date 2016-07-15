







# Main Logic

# Create all the job values

count = 0
for R1 in bondRange1:
	for R2 in bondRange2:
		for A in anglesRange:
			JobList[count]= [R1,R2,A]

			count = count + 1

#print JobList

SubmittedJobs = 0
CompletedJobs = 0
RunningJobs = np.zeros((6,3)) # first number is based on queue limit for system


while CompletedJobs < TotalNumberOfJobs: 

	#Check which jobs are still running
	for i , job in enumerate(RunningJobs):

		#Check if a specificly named job is running, techinically returns number of times it is running.
		currentCL = sub.Popen(['qstat | grep -c '+ Name(job)], shell = True, stdout = sub.PIPE)
		running, error = currentCL.communicate()



		if int(running) != 0: #string must me cast to int here. Check that at least one instance is queued
			print str(job) + 'running' #This job is still running move on
			continue

		else: #This job is dead,submit next job


			if Name(job) != Name([0.0,0.0,0.0]): # Check to make sure it wasn't a NULL JOB
				print str(job) + "Job's Done!"

				try:
					sub.check_output(["cp",Name(job)+".out","output/"+Name(job)+".out"])  # copy output file into place
					sub.check_output(["rm "+Name(job)+"*"], shell = True)
					RunningJobs[i]= [0,0,0] #blanks out running spot, needed for end of queue
					CompletedJobs = CompletedJobs + 1
				
				except sub.CalledProcessError as e:
					print e.output


			if SubmittedJobs < TotalNumberOfJobs:
				SubmitJob(SubmittedJobs)
				RunningJobs[i] = JobList[SubmittedJobs]
				SubmittedJobs = SubmittedJobs + 1

			else:
				#all jobs have been submitted
				pass

		time.sleep(1)

	sub.Popen(['clear'])
	
	print "Completed Jobs:" + str(CompletedJobs)
	print RunningJobs
	
	time.sleep(10)
    