
from collections import Counter
def daily_participants(participants_list):
    dicty = {}
    lst = []
    ans = []
    for i in range(len(participants_list)):
        lst.append(0)
    for i in range(len(participants_list)):
        for j in range(len(participants_list[i])):
            if participants_list[i][j] not in dicty:
                dicty[participants_list[i][j]] = 0

    for name in dicty:
        flag = 0
        for i in range(len(participants_list)):
            if name not in participants_list[i]:
                flag = 1
        if flag is 0:
            ans.append(name)

    return ans






def one_time_participants(participants_list):
  all=participants_list[0:]
  s=[]
  s1=[]
  for list in participants_list[0:]:


    for element in list:
      s.append(element)
  
  

  
  dictOfElems = dict(Counter(s))

  dictOfElems = { key:value for key, value in dictOfElems.items() if value== 1}
  for key, value in dictOfElems.items():


    final=[]
    final.append(key)
    print(final,end="")

def first_day_only_participants(participants_list):
    firstlist=participants_list[0]
    lastlist=participants_list[1:]
    all=participants_list[0:]


    s=[]
    s1=[]

    for list in participants_list[:1]:


      for element in list:
        s.append(element)
    for list in participants_list[1:]:


      for element in list:
        s1.append(element)    

    for i in range(0,len(s)):
      if s[i] not in s1:
        
        assu=[]
        assu.append(s[i])
        print(assu,end=" ")
        
       
      

          
      
participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]

print("All the Daily participants:")

print(daily_participants(participants_list))
print('\n')
print("All the One time participants:")
one_time_participants(participants_list)
print('\n')
print("All the First Day participants:")
first_day_only_participants(participants_list)



