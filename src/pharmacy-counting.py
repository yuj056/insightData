
# coding: utf-8

# In[6]:

#read txt file
with open('itcont.txt', "r") as f:
    data = f.readlines()
    
#extract drug_name and drug_cost
select_list = []
for line in data[1:]:
    drug_name_i = line.strip().split(",")[-2]#strip to remove \n
    drug_cost_i = float(line.strip().split(",")[-1]) # convert drug cost into float type
    select_list.append((drug_name_i,drug_cost_i)) 
    
# merge the rows with same drug name
combined_list = {}
for name, cost in select_list:
    if name not in combined_list:
        combined_list[name] = [cost]
    else:
        combined_list[name].append(cost)

newCombinedList = {k:sum(v) for k,v in combined_list.items()}
numb = [len(v) for k,v in combined_list.items()]

#convert the dictionary into list and add the number of prescriber
dictlist = []
i= 0
for name, cost in newCombinedList.iteritems():
    temp = [name, numb[i], cost]
    i= i+1
    dictlist.append(temp)
    
# sort the list by decend order of drug cost    
new_list = sorted(dictlist, reverse=True,key = lambda x: x[2])
with open('top_cost_drug.txt', 'w') as filehandle:  
    for listitem in new_list:
        filehandle.write('%s\n' % listitem)

