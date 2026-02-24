# Print even no
# for variable in range(2,21,2):
#     print(variable)

# for i in range(1, 51):
#     if i % 5 == 0:
#         continue
#     print(i)


# orders = [1200, 450, 8000, 300, 15000]

# for order in orders:
#     if order > 10000:
#         print(f"High value order {order}")
#     elif order > 1000:
#         print(f"Order in Processing {order}")

# orders = [1200, 450, 8000, 300, 15000, 700, 20000]
# valid_count = 0 
# count = 0
# rev = 0

# for order in orders:
#     if order < 1000:
#         continue
#     if order >1000:
#         valid_count += 1
#         rev += order
#     if order > 10000:
#         count += 1

# print(f"Total valid orders: {valid_count}")
# print(f"Total High orders: {count}")
# print(f"Total Rev: {rev}")


# orders = [1200, 450, 8000, 300, 15000, 700, 20000]

# max_value = orders[0]

# for order in orders:
#     if max_value < order:
#         max_value = order
# print(max_value)

# highest = orders[0]
# second_highest = orders[0]

# for order in orders:
#     if order > highest:
#         second_highest = highest
#         highest = order
#     elif order > second_highest and order != highest:
#         second_highest = order
# print (second_highest)


# user_input = int(input("Enter your num: "))
# i = 1

# while i <= 10:
#     print(f"{user_input} x {i} = {user_input*i}")
#     i += 1

# user_input = int(input("Enter your num: "))
# i = 1
# if user_input > 0:
#     while i <= 10:
#         print(f"{user_input} x {i} = {user_input * i}")
#         i += 1
# else:
#     print('enter valid num')

# for i in range(7):
#     for j in range(i):
#         print ("*", end= "")
#     print()

# for i in range(7, 0, -1):
#     print ("*" * i)
   


# num = [10, 202, 95, 85]
# print(*num)

