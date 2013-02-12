'''
1_6_2 | "Minesweeper"
Authors:
  Steven
'''

# list to collect maps
ms_maps = []

# read input
line = raw_input()
try:
  while line != "0 0":
    # first line is "%d %d" for row_num, col_num
    row_num = int(line.split()[0])
    
    ms_map = []
    # next row_num lines are rows of map
    for i in range(0,row_num):
      ms_map.append(list(raw_input()))
    ms_maps.append(ms_map)

    # grab next map
    line = raw_input()
except EOFError:
  pass

# for each map, solve it!
for counter, ms_map in enumerate(ms_maps):
  # create solution list of lists of integers
  solve_map = [[0]*len(ms_map[0]) for i in range(len(ms_map))]
  # find mines in ms_map
  for row_num in range(0,len(ms_map)):
    for col_num in range(0,len(ms_map[row_num])):
      # if it's a mine, increment neighbors by 1
      if ms_map[row_num][col_num] == "*":
        for row in range(row_num-1, row_num+2):
          if row >= 0 and row < len(ms_map):
            for col in range(col_num-1, col_num+2):
              if col >= 0 and col < len(ms_map[0]):
                solve_map[row][col] += 1
  # time to print the results!
  print "Field #%d:" % (counter+1)
  field_out = ""
  for row_num in range(0,len(ms_map)):
    for col_num in range(0,len(ms_map[row_num])):
      if ms_map[row_num][col_num] == "*":
        field_out += "*"
      else:
        field_out += str(solve_map[row_num][col_num])
    field_out += "\n"
  print field_out

# TODO: output has extra trailing line...