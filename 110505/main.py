# Via proof.tex we know that Player I ("Stan") wins games G(x) provided x is of the form
  # 2**k * 9**k < x <= 2**k * 9**(k+1)
# and Player II ("Ollie") wins otherwise.
# We need simply verify
  # k < log_18 x <= k log_18 9
# that is,
  # 0 < log_18 x - floor(log_18 x) <= log_18 9

# If we don't mind floats...
# from math import log, floor
# def winning_player(x):
#   if 0 < log(x, 18) - floor(log(x, 18)) <= log(9, 18):
#     print "Stan wins."
#   else:
#     print "Ollie wins."

# we're guaranteed inputs less than 2**7 * 9**8, so:
lower_bounds = [9, 18, 162, 324, 2916, 5832, 52488, 104976, 
  944784, 1889568, 17006112, 34012224, 306110016, 612220032]
# generated from
  # lower_bounds = [2**(k/2) * 9**((k+1)/2) for k in range(1, 15)]
def winning_player(x):
  for index, bound in enumerate(lower_bounds):
    if x <= bound:
      if index % 2 == 0:
        return "Stan wins."
      else:
        return "Ollie wins."

import sys
readlines = sys.stdin.readlines() # reads input to list of strings for each line

for line in readlines:
  print winning_player(int(line))