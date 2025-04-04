#take input from user
rows = int(input("Enter number of rows: "))
number = 1 #initialize by 1
print("Floyd's Triangle")
#outer loop to handle number of rows
for i in range(1, rows + 1):
  #inner loop to handle number of columns
  for j in range(1, i + 1):
    #dispaly the reslult
   print(number, end=" ")
   number = number + 1
  print()