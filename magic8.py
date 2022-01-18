#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
#name of customer
name = "Anmol"

#question asked to Magic 8-Ball
question = "Is this real life?"

answer = ""

#generating random number
random_number = random.randint(1,9)

#Checking the random_number variable
print(random_number)

#Response by Magic 8-Ball
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

#if name/question is empty string
if name == "" and question == "":
  print("Enter name and question")
elif name == "": # if name is empty string
  print(question)
else:  
  print(name + " asks: " + question)

if question == "": #if question is empty string
  print("Enter the Question")
else:
  print("Magic 8-Ball's answer: " + answer)


# In[ ]:





# In[ ]:




