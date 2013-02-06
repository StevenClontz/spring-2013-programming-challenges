def medianish(list_of_ints):
  list_of_ints.sort()
  middle = len(list_of_ints) / 2
  return list_of_ints[middle]


import sys
readlines = sys.stdin.readlines() # reads input to list of strings for each line

inputString = ""
for item in readlines:
  inputString += item

inputListStrs = inputString.split()
inputList = [int(item) for item in inputListStrs]
inputList.pop(0) # don't need 0th item

while inputList != []:
  num_of_ints = inputList.pop(0)
  list_of_ints = inputList[0:num_of_ints]
  house = medianish(list_of_ints)
  print sum([abs(item - house) for item in list_of_ints])


  inputList = inputList[num_of_ints:]