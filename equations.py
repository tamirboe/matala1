# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:11:18 2021
@author: Tamir
"""




def exponent(x:float) ->float:
    ex=1.0
    num=100        
    for b in range(num):
        num2=1
        if b==0:
            continue
        for j in range(b):
                  j=j+1
                  num2=num2*j

        num3=x
        for a in range(b):
            if a==0:
                continue
            else:
                num3=num3*x
        ex= ex + (num3/num2)
    return ex


 
def Ln(x:float)  -> float:
    epsilon = 0.001
    
    if x<0 :
        x=x*-1
    yn= x-1.0
    ee = exponent(yn)
    yn1= yn +2*((x-ee)/(x+ee))
    yabss = yn - yn1
    if (yabss ) < 0:
        yabss= yabss*-1
        
    while (yabss) > epsilon:
        ee = exponent(yn)
        yn = yn1
        yn1= yn +2*((x-exponent(yn))/(x+exponent(yn)))
        yabss = yn - yn1
        if (yabss ) < 0:
            yabss= yabss*-1  
    return yn1
    

def XtimesY(x:float,y:float) ->float:
    xy = exponent(y*Ln(x))
    if (x<0) :
        return(0)
    elif x==0:
        return(0)
    else:
        return(xy)
    
   
    
def sqrt(x:float,y:float) ->float:
    #xy = exponent((1/x)*ln(y))
    if (y<=0):
        return(0)
    #elif y==0:
    #    return(0)
    else:
        return(exponent((1/y)*Ln(x)))


def calculate(x:float) ->float:
    cal = exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x) 

    return cal
    #exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x) 
