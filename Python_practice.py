print("Hello World")
print(type(3))
print(type(2019))
ballots = 1341
print(type(ballots))
print(type(73.81))
print(type('Hello World'))
print(type(True))

print("------------")
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16- 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)
print("------------")
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / (2 - 4)))

counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0])
print(counties[1])
print(counties[2])
print(counties[-1])
print(counties[-2])
print(counties[-3])

print("--------------")
print(len(counties))
print("--------------")
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
print(counties[1:3])
print("--------------")

counties.append("El Paso")
counties.insert(2, "El Paso")
print(len(counties))
print(counties)

counties.remove("El Paso")
print(len(counties))
print(counties)

counties.pop(3)
#counties.pop(-1)
print(counties)

print("-------Update-------")
counties[2] = "El Paso"
print(counties)
print("----------------------")

counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
print(counties)
counties.remove("Denver")
counties.insert(2,"Denver")
counties.append("Arapahoe")
print(counties)
print("----------------")


counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])
print(counties_tuple[:2])
print(counties_tuple[:-1])
print("------------------")

counties_dict = {}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"] = 432438
len(counties_dict)

print(counties_dict["Arapahoe"])
print(counties_dict["Denver"])
print(counties_dict["Jefferson"])
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print("---------------")

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
len(voting_data)

print(voting_data[0]["county"])
print(voting_data[0].get("county"))
print(voting_data[0]["registered_voters"])
print(voting_data[0].get("registered_voters"))
voting_data.append({"county": "El Paso", "registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.pop(0)
voting_data.pop(0)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
print("------------------")

# # How many votes did you get?
# my_votes=int(input("How many votes did you get in the election?"))
# # Total votes in the election
# total_votes=int(input("What is the total votes in the election?"))
# # Calculate the percentage of votes you received.
# percentage_votes=(my_votes / total_votes) * 100
# print("I received" + str(percentage_votes)+"% of the total votes.")
# print("-"* 100)
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# print("--------------")

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
   print("Open the windows.")

# print("--------------")

# What is the score?
score=int(input("What is your test score? "))

# Determinte the grade.
if score>=90: 
    print('Your grade is an A.')
else:
    if score>=80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print ('Your grade is a C.')
        else:
            if score >=60:
                print('Your grade is a D')
            else:
                print('Your grade is an F.')

# What is the score?
#score=int(input("What is your test score? "))

# Determinte the grade.
#if score>=90: 
    #print('Your grade is an A.')
    #elif score >= 80:
        #print('Your grade is a B.')
    #elif score >= 70:
        #print ('Your grade is a C.')
    #elif score >=60:
        #print('Your grade is a D.')
    #else:
        #print('Your grade is an F.')

# print("--------------")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

count=7
while count < 1:
    print("Hello World")

counties_tuple=("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)): 
    print(counties_tuple[i])
    print("------------------")

x=0
while x<=5:
    print(x)
    x=x+1