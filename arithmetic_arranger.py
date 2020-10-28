def arithmetic_arranger(problems, ifprint = False):

  if(len(problems) > 5):
    return "Error: Too many problems."

  firstNum = ""
  secondNum = ""
  line = ""

  for elem in problems:
    eq = elem.split()
    if (eq[1] == "*" or eq[1] == "/"):
      return "Error: Operator must be '+' or '-'."
    if(len(eq[0]) > 4 or len([2]) > 4):
      return "Error: Numbers cannot be more than four digits."

    l1 = len(eq[0])
    l2 = len(eq[1]+" "+eq[2])
    if l1 >= l2:
      firstNum = firstNum + 2 * " " + eq[0] + "    "
      secondNum = secondNum + eq[1] + (l1 - l2 + 3) * " " + eq[2] + "    "
      line = line + l1 * "-" + "    "
    else:
      secondNum = secondNum + eq[1]+" "+eq[2] + "    "
      firstNum = firstNum + (l2- l1 + 2) * " " + eq[0] + "    "
      line = line + l2 * "-" + "    "

  arranged_problems = firstNum +  "\n" + secondNum + "\n" + line

  if ifprint:
    print(arranged_problems)

  return arranged_problems