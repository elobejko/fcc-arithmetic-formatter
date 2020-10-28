def arithmetic_arranger(problems, print_res = False):

  if(len(problems) > 5):
    return "Error: Too many problems."

  firstNum = ""
  secondNum = ""
  line = ""
  space = "    "
  count = 0
  res = ""
  r = 0

  for elem in problems:
    eq = elem.split()
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
      int(eq[0])
      int(eq[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    #Calculate results
    if print_res:
      if(eq[1]== "+"):
        r = int(eq[0]) + int(eq[2])
      else:
        r = int(eq[0]) - int(eq[2])

    l1 = len("  " + eq[0])
    l2 = len(eq[1]+" "+eq[2])

    if l1 >= l2:
      firstNum = firstNum + eq[0].rjust(l1) + space
      secondNum = secondNum + eq[1] + eq[2].rjust(l1-1) + space
      line = line + l1 * "-" + space
      res = res +  str(r).rjust(l1) + space 
    else:
      secondNum = secondNum + eq[1]+ " " + eq[2] + space
      firstNum = firstNum + (l2- l1 + 2) * " " + eq[0] + space
      line = line + l2 * "-" + space
      res = res + str(r).rjust(l2) + space

  arranged_problems = firstNum + "\n" + secondNum + "\n" + line
  
  if print_res:
    arranged_problems = arranged_problems + "\n" + res 
  
  return arranged_problems