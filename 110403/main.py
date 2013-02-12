 # read input to list of strings for each line
import sys
readlines = sys.stdin.readlines()

# want to break input into chunks delimited by '\n'
import itertools
keyfunc = lambda x: x == '\n'
raw_groups = [list(group) for is_key, group in itertools.groupby(readlines, keyfunc) if not is_key]

# first entry is always redundant: len(groups) - 1
raw_groups = raw_groups[1:]

# clean the rest of it up - 1st in each group is redundant, make entries integers, want sorted
groups = [sorted([int(speed) for speed in raw_group[1:]]) for raw_group in raw_groups]

# Bridge puzzle: place each group in the left set, and move them by one or two to the right set.
# This is followed by one or two moving from the right set to the left set.
# Each move costs an integer equal to the larger interger moved.
# We want to minimize total cost.

# Solution: consider integers i_0, i_1, ..., i_{k-2}, i_{k-1}. 
# We want to minimize cost - best we can do is hide i_{k-even} by pairing with i_{k-nextodd}.
# We'll need to utilize i_0, i_1 to most quickly move the torch back from right to left.
# Patterns:
  # Cost: i_0+2i_1+i_{k-1}
    # i_0, i_1 to right
    # i_0 to left
    # i_{k-2}, i_{k-1} to right
    # i_1 to left
  # Cost: 2*i_0+i_{k-2}+i_{k-1}
    # i_0, i_{k-1} to right
    # i_0 to left
    # i_0, i_{k-2} to right
    # i_0 to left
# Continue by recursion until just two or three left.
# Two left:
  # i_0, i_1 to right
# Three left:
  # i_0, i_2 to right
  # i_0 to left
  # i_0, i_1 to right
# For simplicity we won't actually move things right and left, we'll just keep track of how we would.

for group in groups: # [1, 5, 9, 100, 103]
  left = group[:]
  moves = []
  cost = 0
  while left != []:
    if len(left) > 3:
      # check two patterns
      if left[0]+2*left[1]+left[-1] < 2*left[0]+left[-2] + left[-1]:
        moves += [
          "%i %i" % (left[0], left[1]),
          "%i" % left[0],
          "%i %i" % (left[-2], left[-1]),
          "%i" % left[1]
          ]
        # track cost of these moves
        cost += left[0]+2*left[1]+left[-1]
      else:
        moves += [
          "%i %i" % (left[0], left[-1]),
          "%i" % left[0],
          "%i %i" % (left[0], left[-2]),
          "%i" % left[0]
          ]
        # track cost of these moves
        cost += 2*left[0]+left[-2]+left[-1]
      # remove last two from the list
      left = left[:-2]
    elif len(left) == 3:
      # use three pattern
      moves += [
        "%i %i" % (left[0], left[2]),
        "%i" % left[0],
        "%i %i" % (left[0], left[1])
        ]
      # track cost of these moves
      cost += left[0]+left[1]+left[2]
      # we've done it!
      left = []
    elif len(left) == 2: # len(left)==2
      # use two pattern
      moves += [
        "%i %i" % (left[0], left[1])
        ]
      # track cost of this move
      cost += left[1]
      # we've done it!
      left = []
    else: # len(left) = 1
      # use one pattern
      moves += [
        "%i" % left[0]
        ]
      # track cost of this move
      cost += left[0]
      # we've done it!
      left = []
  # let's print the results!
  print cost
  for move in moves:
    print move
  print ""





