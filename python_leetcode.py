Python Leetcode Interview Questions

1. https://leetcode.com/problems/nim-game/
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.

Soln -
You can always win a Nim game if the number of stones nn in the pile is not divisible by 44.

Reasoning

Let us think of the small cases. It is clear that if there are only one, two, or three stones in the pile, and it is your turn, you can win the game by taking all of them. 
Like the problem description says, if there are exactly four stones in the pile, you will lose. 
Because no matter how many you take, you will leave some stones behind for your opponent to take and win the game. 
So in order to win, you have to ensure that you never reach the situation where there are exactly four stones on the pile on your turn.

Similarly, if there are five, six, or seven stones you can win by taking just enough to leave four stones for your opponent so that they lose. 
But if there are eight stones on the pile, you will inevitably lose, because regardless whether you pick one, two or three stones from the pile, 
your opponent can pick three, two or one stone to ensure that, again, four stones will be left to you on your turn.

It is obvious that the same pattern repeats itself for n=4,8,12,16,\dotsn=4,8,12,16,…, basically all multiples of 44.

def canWinNim(self, n: int) -> bool:
	if n%4 == 0:
		return False
	else:
		return True			 
		

2. 
String function summary : 

s.count('st')
s.count('st', 3, 8)  #search between posn '3' and '8'

s.replace('st','tu')
s.replace('st','tu',1)

s.rjust(30)     #space padding
s.rjust(30,'0') #0 padding

s.split()
s.split('-', 3) #split with separator '-' and into at most 3 parts
s.splitlines()

s.find('st')  #if no match then return -1
s.index('st') #if no match then Error
s.find('st',3,8)  #find between posn 3 and 8
s.index('st',3,8)  #find between posn 3 and 8

s.strip()    
s.lstrip()
s.rstrip()

s.endswith('st')

'13'.isdigit()      #returns True
'HELLO'.isupper()   #returns True

s.join('st')        # same as s + 'st'
s.join('st','#')    # same as s + '#' + 'st'

max(s) 
min(s)

3.
Dictionary

