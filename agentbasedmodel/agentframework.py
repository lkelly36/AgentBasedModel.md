"""
Assignment 1 - GEOG5995 Programming for Social Scientists
Agent Class Framework
"""

# Import required library

import random

# Create agent class.
# All agents must move, eat and share resources with nearby neighbours.

class Agent():
    def __init__(self, environment, agents, neighbourhood):
        self._x=(random.randint(0,len(environment))) # random starting point based on environment
        self._y=(random.randint(0,len(environment)))
        self.environment = environment
        self.agents= agents
        self.neighbourhood=neighbourhood
        self.store = 0
    
#make agents move, using torus to return agents to the environment
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300

        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
          
# make agents eat the environment
    def eat(self): 
        if  self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
             self.environment[self._y][self._x] -= self.environment[self._y][self._x]
             self.store += self.environment[self._y][self._x]
             
# define function for calculating distance between agents
    def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a._x - agents_row_b._x)**2) + 
        ((agents_row_a._y - agents_row_b._y)**2))**0.5
             
# share resources with nearby neighbours
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            # prevent agent from comparing to themselves
            if agent==self:
                continue
            distance = self.distance_between(agent) 
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = int(sum /2)
                self.store = average
                agent.store = average