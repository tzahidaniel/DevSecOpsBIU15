# try:
#     x = input("Please add a number:")
#     init_x = int(x)
#     print("Thank you")
#
#
# except:
#     print("Oops")
#
#
#

while True:
    try:
        num_str = input("please enter a number: ")
        x = int(num_str)
        break
    except:
        print ("please try again:")


print("ALL GOOD")