# First obtain the users first, middle and last name and capitalise() the first letter of each
first_name = input("Please provide your first name. ").capitalize()
middle_name = input("Please provide your middle name. ").capitalize()
last_name = input("Please provide your last name. ").capitalize()

# Then obtain the first line of the users address and title() so that the first letter in every word is capitalised
address = input("Please provide the first line of your address in the format - 000 Road Name - ").title()

# Obtain their postcode, capitalise every letter by upper()
post_code = input("Please provide your post code in the format - BB00 B00 ").upper()

# Obtain their national insurance number, every letter needs to be capitalised so upper()
ni_number = input("Please provide your National Insurance Number. ").upper()

# Obtain their course name, use title() as course names can be multiple words long
course = input("Please provide the course you've applied to. ").title()

# Obtain their education level and capitalise the first letter
education = input("Please provide your most recent education level. ").capitalize()

# Then print everything in one statement
print(
      f""" User Details:
Hello {first_name} {middle_name} {last_name}. 
You live at:
{address},
{post_code}.
Your National Insurance Number is {ni_number}.
You applied to the {course} course and your current education level is {education}.
"""
)