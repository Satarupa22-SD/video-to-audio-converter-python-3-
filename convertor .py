#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install moviepy


# In[1]:


import moviepy.editor


# In[2]:


from tkinter.filedialog import *


# In[3]:


video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio


# In[ ]:


audio.write_audiofile("sample.mp3")
print("Completed!")


# In[ ]:




