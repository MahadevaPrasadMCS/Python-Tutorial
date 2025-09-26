nums = [4, 5, 1, 2, 0, 4]

def find_index_of_first_non_repeated(nums):
  
    #created a dictionary to store frequencies of numbers in the List
    freq = {}

    #List should not be empty
    if not nums:
        return -1

    #Loop to check the frequencies of number
    for num in nums:
        repeated[num] = repeated.get(num,0) + 1

  #Loop to check the index of first number which is not repeated
    for i,num in enumerate(nums):
        if repeated[num] == 1:
            return i
            
print(find_index_of_first_non_repeated(nums))
