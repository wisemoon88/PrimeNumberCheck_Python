#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_primes(num):
    numberlist = list(range(3,num+1,2))
    print(numberlist)
    placeholder = [2]
    for i in numberlist:
#        if num % i != 0:
            for y in numberlist:
                if i%y == 0:
                    if i != y:
                        break
                    else:
                        placeholder.append(i)
                
       
    print(placeholder)
    return len(placeholder)    
    pass