'a' in mydict          		      	   #test presence of key 
mydict.has_key('a')   		      	   #test presence of key 
'b' in mydict.values() 		      	   #test presence of Values
Mydictionary.get(‘2’, “no key found”)  #get value for a key
len(mydict)                            #number of keys in dictionary
newDict=mydict.copy()     	      	   # a separate copy of the dictionary
del x[‘alpha']      				   # to delete a key
mydict.update(newdict)				   #add/update values from newdict into mydict
mydict.keys() 						   #gives keys of dictionary
mydict.values() 					   #gives values of dictionary
mydict.items() 					   	   #gives list of tuples of form (key,Value).
mydict.setDefault('a':1)    		   #default value of key 'a' if no value passed in dict
sorted(mydict)              		   #sorts on keys and returns a list of keys in sorted manner
sorted(mydict.values())	    		   #returns a list containing sorted values/
cmp(mydict,newDict)         		   #compares 2 dictionary
str(mydict)                 		   #Produces a printable string representation of a dictionary



4.
The following are totally acceptable in python:

passing a string representation of an integer into int
passing a string representation of a float into float
passing a string representation of an integer into float
passing a float into int
passing an integer into float
But you get a ValueError if you pass a string representation of a float into int, or a string representation of anything but an integer (including empty string). 
>>> int('5.0')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '5.0'


5. String to Integer (atoi)
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or 
if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
			 
Tricky Test cases:
" "
"+1 "
" 3.124"
"91283472332"

Soln.
class Solution:
    def myAtoi(self, mystr: str) -> int:
        
        if isinstance(mystr, str):
            if len(mystr.lstrip())==0:
                return 0
            else:
                newstr = mystr.lstrip()
                if newstr[0] in ('-','+') or newstr[0].isdigit():
                    
                    start_pos = 0
                    end_pos = 0
                    
                    print (start_pos, end_pos)
                    for i in newstr[1:]:
                        if i.isdigit():
                            end_pos = end_pos + 1
                            print (start_pos, end_pos)
                        else:
                            break
                    
                    print ("new_str ", newstr[start_pos:end_pos+1])
                    try:
                        if int(newstr[start_pos:end_pos+1]) <-2147483648:
                            return -2147483648
                        elif int(newstr[start_pos:end_pos+1]) >=2147483648:
                            return 2147483647
                        else:                       
                            return int(newstr[start_pos:end_pos+1])
                    except:
                        return 0

                else:
                    #first digit not +/-/number
                    return 0
                        
        else:
            return 0
        
		

6. List

mylist.count('a')    		#how many times 'a' has appeared in list
mylist.index(6)     		#search for value at posn 6
mylist.append(4)     		#append adds value at END
mylist.insert(2,'a') 		#insert value 'a' at posn '2'
mylist.extend(['c','d')		#extend list = concat 2 lists
mylist.pop()    			#delete by Posn - delete last element and return deleted ELEMENT.
mylist.pop(2)				#delete by posn - delete element at posn 2 and return deleted ELEMENT.
del mylist[2]				#delete by posn - delete element at posn 2 and return LIST after deletion.
remove mylist['a']			#delete by value 'a'
mylist.sort() 				#sorts list in-place
sorted(mylist)				#returns new list sorted
mylist.reverse()			#reverse list in-place
reversed(mylist)			#returns new reversed list


7. program to convert roman numeral into integer.
https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        special_case = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
           }

        mydict= {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        
        if isinstance(s,str):
            pass
            if len(s)>0:
                
                #check string contains only expected values - i.e. only roman letters.
                for i in s:                    
                    if not i in ('I','V','X','L','C','D','M'):
                        return
                
                #once we have checked only accepted roman values are there, now start sum.
                #see if correct representation of roman is there: largest to smallest
                
                sum_val = 0
                i=0
                while i<len(s):
                    print (i, s[i])
                    
                    #run from 1st till second last element
                    if i<len(s)-1:
                        print (s[i], s[i+1])
                        
                        #reading left to right higher value comes before lower value
                        #but in special case, lower value comes before higher value
                        
                        if mydict[s[i]]>=mydict[s[i+1]]:
                            sum_val = sum_val + mydict[s[i]]
                            i = i + 1
                            print (sum_val, i)
                        else:
                            print (s[i:i+2], "check special case")
                            #check if special case. If yes, increment i by 2
                            if s[i:i+2] in special_case:
                                sum_val = sum_val + special_case[s[i:i+2]]
                                i = i + 2
                                print (sum_val, i)
                                
                            else:
                                
                                #invalid roman numeral. exit
                                print ("invalid roman numeral. exit")
                                return
                    else:
                        sum_val = sum_val + mydict[s[i]]
                        i = i + 1
                        print (sum_val)
                        
                    
                        
                        
                print (sum_val, "outside")
                return sum_val
                    
        else:
            return
        
        

8. how to remove duplciate from a list of list.
https://stackoverflow.com/questions/12198468/python-how-to-remove-duplicate-lists-in-a-list-of-list

#1
b_set = set(map(tuple,a))  #need to convert the inner lists to tuples so they are hashable
b = map(list,b_set) #Now convert tuples back into lists (maybe unnecessary?)		

#2
b_set = set(tuple(x) for x in a)
b = [ list(x) for x in b_set ]

#3
b = list()
for sublist in a:
    if sublist not in b:
        b.append(sublist)
		
9. how to convert a list of integers to number .
def list_to_int(integers):
            # integers = [1, 2, 3]
            strings = [str(integer) for integer in integers]
            a_string = "". join(strings)
            an_integer = int(a_string)
            return an_integer

			

10. https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3014/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

Ans.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if isinstance(strs,list):
            # pass
            mydict = dict()
            
            for i in strs:
                str_val = str(sorted(list(i)))
                if str_val in mydict:
                    mydict[str_val].append(i)
                else:
                    mydict[str_val] = [i]
            
            print (mydict.values())
            return mydict.values()
            
        else:
            return

11. Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if isinstance(a,str) and isinstance(b,str):
            if a.isdigit() and b.isdigit():
			
				#function to add 2 binary digits
                def add_bin_digits(val1,val2,carry_val):
                    val = carry_val + val1 + val2
                    
                    if val==0:
                        return (0,0)
                    elif val==1:
                        return (1,0)
                    elif val==2:
                        return (0,1)
                    else:
                        return (1,1)
                    
                final_val = []
                list1 = list(map(int,a))
                list2 = list(map(int,b))
                
                i = len(list1)-1
                j = len(list2)-1
                carry = 0
                
                print ('list 1 ', list1, i)
                print ('list 2 ',list2, j )
                
                while i>=0 and j>=0:
                    print ('processing - ')
                    print ('posn = ', i,'val = ', list1[i] )
                    print ('posn = ',j,'val = ', list2[j])
                    x,y = add_bin_digits(list1[i],list2[j],carry)
                    final_val.append(x)
                    carry = y
                    print ('appending ', x)
                    print ('carry forward ',carry)
                    
                    i = i - 1
                    j = j - 1
            
            print ('i = ', i , 'j = ', j)
            if i>=0:
                print ('list1 not processed fully ')
                while i>=0:
                    print (list1[i])
                    x,y = add_bin_digits(list1[i],0,carry)
                    final_val.append(x)
                    carry = y
                    i = i - 1

            if j>=0:
                print ('list2 not processed fully ')
                while j>=0:
                    print (list2[j])
                    x,y = add_bin_digits(0,list2[j],carry)
                    final_val.append(x)
                    carry = y
                    j = j - 1
            if carry:
                final_val.append(1)
            print (final_val)
            final_val.reverse()

            str1 = ''.join(map(str,final_val))
            print (str1)
            return str1



--Other way : faster
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if isinstance(a,str) and isinstance(b,str):
            if a.isdigit() and b.isdigit():
                sum_dict = {
                    0: (0,0),
                    1: (1,0),
                    2: (0,1),
                    3: (1,1)                    
                }
                
                list_a = list(a)
                list_b = list(b)
                print (list_a, list_b)
                
                len_a = len(list_a) -1 
                len_b = len(list_b) -1 
                
                sum_value = []
                carry = 0
                
                while len_a>=0 and len_b>=0:
                    print (list_a[len_a], list_b[len_b], carry)
                    value = int(list_a[len_a]) + int(list_b[len_b]) + carry
                    print (value)
                    add,carry = sum_dict[value]
                    print (add,carry)
                    sum_value.append(add)
                    len_a -=1
                    len_b -=1
                
                if len_a>=0:
                    print ('list A not processed fully ')
                    while len_a>=0:
                        value = int(list_a[len_a])  + carry
                        add,carry = sum_dict[value]
                        sum_value.append(add)
                        len_a -=1
                        
                if len_b>=0:
                    print ('list B not processed fully ')
                    while len_b>=0:
                        value = int(list_b[len_b])  + carry
                        add,carry = sum_dict[value]
                        sum_value.append(add)
                        len_b -=1
                    

                if carry:
                    sum_value.append(1)
                    
                print (sum_value)
                sum_value.reverse()

                str1 = ''.join(map(str,sum_value))
                print (str1)
                return str1
                
                
			
12. collections.Counter() -   #useful in string - count of values.
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

13. Merge Sorted Array
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/309/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:
	-10^9 <= nums1[i], nums2[i] <= 10^9
	nums1.length == m + n
	nums2.length == n

Ans.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
		#Start inserting into end the valueof m/n into nums1.
		while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                print ('m1 =',m-1,' n1 = ',n-1)
                print (nums1)
                print (nums2)
                nums1[m+n-1]=nums1[m-1]
                m=m-1
                print (nums1)
                # print (nums2)
            else:
                print ('m2 =',m-1,' n2 = ',n-1)
                print (nums1)
                print (nums2)
                nums1[m+n-1]=nums2[n-1]
                n=n-1
                print (nums1)
                # print (nums2)
        print (m-1, n-1)  
        
        while n>0:
            nums1[m+n-1]=nums2[n-1]
            n=n-1

14. Valid Palindrome
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/288/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.


Ans.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if isinstance(s,str):
            if len(s)>0:
                s1 = ''.join(i.lower() for i in s if i.isalnum())
                print (s)
                print (s1)
                
                if s1 == s1[::-1]:
                    return True
                else:
                    return False
            else:
                return True
        

Note: 
	"" ---> length 0 string is True as default.
	s1 = ''.join(i.lower() for i in s if i.isalnum())  ---> snippet to keep only alphanumeric characters in a string.

15. compare dictionaries -

def dict_compare(d1, d2):
	d1_keys = set(d1.keys())
	d2_keys = set(d2.keys())
	shared_keys = d1_keys.intersection(d2_keys)
	added = d1_keys - d2_keys
	removed = d2_keys - d1_keys
	modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
	same = set(o for o in shared_keys if d1[o] == d2[o])
	return added, removed, modified, same
			
or,
shared_items = {k: s1[k] for k in s1 if k in t1 and s1[k] == t1[k]}
print (shared_items)	

		
16. One Edit Distance

Solution
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.

Ans.
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # if isinstance(s,str) and isinstance(t,str):
        def insert_check(str1,str2):
            if len(str2)-len(str1) == 1:
                print ('running insert_check ', str1, str2)
                
                list1 = list(str1)
                list2 = list(str2)
                
                flag = False
                i=j=0
                posn = 0
                while i<len(list1) and j<len(list2) and not flag:
                    if list1[i] == list2[j]:
                        posn = posn + 1
                        i = i + 1
                        j = j + 1
                    else:
                        flag = True
                        break
                
                if flag or i==len(list1):
                    print ('check insert')
                    print ('before ', list1)
                    list1.insert(posn,list2[posn])
                    print ('after ',list1)
                    
                
                print (list1)
                print (list2)
                
                if list1 == list2:
                    return True
                else:
                    return False
        
        def delete_check(str1,str2):
             if len(str1)-len(str2) == 1:
                print ('running delete_check ', str1, str2)
                
                list1 = list(str1)
                list2 = list(str2)
                
                flag = False
                i=j=0
                posn = 0
                while i<len(list1) and j<len(list2) and not flag:
                    if list1[i] == list2[j]:
                        posn = posn + 1
                        i = i + 1
                        j = j + 1
                    else:
                        flag = True
                        break
                
                if flag or j==len(list2):
                    print ('check delete')
                    print ('before ', list1)
                    list1.pop(posn)
                    print ('after ',list1)
                    
                
                print (list1)
                print (list2)
                
                if list1 == list2:
                    return True
                else:
                    return False
                
        def replace_check(str1,str2):
             if len(str1)-len(str2) == 0:
                print ('running replace_check ', str1, str2)
                
                list1 = list(str1)
                list2 = list(str2)
                
                flag = False
                i=j=0
                posn = 0
                while i<len(list1) and j<len(list2) and not flag:
                    if list1[i] == list2[j]:
                        posn = posn + 1
                        i = i + 1
                        j = j + 1
                    else:
                        flag = True
                        break
                print ('flag is ',flag)
                if flag:
                    print ('check replace')
                    print ('before ', list1)
                    list1[posn]=list2[posn]
                    print ('after ',list1)
                
                
                    print (list1)
                    print (list2)

                    if list1 == list2:
                        return True
                    else:
                        return False        
                else:
                    return False        

  
                    
        # print ('insert_check(s,t) ', insert_check(s,t))    
        
        if insert_check(s,t) or delete_check(s,t) or replace_check(s,t):
            return True
        else:
            return False
            
            		
17. Product of Array Except Self

Solution
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Ans.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if isinstance(nums,list):
            if len(nums)>0:
                
                left = [1]*len(nums)
                right = [1]*len(nums)
                answer = [1]*len(nums)
                
                i=0
                #calculate left array
                while i<len(left):
                    if i==0:
                        left[i]=1
                        i = i + 1
                    else:
                        left[i] = left[i-1]*nums[i-1]
                        i = i + 1
                
                print ('left list ',left)
                
                j=len(right)-1
                while j>=0 :
                    if j==len(right)-1:
                        right[j]=1
                        j = j - 1
                    else:
                        right[j] = right[j+1]*nums[j+1]
                        j = j - 1
                
                print ('right list ',right)
                
                k=0
                while k<len(nums):
                    answer[k] = left[k] * right[k]
                    k=k+1
                print (answer)
                return answer

18. Move Zeroes : https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/262/

Solution
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Ans.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if isinstance(nums,list):
            if len(nums)>0:
                
                zero_tracker = 0
                non_zero_tracker =0
                i = 0
                length_list = len(nums)
                
                '''
                approach:
                2 pointers -
					zero
						- if hit zero, wait and move step by step
						- if hit non-zero, skip until end or zero
					non-zero
						- if hit non-zero, wait and move step by step
						- if hit zero, skip until end or zero
					
					when swap, move the zero and non-zero by 1.
                
                '''
                
                while i < length_list:
                    if nums[i] == 0:
                        zero_tracker = i 
                        
                        if zero_tracker>=non_zero_tracker:
                            non_zero_tracker = zero_tracker + 1

                        while   non_zero_tracker<length_list and nums[non_zero_tracker]==0:
                            non_zero_tracker = non_zero_tracker + 1
                            
                        if non_zero_tracker<length_list and zero_tracker<length_list:   
                            nums[zero_tracker],nums[non_zero_tracker] = nums[non_zero_tracker],nums[zero_tracker]
                            
                        else:
                            break
                        
                        i =  i + 1
                    else:
                        non_zero_tracker=i
                        i =  i + 1
				
19. 
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3017/
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

Soln.
approach start from begin and if num of distinct char equals k, then before adding next char, remove char at start of window.


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if isinstance(s,str) and isinstance(k,int):
            if len(s)>0 and k>0:
                print ('checking ',s, ' for max distinct ',k,' characters')
                          
                #edge case 2
                if len(set(s))<=k:
                    return len(s)
                
                mydict = dict()
                start_posn = 0
                end_posn = 0
                i=0
                
                len_max_str = 0
                max_str = ""
                
                while i<len(s):
                    end_posn = end_posn + 1
                    
                    if s[i] in mydict:
                        mydict[s[i]]=i
                    else:
                        if len(mydict.keys()) == k:
                            print ('len(mydict.keys()) == k', len(mydict.keys()) , k)
                            # remove earliest value by updating start posn 
                            a = min(mydict.values())
                            print ('a ',a)
                            
                            for x in mydict:
                                if mydict[x] == a:
                                    index_to_remove = x
                                    break
                            print ('index_to_remove ',index_to_remove)
                            start_posn = mydict[index_to_remove] + 1
                            
                            del mydict[index_to_remove]
                            mydict[s[i]]=i
                        else:
                            mydict[s[i]]=i
                            
                    
                    #update min_string
                    if end_posn - start_posn + 1 > len_max_str:
                        len_max_str = end_posn - start_posn
                        max_str = s[start_posn:end_posn+1]
                    
                    i = i + 1
                
                print  (max_str)
                return len_max_str
                    
            else:
                #edge case 1
                return 0

other approache (shorter code)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if isinstance(s,str) and isinstance(k,int):
            '''
            create a sliding window, and if max char >k then drop first element.
            
            edge cases - len of string < k.
            
            '''
            
            
            #edge cases - len of string < k.
            if len(s)<k:
                return len(s)
            
            start=0
            end=start+1
            i=0
            curr_max = 0
            mydict = {}
            
            while i < len(s):
                #check if len>k update curr max                
                #check if num of dist elements >k remove 1st element.

                end = i
                mydict[s[i]] = i
                
                
                if len(mydict)>k:
                    min_val = min(mydict.values())
                    removal_key = -1
                    for x in mydict:
                        if mydict[x] == min_val:
                            removal_key=x
                    # print ('removal_key ',removal_key)
                    start = mydict[removal_key] + 1
                    
                    del mydict[removal_key]
                
                if len(s[start:end+1])>curr_max:
                    # print ('accepted ',s[start:end+1])
                    curr_max = len(s[start:end+1])
                    
                # print (s[i], mydict, len(s[start:end+1]))
                i = i + 1
            
            # print (s[start:end+1], curr_max)
            return curr_max
            
        else:
            return 0
			
			
20.	https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3018/
Validate IP Address

Solution
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

 

Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 

Constraints:

IP consists only of English letters, digits and the characters "." and ":".


Solution.
class Solution:
    def validIPAddress(self, IP: str) -> str:
        '''
        Approach - read-in the string.
        split on basis of dot separator - if pass then check if ipv4
        split on basis of colon separator - if pass then check ipv6
        else return neither
        '''
        
        if isinstance(IP,str):
            if len(IP)>0:
                
                #check IPv4
                #tests - array has only 4 length, all digit, non start with 0.
                
                my_array = IP.split('.')                
                if len(my_array)==4:
                    for i in my_array:
                        print (i)
                        if len(i)==0:
                            return 'Neither'
                        else:
                            if not i.isdigit():
                                return 'Neither'
                            else:
                                if not (0<= int(i) <256):
                                    return 'Neither'
                                else:
                                    print ('ok', len(i)>1, i[0]=='0')
                                    if len(i)>1 and i[0]=='0':
                                        print ('bad length')
                                        return 'Neither'
                    return 'IPv4'

                def check_hexadecimal(s):
                    acceptable_chars = '0123456789ABCDEFabcdef'
                    for char in s:
                        if char not in acceptable_chars:
                            return False
                    return True
                
                #check IPv6
                my_array = IP.split(':')
                print ('my_array ',my_array)
                
                if len(my_array)==8:
                    
                    for i in my_array:
                        print (i)
                        if not 0<len(i)<=4:
                            return 'Neither'
                        else:
                            if not check_hexadecimal(i):
                                return 'Neither'

                    return 'IPv6' 
                        
                else:
                    return 'Neither'
                
                    
                
            else:
                return 'Neither'
        
21. https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3019/
Subarray Sum Equals K

Solution
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Ans.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if isinstance(nums, list) and isinstance(k,int):
            
            #declare variables
            count = 0 		#denotes number of occurences. set to 0
            cum_sum = 0  	#denotes cumulative sum of values from 1st value onwards. set to 0.
            sum_dict={0:1}  #a dictionary of sums captured along with occurences. 
            
            for i in nums:
                print ('processing ',i)
                
                cum_sum = cum_sum + i
                
                sum_to_search = cum_sum - k
                
                #check if this sum is present in sum_dict
                if sum_to_search in sum_dict:
                    count =  count + sum_dict[sum_to_search]
                
                if cum_sum in sum_dict:
                    sum_dict[cum_sum]+=1
                else:
                    sum_dict[cum_sum]=1
            
            print (count)
            return count


2020-8-12 [added new]
22. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/

Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Constraints:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.			

Ans.
Approach: 
create 2 varaibles - cum_sum and mod_list.
find for each posn -
	* cumulative sum
	* mod of cum sum with k

if mod of cum_sum%k is already in a mod_list, return True.
Else, if we scan whole list and still no entry of cum_sum%K then return False.


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if k>0:
            mod_list=[]
            cum_sum= 0
            for i in nums:
                print ('processing ',i)
                cum_sum = cum_sum + i
                
                mod_val = cum_sum%k
                
                if mod_val in mod_list:
                    return True
                else:
                    mod_list.append(mod_val)
            return False
                
        
        else:
            return False
			

2020-08-19

23. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Ans.
Approach: when it comes to palindrome, do 2 things for each posn -
* assume len of palindrome as ODD - scan left and right from posn and check if palindrome
* assume len of palindrome as EVEN - scan left=posn and right = posn+1 and check if palindrome

edge cases -
if len of string = 0 --empty
if len of string = 1 -- just one element.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if isinstance(s,str) and len(s)>0:
            
            def check_palindrome(s,start_left, start_right):
                # print ('check_palindrome ',s, start_left, start_right)
                # len_ = start_right - start_left +1
                while start_left>=0 and start_right<len(s) and s[start_left]==s[start_right]:
                    start_left -=1
                    start_right +=1
                
                flag = False
                if s[start_right-1] == s[start_left+1]:
                    flag=True
                
                # print ('check_palindrome now ',s[start_left:start_right+1])
                return flag,start_left+1,start_right
            
            if len(s) == 1:
                return s
            
            x = 0
            max_len = -1
            max_coord = (0,0)

            while x<len(s)-1:
                
                flag_odd,left_odd,right_odd = check_palindrome(s,x,x)
                max_odd = right_odd - left_odd
                # max_odd_coord = (left_odd,right_odd)
                
                flag_even,left_even,right_even = check_palindrome(s,x,x+1)
                max_even = right_even - left_even
                # max_even_coord = (left_even,right_even)
                
                if max_odd> max_len and max_odd>max_even and flag_odd:
                    max_len = max_odd
                    max_coord = (left_odd,right_odd)
                elif max_even>max_len and max_even>max_odd and flag_even:
                    max_len = max_even
                    max_coord = (left_even,right_even)
                x=x+1
            
            # print (s[max_coord[0]:max_coord[1]] ,max_len)
            return s[max_coord[0]:max_coord[1]]         
                
            
            
            
        else:
            return ""
    
        
24. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Ans.

Idea -
The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration

Variables i and j define the container under consideration. 
We initialize them to first and last line, meaning the widest container. 
Variable water will keep track of the highest amount of water we managed so far. 
We compute j - i, the width of the current container, and min(height[i], height[j]), the water level that this container can support. 
Multiply them to get how much water this container can hold, and update water accordingly. 
Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof". 
Continue until there is nothing left to consider, then return the result.


class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water        


25. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 
 
 Ans.
 class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if isinstance(nums, list) and isinstance(target,int):
            
            nums.sort()
            result = nums[0] + nums[1] + nums[2]
            
            #set 2 pointers, one at start and other at end of array.
            
            for i,val in enumerate(nums):
                j = i + 1
                k = len(nums) -1
                
                while j < k:
                    sum_val = nums[i] + nums[j] + nums[k]
                    
                    if sum_val == target:
                        result = sum_val
                        return result
                    
                    if abs(target-sum_val) < abs(target - result):
                        result = sum_val
                    
                    if sum_val<target:
                        j = j + 1
                    else:
                        k = k -1
            
            return result
        
        else:
            return 
			
			
26. 4Sum
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

Ans.

This problem is a follow-up of 3Sum, so take a look at that problem first if you haven't. 4Sum and 3Sum are very similar; 
the difference is that we are looking for unique quadruplets instead of triplets.

As you see, 3Sum just wraps Two Sum in an outer loop. As it iterates through each value v, it finds all pairs whose sum is equal to target - v using one of these approaches:

Two Sum uses a hash set to check for a matching value.
Two Sum II uses the two pointers pattern in a sorted array.
Following a similar logic, we can implement 4Sum by wrapping 3Sum in another loop. But wait - there is a catch. 
If an interviewer asks you to solve 4Sum, they can follow-up with 5Sum, 6Sum, and so on. 
What they are really expecting at this point is a kSum solution. Therefore, we will focus on a generalized implementation here.


Approach-
The two pointers pattern requires the array to be sorted, so we do that first. 
Also, it's easier to deal with duplicates if the array is sorted: repeated values are next to each other and easy to skip.

For 3Sum, we enumerate each value in a single loop, and use the two pointers pattern for the rest of the array. 
For kSum, we will have k - 2 nested loops to enumerate all combinations of k - 2 values.

Algorithm

We can implement k - 2 loops using a recursion. We will pass the starting point and k as the parameters. When k == 2, we will call twoSum, terminating the recursion.

For the main function:
	Sort the input array nums.
	Call kSum with start = 0, k = 4, and target, and return the result.

For kSum function:
	Check if the sum of k smallest values is greater than target, or the sum of k largest values is smaller than target. 
	Since the array is sorted, the smallest value is nums[start], and largest - the last element in nums.
		If so, no need to continue - there are no k elements that sum to target.
	If k equals 2, call twoSum and return the result.
	Iterate i through the array from start:
		If the current value is the same as the one before, skip it.
		Recursively call kSum with start = i + 1, k = k - 1, and target - nums[i].
		For each returned set of values:
			Include the current value nums[i] into set.
			Add set to the result res.
			Return the result res.

For twoSum function:
	Set the low pointer lo to start, and high pointer hi to the last index.
	While low pointer is smaller than high:
		If the sum of nums[lo] and nums[hi] is less than target, increment lo.
			Also increment lo if the value is the same as for lo - 1.
		If the sum is greater than target, decrement hi.
			Also decrement hi if the value is the same as for hi + 1.
		Otherwise, we found a pair:
			Add it to the result res.
			Decrement hi and increment lo.
Return the result res.

soln -
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def twosum(nums, target):
            left = 0
            right = len(nums)-1
            result = []
            
            while left<right:
                sum_val = nums[left] + nums[right]
                if sum_val < target:
                    left += 1
                elif sum_val>target:
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left +=  1
                    right -= 1
            return result
        
        def kSum(nums, target, k):
            #k = number of elements in sublist for forming sum
            
            result = []
            
            if len(nums)==0:
                return result
            
            if k==2:
                #call twosum
                return twosum(nums, target)
            
            for i, val in enumerate(nums):
                if i==0 or nums[i]!=nums[i-1]:
                    for j,val in enumerate( kSum(nums[i+1:], target - nums[i],k-1) ):
                        result.append([nums[i]]+ val)
            
            return result
        
        nums.sort()    
        
        output_list = []
        for i in kSum(nums, target, 4):
            if i not in output_list:
                output_list.append(i)
        
        return output_list


        
        

27. Sort Colors
https://leetcode.com/problems/sort-colors/solution/

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Ans.
3 cases:
if nums[i] == 0; swap with pointer_zero and increment pointer_zero; 
we increment 'i' here as we have swapped now, and want to move pointer to next value post swap.

if nums[i] == 2; swap with pointer_two and decrement pointer_two
we dont increment i here as after swap we want to process current node again.

if nums[i] == 1; i++;


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if isinstance(nums,list):
            
            pointer_zero =0
            pointer_two = len(nums) -1
            
            i=0
            
            while i<=pointer_two:
                '''
                3 cases:
                if nums[i] == 0; swap with pointer_zero and increment pointer_zero; 
				we increment 'i' here as we have swapped now, and want to move pointer to next value post swap.
                
                if nums[i] == 2; swap with pointer_two and increment pointer_two
                we dont increment i here as after swap we want to process current node again.
                
                if nums[i] == 1; i++;
                '''
                print (nums[i])
                print ('before ', nums)         
                if nums[i] == 0:
                    nums[i],nums[pointer_zero] = nums[pointer_zero],nums[i]
                    i += 1
                    pointer_zero += 1
                elif nums[i] == 2:                    
                    nums[i],nums[pointer_two] = nums[pointer_two], nums[i]                    
                    pointer_two -= 1
                else:
                    i +=1
                print ('after ', nums)                         
            
        else:
            return

28. Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]

Ans.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output

My soln-
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def kComb(first,arr):
            if len(arr) == k:
                result.append(arr[:])
            
            for i in range(first, n+1):
                arr.append(i)
                kComb(i+1, arr)
                arr.pop()
        
        kComb(1,[])
        return result

29. Subsets
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Ans.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrace(first, curr,k):
            if len(curr) == k:
                result.append(curr[:])
            
            for i in range(first, n):
                curr.append(nums[i])
                backtrace(i+1, curr,k)
                curr.pop()
        
        n = len(nums)
        for x in range(n+1):
            backtrace(0,[],x)
        return result

30. Minimum Time Visiting All Points
https://leetcode.com/problems/minimum-time-visiting-all-points/

On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.

Example 1:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Example 2:
Input: points = [[3,2],[-2,2]]
Output: 5

Ans.
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if isinstance(points, list):
            x1,y1 = points[0]
            i = 0
            cost=0

            while i<len(points) :
                x2,y2=points[i]
                dx = abs(x2-x1)
                dy = abs(y2-y1)
                flag=True

                while flag:
                    if dx>0 and dy>0:
                        dx-=1
                        dy-=1
                        cost+=1
                    
                    elif dx==0 and dy>0:
                        dy-=1
                        cost+=1
                    elif dy==0 and dx>0:
                        dx-=1
                        cost+=1
                    else:
                        flag=False
                i+=1
                x1,y1 = x2, y2
                
            return cost
            
        else:
            return	

31.  Pow(x, n) -
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104		

Ans.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n<(pow(-2,31)-1) or n>pow(2,31):
            return
        
        if x>100.0 or x<-100.0:
            return
        
        if x==0:
            return float(inf)
        
        if n==0:
            return 1.0
        
        if n<0:
            x = 1/x
            n = -n
        
        def recur_(val, power):
            print (val, power)
            if power <2:
                print ('power <2')
                return 1.0*val
            
            if int(power%2) ==0:
                print ('power%2 ==0')
                return recur_(val*val, power/2)
            else:
                print ('NOT power%2 ==0')
                return val*recur_(val*val, power/2)
        
        return recur_(x,n)
        
            
32. Permutations
https://leetcode.com/problems/permutations/      

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Ans.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if isinstance(nums, list):
            if len(nums)==0:
                return []
            
            if len(nums)==1:
                return [nums]
            
            result = []
            
            def backtrace(num, arr):
                print (num, arr)
                if len(num)==0:
                    result.append(arr[:])
                
                for i,val in enumerate(num):
                    arr1 = arr.copy()
                    x = num.pop(i)
                    arr1.append(x)
                    backtrace(num, arr1)
                    num.insert(i, x)
            
            backtrace(nums, [])
            print (result)
            return result


33. Permutations II-
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

Ans.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if isinstance(nums, list):
            print ('nums ',nums)
            if len(nums)==0:
                return
            
            if len(nums)==1:
                return [nums]
            
            result = []
            
            def backtrace(num, arr):
                # print (num, arr)
                if len(num)==0:
                    if arr[:] not in result:  #only this line added --otherwise same as #32
                        result.append(arr[:])
                
                for i,val in enumerate(num):
                    
                    arr1 = arr.copy()
                    x = num.pop(i)
                    arr1.append(x)
                    backtrace(num, arr1)
                    num.insert(i, x)
                    
            
            
            backtrace(nums, [])
            print (result)
            return result

# Other approach
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if isinstance(nums, list):
            print ('nums ',nums)
            if len(nums)==0:
                return
            
            if len(nums)==1:
                return [nums]
            
            result = []
            
            def backtrace(num, arr):
                if len(num)==0:
                    if arr not in result:
                        result.append(arr[:])
                
                for i, val in enumerate(num):
                    val = num.pop(i)
                    arr.append(val)
                    backtrace(num,arr)
                    arr.pop()
                    num.insert(i,val)
            
            backtrace(nums,[])
            return result
                	       
	       
34. Combination Sum 
https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500

Ans.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if isinstance(candidates, list) and isinstance(target, int):
            
            if target <=0:
                return []
            
            if min(candidates)>target:
                return []
            
            result = []
            
            def backtrace(num, arr, target_):
                if sum(arr)==target_:
                    val_ = sorted(arr[:])
                    if  val_ not in result:
                        result.append(val_)
                
                if sum(arr)>target_:
                    return []
                
                if sum(arr)< target_ or len(arr)==0:
                    for i, val in enumerate(num):
                        x = num[i]
                        arr1 = arr.copy()
                        arr1.append(x)
                        backtrace(num, arr1, target_)
                        
               
            backtrace(candidates, [], target)
            print (result)
            return result
            
            
        else:
            return []
			
35. Combination Sum II     
https://leetcode.com/problems/combination-sum-ii/       

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

Ans.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if isinstance(candidates, list) and isinstance(target, int):
            
            if len(candidates)==0:
                return []
            
            if target<=0:
                return []
            result = []
            
            
            def backtrace(num, arr, target):
                
                if sum(arr)==target:
                    if arr[:] not in result:
                        result.append(arr[:])
                
                if sum(arr)>target:
                    return
                
                if sum(arr)<target:
                    for i, val in enumerate(num):
                        x = num.pop(i)
                        arr1 = arr.copy()
                        arr1.append(x)
                        arr1.sort()
                        backtrace(num, arr1, target)
                        num.insert(i, x)
                    
                    
                
            
            backtrace(candidates,[], target)
            print (result)
            return result

