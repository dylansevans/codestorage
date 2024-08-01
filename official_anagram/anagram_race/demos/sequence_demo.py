#Sequence Data Types: Strings, Lists, Tuples
magic_word = "bananas" #str - can use a variety of quotes
numbers_list = [1234, 12345, 2468, 9999, 11111, 90] #list - uses [ ]
numbers_tuple =  (1234, 12345, 2468) #tuple - uses ( )

#Finding the Length of a Sequence: len()
len(magic_word)    #7            
len(numbers_list)  #6         
len(numbers_tuple) #3

#Strings and Tuples are immutable.
#magic_word[3] = "i"       #error			
numbers_list[3] = 24601   #OK		
#numbers_tuple[3] = 24601  #error

#Sequence Slicing
magic_word[2]     #"n"
magic_word[-1]    #"s"
magic_word[2:5]   #"nan"
magic_word[2:]    #"nanas"
magic_word[1::2]  #"aaa"
magic_word[::-1]  #"sananab"

numbers_list[2]     #2468
numbers_list[-1]    #90
numbers_list[2:5]   #[2468, 9999, 11111]
numbers_list[2:]    #[2468, 9999, 11111, 90]
numbers_list[1::2]  #[12345, 9999, 90]
numbers_list[::-1]  #[90, 11111, 9999, 2468, 12345, 1234]

numbers_tuple[2]     #2468
numbers_tuple[-1]    #2468
numbers_tuple[2:5]   #error
numbers_tuple[2:]    #(2468,)
numbers_tuple[1::2]  #(12345,)
numbers_tuple[::-1]  #(2468, 12345, 1234)

#Modifying Sequences
magicWord = magic_word*3  #"bananasbananasbananas"
print(magicWord)
negatives = [-1] * 5     #[-1, -1, -1, -1, -1]
numbers2 = numbers_list + [3333] #[1234, 12345, 2468, 3333]
numbers_list.append(3333)  #[1234, 12345, 2468, 3333]
