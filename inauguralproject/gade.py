import numpy as np
import scipy.optimize as opt


# Defining utility

def utility(c,v,l,eps):
    u = np.log(c) - v*(l**(1+1/eps)/(1+1/eps))
    return u

# Defining constraint

def eq(m,w,l,tau_0,tau_1,kappa):
    x = m + w*l - (tau_0*w*l + tau_1*np.max(w*l-kappa,0))
    return x


def choice(l,w,eps,v,tau_0,tau_1,kappa):
    c = eq(m,w,l,tau_0,tau_1,kappa)
    return -utility(c,v,l,eps)


def optimizer(w,eps,v,tau_0,tau_1,kappa,m):
    res = opt.minimize_scalar(
    choice, method='bounded',
    bounds=(0,1), args=(w,eps,v,tau_0,tau_1,kappa))
    
    l_star = res.x
    c_star = eq(m,w,l_star,tau_0,tau_1,kappa)
    utility_star = (c_star,l_star,v,eps)
    
    return l_star,c_star,utility_star