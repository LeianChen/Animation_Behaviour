#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__ 0.1.0

"""

import random

class Agent():
    def __init__(self, environment, agents):
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)
        self.environment = environment
        self.store = 0
        self.agents = agents
    

    def move(self):

        if random.random() < 0.5:
            self.y = (self.y + 1) % 299
        else:
            self.y = (self.y - 1) % 299
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 299
        else:
            self.x = (self.x - 1) % 299

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                #print('other store: '+ str(agent.store))
                #print('own store: '+ str(self.store))
                
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                
                #print('other store: '+ str(agent.store))
                #print('own store: '+ str(self.store))
                #print('-------------------------------')
                #print("sharing " + str(dist) + " " + str(ave))
                # could try to remove the agent from agents list
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    

    
    
    
    