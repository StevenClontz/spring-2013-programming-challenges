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
  print line 