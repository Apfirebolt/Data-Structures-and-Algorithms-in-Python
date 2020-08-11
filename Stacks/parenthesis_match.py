"""Parenthesis match problem using stacks, given a string containing (, { and ]. Determine if it is balanced"""

s = '[()]{}{[()()]()}'
stack = []
n = len(s)
i = 0

while i < n:
  if len(stack):
    toPop = False
    stack_top = stack[len(stack)-1]
    if s[i] == ')' and stack_top == '(':
      toPop = True
    elif s[i] == '}' and stack_top == '{':
      toPop = True
    elif s[i] == ']' and stack_top == '[':
      toPop = True
    if toPop:
      stack.pop()
      i += 1
      continue
  stack.append(s[i])
  i += 1

if not len(stack):
  print('Balanced')
else:
  print('Not Balanced')

