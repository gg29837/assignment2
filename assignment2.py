#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# 
# ---
# 
# Complete the Python functions below, test your code, then commit the changes to this file to the repository and push it to [Github](https://github.com) for submission.

# # Problem 1
# 
# Complete the function such that its output is the square of $a$

# In[2]:


def square(a):
    ans = a**2
    return ans


# # Problem 2
# 
# Given a mathematical function $x(t) = 5 t$, write a Python function that returns an estimate to the first derivative of $x$ at a given point $t$ using the following finite-difference formula
# 
# $$\frac{\partial x}{\partial t} \approx \frac{\Delta x}{\Delta t} = \frac{x(t+\Delta t) - x(t)}{\Delta t}$$
# 
# $\Delta t$ is a user provided argument to the function.

# In[3]:


def finite_diff(t, delta_t):
    x = 5*t
    derivative_of_x = (5*(t+delta_t)-5*t)/delta_t
    return derivative_of_x


# # Problem 3
# 
# Write a function that takes in a productivity index of a well $J$ in (ft$^3$/psi-day), a bottomhole pressure $P_{wf}$ (psi), and an initial pressure $P_i$ (psi) and returns the initial production rate $q_w$ in BBLs/day.
# 
# Give a default argument to $P_{wf}$ such that if it is omitted from the function argument list then $P_{wf} = 2000$ (psi). 
# 
# Recall that
# 
# $$
# q_w = J (P_i - P_{wf})
# $$
# 
# you may need a conversion factor.

# In[1]:


def well(J, Pi, Pwf=2000):
    qw = (J/5.61458)*(Pi-Pwf)
    return qw


# In[ ]:




