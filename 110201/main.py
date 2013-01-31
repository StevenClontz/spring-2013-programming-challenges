def read_input():
  '''
  Reads raw input and returns list of strings holding each line
  '''
  input_list = []
  while 1:
    try:
      input_list.append(raw_input())
    except EOFError:
      break
  return input_list

for line in read_input():
  # split string "4 1 4 2 3" into space delimited list of signed integers
  string_list = line.split()
  number_list = []
  for number_string in string_list[1:]:
    number_list.append(int(number_string))
  # get list of False entries for length of list
  check_list = [False]*(len(number_list))
  # don't need jump of length 0
  check_list[0] = True
  # go through pairs and set appropriate entry of check_list to True if we found that jump
  for n in range(len(number_list)-1):
    # find difference in pairs
    check = abs(number_list[n]-number_list[n+1])
    if 0 < check < len(number_list):
      check_list[check] = True
  if len(set(check_list)) == 1 and check_list[1]:
    print "Jolly"
  else:
    print "Not Jolly"