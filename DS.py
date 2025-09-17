#Problem 1
def hello_world():
    print("Hello world!")
hello_world()

#problem 2
def todays_mood():
    mood="happy"
    print("today's mood:" + mood)
todays_mood()

# problem 3
def print_menu(menu):
    print("lunch today is: "+ menu)
food="pizza"
print_menu(food)

# problem 4
def sum (a,b):
    return a+b
a= 13
b=27
double= sum(a,b)*2
print(double)
# problem 5
def product(a,b):
    return a*b
a=27
b=30
print(product(a,b))

# problem 6
def classify_age(age):
    if age < 18:
        print("child")
    else:
        print("adult")
age = int(input("whta is your age: "))
classify_age(age)

#problem 7
def what_time_is_it(hour):
    if hour==2:
        return "taco time"
    elif hour== 12:
        return "peanut butter jelly time"
    else:
        return "nap time"
hour= int(input('what time is it now: ?'))
print(what_time_is_it(hour))

# problem 8
def blackjack(score):
    if score==21:
        print("blackjack")
    elif score > 21:
        print("Bust")
    elif 17<= score< 17:
        print("Nice hand")
    else:
        print("Hit me!")
score= int(input( " what is your total"))
blackjack(score)

#problem 9
def get_first (lst):
    if len(lst)==0:
        return "None"
    else:
        return lst[0]
user_input= input('what is the list?')
lst =(list(map(int,user_input.split())))
print(get_first(lst))

#problem 10
def get_last(lst):
    if len(lst)==0:
        return None
    else:
         return lst[-1]
user_input= input('what nummbers do you have for use today')
lst= list(map(int,user_input.split()))
print(get_last(lst))

#problem 11
def counter(stop):
    for i in range(1,stop +1):
        print(i)
counter(5)

#problem 12
def sum_ten():
    total=0
    for i in range(1,11):
        total+=i
    return total
print(sum_ten())

#problem 13
def sum_positive (stop):
    total = 0
    for i in range(1,stop +1):
        total+=i
    return total
sum= int(input('what is yor favourate number'))
print(sum_positive(sum))

#problem 14
def sum_range(start,stop):
    total = 0
    for i in range(start,stop +1):
        total+= i
    return total
start= 3
stop = 9
print(sum_range(start,stop))

#problem 15
def print_negatives(lst):
    positive = []
    for nums in lst:
        if nums<0:
            print(nums)
        if nums > 0 :
            positive.append(nums)
    if positive == lst:
        print(None)   
numbers= []
print_negatives(numbers)

#problem 16
def greet_user (name):
    print("hello "+ name.capitalize())
name=input('what is the name please ')
greet_user(name)

#problem 17
def difference (a,b):
    return b-a
b=30
a=2
print(difference(a,b))

# problem 18
def concatenate_list(nums):
    return nums + nums
nums= [3,5,6,7,8] 
print(concatenate_list(nums))

# problem 19
def sleep_assessment(hours):
    if hours < 8 :
        print("Oof, go back to bed!")
    elif 8 <= hours <= 10:
        print('You got a good night\'s rest!')
    else:
        print('You are sleep prodigy')
sleep_assessment(6)

# problem 20
def calculate_tip(bill,service_quality):
    if service_quality == "poor":
        return int((10/100) *bill)
    elif service_quality == "average":
        return int((15/100) * bill)  
    elif service_quality == "excelent":
       return int((20/100)*bill)
    else:
        None
tip1 = calculate_tip(44.53,"average")
print(tip1)
print(calculate_tip (200,"poor"))  

#problem 21
def rock_paper_scissors(player1,player2):
    if player1==player2:
        print('it is a tie ')
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
rock_paper_scissors("rock","scissors")
rock_paper_scissors("paper","scissors")

#problem 22
def halve_lst(lst):
    result = []
    for number in lst:
        halved = number/2
        result.append(halved)
    return result
print(halve_lst([2,4,6,8]))

#problem 23
def above_threshold(lst,threshold):
    count = []
    for i in lst :
        if i > threshold:
            count.append(i)
    return count
lst=[8,2,13,11,4,10,14,15,3,17,1,1,7,8,7,9]
new_lst=above_threshold(lst,8)
print(new_lst)

#problem 24
def countdown(m,n):
    for nums in range(m,n-1,-1):
        print(nums)
print(countdown(10,1))

#problem 25
def power(base,exponent):
    result= base**exponent
    return result
print(power(2,5))
print(power(3,3))

#problem 26
def list_length(lst):
    count = 0
    for i in lst:
        count+=1
    return count
lst=[3,6,7,8,9,0,3,5,6,5]
print(list_length(lst))

#problem 27
def factorial(n):
    count= 1
    for nums in range(n,0,-1):
        count*= nums
    return count 
print(factorial(3))
print(factorial(6))

#problem 28
def squares(nums):
    result= []
    for num in nums:
        power = num**2
        result.append(power)
    return result
nums= [3,5,6,7,8,9,0]
print(squares(nums)) 

#problem  29
def multiply_list(lst,multiplier):
    result=[]
    for num in lst:
        multiply  = num*multiplier
        result.append(multiply)
    return result
lst= [ 1,3,2]
new_lst = multiply_list(lst , 3)
print(new_lst)

#problem 30
def count_evens(lst):
    evens = []
    for num in lst:
        if num %2 ==0:
            evens.append(num)
    return evens
lst=[2,5,6,7,8,9]
count1 = count_evens(lst)
print(count1)

#problem 31
def print_list(lst):
    for nums in lst:
        print(nums)
lst=[1,3,2,4,5,6,7,8,9]
print_list(lst)

#problem 32
def doubled(lst):
    for num in lst:
        double= num*2
        print(double)
