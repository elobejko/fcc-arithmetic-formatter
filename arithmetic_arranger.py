def arithmetic_arranger(problems, if_print_res = False):

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
    if (eq[1] == "*" or eq[1] == "/"):
      return "Error: Operator must be '+' or '-'."
    
    if(len(eq[0]) > 4 or len(eq[2]) > 4):
      return "Error: Numbers cannot be more than four digits."

    if(count == len(problems)):
      space = ""
    
    if if_print_res:
      if(eq[1]== "+"):
        r = int(eq[0] + int[eq[2]])
      else:
        r = int(eq[0] - int[eq[2]])

    l1 = len("  " + eq[0])
    l2 = len(eq[1]+" "+eq[2])
    if l1 >= l2:
      firstNum = firstNum + 2 * " " + eq[0] + space
      secondNum = secondNum + eq[1] + (l1 - l2 + 1) * " " + eq[2] + space
      line = line + l1 * "-" + space
      res = res + " " * (l1 - len(str(r))) + str(r) + space 
    else:
      secondNum = secondNum + eq[1]+" "+eq[2] + space
      firstNum = firstNum + (l2- l1 + 2) * " " + eq[0] + space
      line = line + l2 * "-" + space
      res = res + " " * (l1 - len(str(r)) + str(r) + space 

  
    arranged_problems = firstNum +  "\n" + secondNum + "\n" + line
    if if_print_res:
      arranged_problems =+res 


  return arranged_problems