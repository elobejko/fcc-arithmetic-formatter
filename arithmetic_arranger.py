def arithmetic_arranger(problems, print_res = False):

  if(len(problems) > 5):
    return "Error: Too many problems."

  firstLine = ""
  secondLine = ""
  thirdLine = ""
  space = "    "
  count = 0
  resultsLine = ""
  r = 0

  for problem in problems:
    eq = problem.split()
    count +=1
    #Only  + and - operators are accepted
    if (eq[1] == "*" or eq[1] == "/"):
      return "Error: Operator must be '+' or '-'."
    #Number cannot be longer than four digits
    if(len(eq[0]) > 4 or len(eq[2]) > 4):
      return "Error: Numbers cannot be more than four digits."
    #No spaces after last problem
    if(count == len(problems)):
      space = ""
    #Number can contain inly digits
    try:
      x = int(eq[0])
      y = int(eq[2])
    except ValueError:
      return "Error: Numbers must only contain digits."
    #Calculate results
    if print_res:
      if(eq[1]== "+"):
        r = x + y
      else:
        r = x - y

    maxlen = max(len(eq[0]), len(eq[2]))
    firstLine = firstLine + eq[0].rjust(maxlen + 2) + space
    secondLine = secondLine + eq[1] + eq[2].rjust(maxlen + 1) + space
    thirdLine = thirdLine + (maxlen + 2) * "-" + space
    resultsLine = resultsLine +  str(r).rjust(maxlen + 2) + space 

  arranged_problems = firstLine + "\n" + secondLine + "\n" + thirdLine
  if print_res:
    arranged_problems = arranged_problems + "\n" + resultsLine 
  
  return arranged_problems