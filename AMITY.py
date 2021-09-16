

import pylab as plt
from blimpy import Waterfall


# In[6]:


file_path = 'Voyager1.single_coarse.fine_res.h5'
obs = Waterfall(file_path)


# In[7]:


obs.info()


# In[8]:


print(obs.header)
print(obs.data.shape)


# In[13]:


obs.plot_spectrum(logged=True)


# In[17]:


obs.plot_spectrum(f_start=8419.2740, f_stop=8419.2750)
#plt.savefig("test1.png")


# In[18]:


obs.plot_waterfall(f_start=8419.2740, f_stop=8419.2750)
plt.savefig("Q216.png")


# In[ ]:




