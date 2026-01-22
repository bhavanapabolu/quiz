

q1='''Is python case sensitive when dealing with identifiers?
a.Yes
b.No
c.Machine indenpendent
d.None'''
q2='''Which of the following is not a keyword?
a.eval
b.assert
c.local
d.pass'''
q3='''Which one of these is a floor division operator?
a./
b.//
c.%
d.None'''
q4='''What is the output of this 3*1**3?
a.27
b.9
c.3
d.1'''
q5='''Which type of programming does python support?
a.object oriented programming
b.structured programming
c.functional programming
d.all of the mentioned'''
q6='''Which of the correct extension of the python file?
a..python
b.pl
c..py
d..p'''
q7='''All keywords in python are in____________
a.Capitalized
b.Lower case
c.Upper case
d.None of the mentioned'''
q8='''Which of the following is used to define a block of code in python language?
a.Indentation
b.Key
c.Brackets
d.All of the mentioned'''
q9='''Which of the following functions in a buitl-in function in python?
a.factorial()
b.print()
c.seed()
d.sqrt()'''
q10='''Which of the following is not a core data type in python programming?
a.Tuples
b.Lists
c.Class
d.Dictionary'''
questions={q1:"a",q2:"a",q3:"b",q4:"c",q5:"d",q6:"c",q7:"d",q8:"a",q9:"b",q10:"c"}
name=input("Enter your name:")
print("Hello",name,"Welcome to quiz")
score=0
for i,j in questions.items():
  print()
  print(i)
  option=input("Do you want to skip the question(yes/no):")
  if option=="yes":
     continue
  ans=input("Enter your answer(a/b/c/d):")
  if ans==questions[i]:
      print("Correct answer")
      score=score+1
      print("Current score is:",score)
  else:
      print("Wrong answer you lost 1 point")
      print("Current score is:",score)
print("Final score is:",score)
print("You got ",score," points out of 10 points")
print("THANK YOU FOR USING THIS APPLICATION")

     