lst=[1,3,2,4,5,6,7,8,7]
doubled(lst)

#prioblem 33
#we  are now modifying the doubled function so that it can print the list as a whole 
def doubled(lst):
    result= []
    for num in lst:
        double= num*2
        result.append(double)
    return result
lst=[1,3,2,4,5,6,7,8,7]
new_lst = doubled(lst)
print(new_lst)

#Problem 34
def flip_sign(lst):
    result= []
    for i in lst:
        flip = i*-1
        result.append(flip)
    return result
lst = [1,2,3,4,5,6,7]
flipped_sign = flip_sign(lst)
print(flipped_sign)

# Problem 35
def max_diffference(lst):
    high= max(lst)
    lower=min(lst)
    max_diff = high-lower
    return max_diff
lst=[1,3,2,4,5,6,6,9,56,10]
max_diff = max_diffference(lst)
print(max_diff)

#problem 36
def count_less_than(numbers,threshold):
    count=0
    for num in numbers:
        if num < threshold:
            count += 1 
    return count
numbers= [12,8,2,4,4,10]
counter =  count_less_than(numbers,5)
print(counter)

#problem 37
def get_evens(lst):
    result = []
    for i in lst:
        if i % 2==0:
            result.append(i)
    return result
lst = [1,2,3,4]
evens_lst=get_evens(lst)
print(evens_lst)

#problem 38
def multiples_of_five():
    for i in range(5,101,5):
        print(i)
multiples_of_five()

# problem 39
def find_divisors(n):
    result = []
    for i in range(1,n+1):
        if n % i ==0:
            result.append(i)
    return result
lst = find_divisors(6) 
print(lst)

# problem  40
def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3==0:
            print("fizz")
        elif i % 5==0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(13)

# problem 41
def print_indices(lst):
    for i in range(len(lst)):
        print(i)
lst= [5,1,3,8,2]
print_indices(lst)

#problem 42
def linear_search(lst,target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i 
    else:
        return  -1
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)

#problem 43
def convertTemp(celsius):
    ans= []
    kelvin = celsius + 273.15
    ans.append(kelvin)
    fahrenheit= celsius* 1.80 + 32.00
    ans.append(fahrenheit)
    return ans 
temperatures = convertTemp(23.00)
print(temperatures)

#problem 44
def average (scores):
    count = 0
    total_elements = len(scores)
    for i in scores:
        count+=i
    return count/ total_elements
scores = [84,73,92,95,88]
avg_score =  average(scores)
print(avg_score)

#problem 45
def increment_values(lst):
    values = []
    for i in lst:
        increment = i+1
        values.append(increment)
    return values 
lst = [ 3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)

#problem 46
def check_num(lst,num):
    for i in lst:
        if i==num:
            return True
    return False
lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
print(flag1)
flag2 = check_num(lst,7)
print(flag2)

#problem 47
def find_missing(nums):
    for i in range(0,6):
        if i not in nums:
         print(i)
    
nums = [2,5,1,3]
missing= find_missing(nums)
print(missing)

#problem 48
def reverse_list (lst):
    lst.sort(reverse=True)
    return lst
lst = [1,2,3,4,5,6]
rev= reverse_list(lst)
print(rev)

#problem 49
def get_odds(nums):
    odd = []
    for i in nums:
        if i%2 != 0:
         odd.append(i)
    return odd
nums= [2,5,1,8,6,7]
odd_nums = get_odds(nums)
print(odd_nums)

# problem 50
def multiplication_table(num):
   for i  in range(1,11):
       nums = num*i
       print(nums)
multiplication_table(7)
      
# problem 51
def list_to_number(digits):
   stri_nums=""
   for c in digits:
        stri_nums+=str(c)   
   return int(stri_nums)
digits = [1,0,4]
number = list_to_number(digits)
print(number)

#`problem 52
def move_zeroes(nums):
   zeroes = []
   zero_count=0
   for c in nums:
      if c!=0:
         zeroes.append(c)
      else:
        zero_count+=1
   zeroes.extend([0]*zero_count)
   return zeroes
nums = [1,0,2,3,0,0,4]
new_nums= move_zeroes(nums)
print(new_nums)
      
#problem 53
def print_odd_indices(nums):
   for c in range(len(nums)):
      if c%2!=0:
        print (nums[c])
nums = [3,4,8,1,5,2]
print_odd_indices(nums)
   
#problem 54
def find_all_occurrences(lst,target):
    indices= []
    for i in range(len(lst)):
        if lst[i]==target:
            indices.append(i)
    return indices
lst =[1,2,6,5,2,1,3,2,2]
index_list= find_all_occurrences(lst,2)
print(index_list)

# Dictionaries in Python
faith = dict()
faith["mupotsa"]="pana"
print(faith )
#Problem 1
def is_sebsequence(lst,sequence):
    seq_index = 0
    for i in lst:
        if seq_index==len(sequence):
            break
        if i ==sequence[seq_index]:
            seq_index+=1
    return seq_index == len(sequence)  # True if all of sequence was matche
lst=[5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]
print(is_sebsequence(lst,sequence))
 

 # python list 
x= [ 1,2,3,4,5,6]
y=[2,5,8,9]
print ( x+ y ) # this is what we call concatenation
d= 2*y# this is called repetition 
print (d)
print(len(x)) # called length  of the list 
print ( (x[4])) # this print the object that is on the 4th position of  the list and we always start  counting on 0 always 
print (x[3:5]) # we always take the 3 rd number and we always disgurd the last number , like we dont include the number that is on the 5th place  .
print (3 in x ) # check if the element is in the list 
z = y.append (4)
print(z)



            





        









