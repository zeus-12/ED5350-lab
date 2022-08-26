
# In[20]:


def cal_sum(a,b):
    return a+b
print(cal_sum(5,7))


# In[4]:


print(cal_sum('a','b'.upper()))


# In[21]:


a,b=str(1),'a'
print(cal_sum(a,b))


# In[22]:


#positional arguments cannot foloow keyword arguments


# In[23]:


def pos_fun(i,f,st):
    i=100
    su1=i+f
    st1=st.upper()
    return su1,st1
i=10
out_fun=pos_fun(i,f=20.3,st='t')
print(out_fun)


# In[26]:


def var_arg(*arg):
    for var in arg:
        print(var,type(var))
var_arg('a',1,2)


# In[27]:


lst=[1,2,3]
var_arg(lst)


# In[28]:


var_arg(*lst)


# In[29]:


tup=(1,2,3)
var_arg(tup)


# In[30]:


var_arg(*tup)


# In[31]:


def kwar_arg(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
kwar_arg(i=10)
kwar_arg(i=10,j=20.4)
kwar_arg(i=10,j=10.6,k='t')


# In[ ]:


#suppose we have variable length position and variable length keyword and simple positional and simple keyword , then 
#

