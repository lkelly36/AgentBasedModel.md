"""
Assignment 1 - GEOG5995 Programming for Social Scientists
Final Model
"""

# Import required libraries
            
import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

# Read the data into the environment

environment = []

dataset = open("in.txt", newline='')
reader = csv.reader(dataset, quoting=csv.QUOTE_NONNUMERIC)
    
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist) 
dataset.close() # Close the file

# Set values
num_of_agents = 50
num_of_iterations = 100
neighbourhood = 20
agents = []

# Make the agents using agentframework.py file.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))

# Move the agents, make them eat, calculate distance
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# Plot the graph
matplotlib.pyplot.xlim(0, 300) # x axis
matplotlib.pyplot.ylim(0, 300) # y axis
matplotlib.pyplot.imshow(environment)
      
# Set figure for animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True

# Define function for animation  
def update(frame_number):
    fig.clear()
    global carry_on
    
    #move, eat, calculate distance between eachother
    for j in range(num_of_iterations):
        random.shuffle(agents) # randomise
        for i in range(len(agents)):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    
    # stopping condition
    if len(agents)==0:
        carry_on=False
        print("Stopping condition ")
   
    #plots the agents as they move and represented by white dots 
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)  
    matplotlib.pyplot.imshow(environment)
        
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a			
        a = a + 1
        #print(carry_on)
        #print(a)
        
# animation
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 10000, frames= gen_function(), repeat=False)
matplotlib.pyplot.show()

# Save animation

animation.save('/Users/louisekelly/Desktop/python/Leeds/animation.gif', writer='writer', fps=60)

