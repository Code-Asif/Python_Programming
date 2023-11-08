# It is a simple quiz game in which you can consequtively answer all the question and earn some rewards

questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "What is the size of float and double in java?", "32 and 64", "32 and 32", "64 and 64",
    "64 and 32", "None", 1
  ],
  [
    "Automatic type conversion is possible in which of the possible cases?", "Byte to int", "int to long", "Long to int",
    "short to int", "None", 2
  ],
  [
    "Select the valid statement", "char[] ch = new char(5)", "char[] ch = new char[5]", "chat[] ch = new char()",
    "char[] ch = new char[]", "None", 2
  ],
  [
    "When an array is passed to a method, what does the method receive?", "The reference of array", "A copy of the array", "Length of the array",
    "Copy of first element", "None", 1
  ],
  [
    "Select the valid statement to declare and initialize an array.", "int []a = {}", "int []a = {1,2,3}", "int []a = (1,2,3)",
    "int [][]a = {1,2,3}", "None", 2
  ],
  [
    "Arrays in java are-", "Object reference", "Object", "Primitive data types",
    "Class", "None", 1
  ],
  [
    "When is the object created with new keyword?", "At run time", "At compile time", "Depends on the code",
    "Never", "None", 1
  ],
  [
    "Identify the keyword among the following that makes a variable belong to a class,rather than being defined for each instance of the class.", "final", "static", "volatile",
    "abstract", "None", 2
  ],
  [
    "compareTo() returns", "true", "flase", "An int value",
    "Nothing", "None", 3
  ],
  [
    "To which of the following does the class string belong to.", "java.lang", "java.awt", "java.applet",
    "java.string", "None", 1
  ],
  [
    "Total constructor string class have?", "3", "7", "13",
    "20", "None", 3
  ],
  [
    "Identify the return type of a method that does not return any value.", "int", "void", "double",
    "short", "None", 2
  ],
  [
    "Output of Math.floor(3.6)?", "3", "3.0", "4",
    "4.0", "None", 2
  ],
  [
    "Where does the system stores parameters and local variables whenever a method is invoked?", "Heap", "stack", "array",
    "tree", "None", 2
  ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"Q. {question[0]}")
  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")