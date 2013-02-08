## NOT FINISHED ##



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

def job_cost(job, case):
  return job[1]*(sum([otherjob[2] for otherjob in case]) - job[2]) # length of job times fines of other jobs

def job_cost_cmp(case):
  return lambda job, otherjob: job_cost(job, case) - job_cost(otherjob, case) if not 0 else job[0]-otherjob[0]

# we need to find the least expensive job. Since being greedy doesn't work, we'll need to recurse
def cheapest_job(case):
  """
  Returns:
  ((tuple_of_cheapest_job), cheapest_job_cost)
  """
  # if just two, should pick the job with the smallest fine
  if len(case)==2:
    return (
      sorted(case, job_cost_cmp(case))[0], 
      job_cost(sorted(case, job_cost_cmp(case))[0], case)
      )
  # if more than 2, consider cost of choosing each by recursing cheapest_job on leftovers
  if len(case)>2:
    case_with_costs = []
    for n, job in enumerate(case):
      case_with_costs.append((job, job_cost(job, case) + job_cost(cheapest_job(case[:n]+case[n+1:])[0], case[:n]+case[n+1:])))
    return sorted(case_with_costs, lambda x,y: x[1]-y[1] if not 0 else x[0][0]-y[0][0])[0]

for case in cases:
  result = ""
  while len(case) > 1:
    cheap_job = cheapest_job(case)
    print cheap_job
    result += "%i " % cheap_job[0][0]
    case = case.remove(case.index(cheap_job[0]))
  print result + "%i " % case[0][0]



# FAIL - Greedy algorithm fails us in the given test case!
        # # For each case, we can assign the cost for doing a particular job by adding the fines levied for skipping 
        # # every other job. We'll choose the job with the minimal cost.

        # # we'll use this in a moment
        # def cost(job, case):
        #   return (sum([any_job[3] for any_job in case])-job[3])*job[2]

        # for case in cases:
        #   jobs_with_cost = sorted([(cost(job, case) , job[1], job[2], job[3]) for job in case])
        #   result = ""
        #   print "  ----"
        #   while jobs_with_cost != []:
        #     print jobs_with_cost
        #     result += "%i " % jobs_with_cost[0][1]
        #     jobs_with_cost = sorted([(cost(job, jobs_with_cost[1:]) , job[1], job[2], job[3]) \
        #       for job in jobs_with_cost[1:]])
        #   print "  ----"
        #   print result + "\n"

