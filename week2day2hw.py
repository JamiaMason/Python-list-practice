#Given a list as a parameter, write a function that returns a list of numbers that 
#less than 10

#steps: 
#create a list
list = [1,11,14,5.8,9]
for i in list:
      if i < 10:
         print(i)


#Write a function that takes in two lists and returns the two lists 
# merged together and sorted

#please let me know how to make comments without hashtag

list = [1,2,3,4,5,6]
sorted_tup = sorted(list)

another_list = [3,4,5,6,7,8,10]
combine_list = sorted_tup + another_list

changedtup = tuple(combine_list)


print(combine_list)
print(sorted_tup)
