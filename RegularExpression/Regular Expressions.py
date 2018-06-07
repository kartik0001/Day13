
# coding: utf-8

# In[2]:


'''
Q.1- Extract the user id, domain name and suffix from the following email addresses. 
emails = "zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"
desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'),
('jeff42', 'amazon', 'com')]
'''

desired_output=[]
import re
tup_1=(tuple)(re.split("\W","zuck26@facebook.com"))
tup_2=(tuple)(re.split("\W","page33@gmail.com"))
tup_3=(tuple)(re.split("\W","jeff42@amazon.com"))
desired_output.append(tup_1)
desired_output.append(tup_2)
desired_output.append(tup_3)
print("The desired output is:")
print(desired_output)


# In[4]:


'''
Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
text = "Betty bought a bit of butter, But the butter was so bitter,
So she bought some better butter,
To make the bitter butter better."
'''

text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
import re
matcher=re.finditer('[bB]',text)
count=0
for m in matcher:
    count=count+1
    print('Match is at: {}, End: {}, Pattern found is: {}'.format(m.start(), m.end(), m.group()))
print('Total count is: ',count)


# In[9]:


'''
Q.3- Split the following irregular sentence into words 
sentence = "A, very very; irregular_sentence"
desired_output = "A very very irregular sentence"
'''
desired_output=[]
import re
list=(re.split("[,;_]","A, very very; irregular_sentence"))
print('Irregular Sentence:',list)
for i in list:
    print(i+" ",end="")


# In[13]:


'''
Q.1- Clean up the following tweet so that it contains only the user’s message.
That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
tweet = ''Good advice! RT @TheNextWeb: What I would do differently if 
I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'' 
desired_output = 'Good advice What I would do differently if I was learning to code today'
'''
import re
tweet= "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
print("The Tweets:\n",tweet)
str1=re.sub('http[\S]*','',tweet)
str1=re.sub('#[\w]*','',str1)
str1=re.sub('@[\w]*','',str1)
str1=re.sub('[,.;:\'!?]','',str1)
str1=re.sub('RT','',str1)
str1=re.sub('cc','',str1)    
print("Output:\n",str1)

