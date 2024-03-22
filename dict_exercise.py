student_mark={
  "Jenny":92,
  "Harry":78,
  "Dimpy":56,
  "Rahul":41,
  "Aniket":99,
  "Prem":34
}



for k,v in student_mark.items():
  if v in range(91,101):
   student_mark[k]='A+'
  elif v in range(81,91):
   student_mark[k]='A'
  elif v in range(71,81):
   student_mark[k]='B+'
  elif v in range(61,71):
   student_mark[k]='B'
  elif v in range(51,61):
   student_mark[k]='C'
  elif v in range(41,50):
   student_mark[k]='D'
  else:
   student_mark[k]='F'
print(student_mark)

D={1:10,2:20,3:30}
print(D.keys())
print(D.values())
print(D.items())
 