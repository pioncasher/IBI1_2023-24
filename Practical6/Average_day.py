# pseudocode 
# create a dictionary 
# print the dictionary
# generate pie plot
# given a request activity
# print time spent on it

import matplotlib.pyplot as plt
activity_time={"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1,"other":1.5}   
print(activity_time)

activity=activity_time.keys()
time=activity_time.values()
plt.figure()
plt.pie(time,labels=activity,startangle=90)
plt.show()
plt.clf()

act="Sleeping"   # the request activity
print("Time spent on " + act + " is "+str(activity_time[act])+" hours.")