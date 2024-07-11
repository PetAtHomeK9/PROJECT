#List can be mutable and allow duplicate value
This_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4]
print(This_List)
This_List.append(11)
print(This_List)
This_List.reverse()
print(This_List)

This_List = ["Franklin", "Emmanuel","Oluwabukunmi","PetAtHome k9"]
print(This_List)
This_List.append(11)
print(This_List)
This_List.reverse()
print(This_List)


#Tuple allow duplicate value but not mutable
This_Tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4)
print(This_Tuple)
This_Tuple.count(4)
print(This_Tuple)

This_Tuple = ["Franklin", "Emmanuel","Oluwabukunmi","PetAtHome k9"]
print(This_Tuple)


#Set can not be mutable and doesn't accept duplicate value
This_Set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4}
print(This_Set)

This_Set = {"Franklin", "Emmanuel","Oluwabukunmi","PetAtHome k9"}
print(This_Set)


#Dict can not be mutable and does not allow duplicate value
This_Dict = {"Name" : "Franklin", "Sex" : "Male", "Zodiac" : "Libra","Name" : "Franklin"}
print(This_Dict)

This_Dict = {"Name" : "Franklin", "Sex" : "Male", "Zodiac" : "Libra"}
print(This_Dict)