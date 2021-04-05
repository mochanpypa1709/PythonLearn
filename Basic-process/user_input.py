name = "Sim"
experience_years = 1.5

print("Hi %s, you have %s years of experience." % (name, experience_years))
print("Hi {}, you have {} years of experience".format(name, experience_years))

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
print(experience_years)