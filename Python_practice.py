# print("Hello World")

# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == "Denver":
#         print(counties[1])

# # temperature = int(input("What is the temperature outside?"))
# # if temperature >80:
# #     print("Turn on the AC.")
# # else: 
# #     print("Open the windows.")

# # grade = int(input("What is your Grade?  "))
# # if grade >= 90:
# #     print("Your grade is an A")
# # else:
# #     if grade >= 80:
# #         print("Your grade is a B")
# #     else:
# #         if grade >= 70:
# #             print("Your grade is a C")
# #         else:
# #             if grade >= 60:
# #              print("Your grade is a D")
# #             else:
# #                 print("Your grade is an an F.")

# # counties = ["Arapahoe","Denver","Jefferson"]
# # if "El Paso" in counties:
# #     print("El Paso is in the list of counties.")
# # else:
# #     print("El Paso is not the list of counties.")

# # if "Arapahoe" in counties and "El Paso" in counties:
# #     print("Arapahoe and El Paso are in the list of counties.")
# # else:
# #     print("Arapahoe or El Paso is not in the list of counties.")

# # if "Arapahoe" in counties or "El Paso" in counties:
# #     print("Arapahoe or El Paso is in the list of counties.")
# # else:
# #     print("Arapahoe and El Paso are not in the list of counties.")

# x = 0
# while x <=5:
#     print(x)
#     x = x+1

# for county in counties:
#     print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print (counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))   

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict.values())

# for county_dict in voting_data:
#     for value in county_dict:
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

# for county_dict in voting_data:
#     print(county_dict['county'])

# Skill Drill #1 (3.2.11)
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:{2},} registered voters.")

# Skill Drill #2 (3.2.11)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
        print(f"{county_dict['county']} county has {county_dict['registered_voters']:{2},} registered voters.")