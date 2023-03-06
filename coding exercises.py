'''
dollars = input("Enter Amount to calculate: ")

euros = int(dollars)*0.95

print("Amount in Euros: " + str(euros))
'''

ranking = ['John', 'Sen', 'Lisa']

ranknumber = input("Enter a name: ")
#print("Corresponding athlete: " + ranking[int(ranknumber)])
name = ranking.index(ranknumber)
print("Corresponding athlete: " + str(name) )