# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:05:10 2020

@author: cbony, msnyder
"""

from random import randint
from fractions import Fraction


#definitions
problems_per_section = 2

hyp = randint(1,30)
adj = randint(1,hyp)
random_value = randint(1,10)

problems = {
        '5.1a' :
            [
                    (f'Find an angle A degrees that is coterminal with an angle measuring {randint(-720,0)} degrees, where 0 <= A < 360.', 1),
                    (f'Find an angle A degrees that is coterminal with an angle measuring {randint(360,1080)} degrees, where 0 <= A < 360.', 3),
                    (f'Find an angle A degrees that is coterminal with an angle measuring {Fraction(randint(-24,0),12)} * pi, where 0 <= A < 2pi.', 0),
                    (f'Find an angle A degrees that is coterminal with an angle measuring {Fraction(randint(24,72),12)} * pi, where 0 <= A < 2pi.', 0),
                    (f'If angle A = {360*randint(-48,72)/24} degrees, what is the measurement of A in radians? Give an exact answer.', 0),
                    (f'If angle A = {Fraction(randint(24,72),12)} * pi radians, what is the measurement of A in degrees? Give an exact answer.', 0),
                    (f'Which quadrant does the angle {randint(-360,360)} degrees terminate in when drawn in the standard position?', 0),
                    (f'Which quadrant does the angle {Fraction(randint(-24,24),12)} * pi terminate in when drawn in the standard position?', 3),
                    (f'Approximate a drawing of the angle {randint(-360,360)} degrees in standard position.', 0),
                    (f'Approximate a drawing of the angle {Fraction(randint(-24,24),12)} * pi radians in standard position.', 1)
            ],
        '5.1b' :
            [
                    (f'The radius of the wheel on a car is {randint(8,23)} inches. If the wheel is revolving at {randint(200,1400)} revolutions per minute, what is the linear speed of the car in miles per hour? Round to the nearest tenth.', 3),
                    (f'Find the area of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {Fraction(randint(0,24),12)} * pi radians. Round answer to the nearest tenth.', 2),
                    (f'Find the area of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {randint(0,360)} degrees. Round answer to the nearest tenth.', 1),
                    (f'Find the length of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {Fraction(randint(0,24),12)} * pi radians. Round answer to the nearest tenth.', 1),
                    (f'Find the length of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {randint(0,360)} degrees. Round answer to the nearest tenth.', 1)
            ],
        '5.2b' :
            [
                    (f'If the terminal side of an angle θ intercepts the unit circle when y is magnitude {["1/2","1/2**(1/2)","3**(1/2)/2"][randint(0,2)]} in quadrant {randint(1,4)}, what is the angle measure of θ?',1),
                    (f'The terminal side of angle θ intersects the unit circle in quadrant {randint(1,4)} at {["x","y"][randint(0,1)]} value {Fraction(randint(1,random_value),random_value)}. What are the exact values of sinθ and cosθ?',3),
                    (f'If the terminal side of angle t goes through the point ({adj}/{hyp},({(hyp**2-adj**2)}**(1/2))/{hyp}) on the unit circle, then what is {["sin(t)","cos(t)"][randint(0,1)]}?',4)
            ]
        }
    
#jank code.
    
#preset
problem_number = 0


for section in problems.keys():
    print(section)
    
    selection = problems[section]
    
    possible_problems = []
    
    max_right = 0
    min_right = -1
    
    #get maximum
    for item in selection:
        if item[1] > max_right:
            max_right = item[1]
        if item[1] < min_right or min_right == -1:
            min_right = item[1]
    
    #give the possibility of decent practice
    max_right += 1
    
    #create random array of problems
    for item in selection:
        for i in range(0,max_right-item[1]):
            possible_problems.append(item[0])
            
    #print the problems.
    for i in range(0,problems_per_section):
        #reset variables
        hyp = randint(1,30)
        adj = randint(1,hyp)
        random_value = randint(1,10)
        
        problem_choice = randint(0,len(possible_problems)-1)
        problem_number += 1
        print(str(problem_number)+'.\t'+possible_problems.pop(problem_choice))
