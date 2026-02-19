#budget tool

#import summary

rules = """
	1. Press '0' to exit

"""
while True:
	print(rules)
	n = input("\n Enter Number: ")

	if n == 0:
		print("Thank you for using the budget tool")
		break
