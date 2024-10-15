m = int(input("Введите число  m: "))
n = int(input("Введите число  n: "))
arr = list()
for i in range(m):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
print(arr)
#output array
# for i in range(m):
#   for j in range(n):
#     print(arr[i][j], end = ' ')
#   print()

for i in range(len(arr)):
  for j in range(len( arr[i])):
    if arr[i][j] < 0:
      arr[i][j]= 0 
    else:
      arr[i][j]= 1 
#output array
# for i in range(m):
#   for j in range(n):
#   print()
# print(arr)

#3

# n = int(input("Введите число  n: "))
# arr = list()
# for i in range(т):
#   brr = list()
#   for i in range(n):
#     brr.append(int(input()))
#   arr.append(brr)
# print(arr)
arr = [[2,7,6,],[9,5,1],[4,3,8]]
control = sum(arr[0]) 
print(control)
for i in range(len(arr)):
    sum_diag = 0
    sum_column = 0
    sum_row = 0

    for j in range(len( arr[i])):
       sum_row += arr[i][j]
       if sum_row != control:
          print('не магический квадрат')
       if i == j:
        sum_diag += arr[i][j]
    # sum_column = sum(arr[i][j])
  