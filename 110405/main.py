# read input to list of strings for each line
import sys
readlines = sys.stdin.readlines()

# want to break input into chunks delimited by '\n'
import itertools
raw_cases = [list(group) for is_key, group in itertools.groupby(readlines, lambda x: x == '\n') \
  if not is_key]

# first entry just gives len(raw_cases)-1
raw_cases = raw_cases[1:]

#cleanup time: each case starts with length of case (should drop), each line is then '%i %i\n'
cases = [[tuple([n+1]+[int(x) for x in item.split()]) for n, item in enumerate(raw_case[1:])] \
  for raw_case in raw_cases]

# data is now structured
  # cases =
  #   [
  #     [
  #       (1, length1, fine1),
  #       (2, length2, fine2),
  #       ...
  #     ],
  #     [
  #       (1, length1, fine1),
  #       (2, length2, fine2),
  #       ...
  #     ]
  #   ]

# Rather than check every ordering of jobs, we can just consider which job is best to go first by
# greedily picking the cheapest job, and then reassessing the remaining jobs similarly.

def job_cost_cmp(job, otherjob):
  return job[1]*otherjob[2] - otherjob[1]*job[2] if not 0 else job[0]-otherjob[0]

def sorted_case(case):
  return sorted(case, job_cost_cmp)

def job_order(case):
  if len(case) == 1:
    return "%i" % case[0][0]
  else:
    return "%i %s" % (sorted_case(case)[0][0], job_order(sorted_case(case)[1:]))

for case in cases:
  print job_order(case)

