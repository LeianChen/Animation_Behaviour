# -*- coding: utf-8 -*-
"""
__version__ 0.1.0

"""

import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import requests
import bs4
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5



"""
a = agentframework.Agent()
print (a.y, a.x)
a.move()
print(a.y, a.x)
"""


############################################
######### Import environment ###########
########################################### 
#The pattern for dealing with looping 2D data 
        
environment = []
f = open('in.txt') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:	
    
    rowlist = []		
    for value in row:				
        rowlist.append(value)
        
    environment.append(rowlist)

f.close()

############################################
######### Import data HTML ###########
########################################### 
"""
f = open("data.html", "w")

f.write("<HTML>\n<BODY>\n")
f.write("<STYLE>\n")
f.write("TD {border: 1px solid black; padding: 15px;}\n")
f.write("TH {border: 1px solid black; padding: 15px;}\n")
f.write("</STYLE>\n")
f.write("<TABLE class=\'datatable\' id=\'yxz\'>\n")
f.write("<TR><TH>y</TH><TH>x</TH><TH>z</TH></TR>\n")

for i in range(100):
	y = random.randint(0,99)
	x = random.randint(0,99)
	z = random.randint(0,255)
	f.write("<TR><TD class=\'y\'>" + str(y) + "</TD>")
	f.write("<TD class=\'x\'>" + str(x) + "</TD>")
	f.write("<TD class=\'z\'>" + str(z) + "</TD></TR>\n")

f.write("</TABLE>\n</BODY>\n</HTML>")

f.close()
"""

#r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
#content = r.text
#soup = bs4.BeautifulSoup(content, 'html.parser')
#td_ys = soup.find_all(attrs={"class" : "y"})
#td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

############################################

num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20


############################################
######### Setting up matplotlib ###########
########################################### 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)



# Make the agents.
for i in range(num_of_agents):
#    y = int(td_ys[i].text)
#    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents))

#if (x == None):
#    self._x = random.randint(0,100)
#else:
#    self._x = x


carry_on = True


############################################
######### Call methods for each agent ######
########################################### 
#for j in range(num_of_iterations):
#Check if shuffle works
    #for k in range(num_of_agents):
        #print(agents[k].x,agents[k].y)
    #print ("shuffling...")

   # random.shuffle(agents)
#Check if shuffle works
    #for k in range(num_of_agents):
        #print(agents[k].x,agents[k].y)
    #print("----")
    


# check store of all agents
#for i in range(num_of_agents):
#    print(agents[i].store)


def update(frame_number):
    
    fig.clear()
#    matplotlib.pyplot.xlim(0, 299)
#    matplotlib.pyplot.ylim(0, 299)
#    matplotlib.pyplot.imshow(environment)

    global carry_on
    
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat() #call eat for each agent
        agents[i].share_with_neighbours(neighbourhood)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    


############################################
######### Mapping the environment ###########
########################################### 
"""
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(299, 0)
matplotlib.pyplot.imshow(environment)
"""



def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1



def run():
    #animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=10, repeat=False)
    canvas.show()

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()




#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#matplotlib.pyplot.show()



###########################################################
######### Building neighbourhood method in Agent ##########
########################################################## 
"""
# Loop through the agents in self.agents .
    # Calculate the distance between self and the current other agent:
    distance = self.distance_between(agent) 
    # If distance is less than or equal to the neighbourhood
        # Sum self.store and agent.store .
        # Divide sum by two to calculate average.
        # self.store = average
            # agent.store = average
    # End if
# End loop
"""






"""
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
"""