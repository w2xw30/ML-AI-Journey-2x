import math
from fractions import Fraction as F

def decimal_to_prob(d):
    return 1/d

def prob_to_decimal(p):
    return 1/p

def prob_to_odds(p):
    return (p/(1-p))

def odds_to_prob(o):
    return (o/(o+1))

def logit(p):
    return math.log(p/(1-p))

def sigmoid(z):
    return (1/(1+pow(math.e,-z))) 

def fractional_to_decimal(a, b):
    x = F(a,b)
    return float(x)

def decimal_to_fractional(d):
    return F(d)
