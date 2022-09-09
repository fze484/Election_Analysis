print("Hello World")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print("--------------")
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)
print("--------------")
voting_data[1]=({"county":"El Paso", "registered_voters": 461149})
print(voting_data)
print("--------------")

voting_data.pop(0)
print(voting_data)
print("--------------")

voting_data.append({"county":"Denver", "registered_voters": 463353})
print(voting_data)
print("--------------")

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)

print("--------------")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

print("--------------")
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

print("--------------")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

print("--------------")
for county, voters in counties_dict.items():
    print(county, voters)
print("--------------")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print("--------------")
for i in range(len(voting_data)):

      print(voting_data[i]['county'])
print("--------------")
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("--------------")
""" candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.") 
print(message_to_candidate)"""



print("--------------")
print("Print each county and registered voter from the dictionary") 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, value in counties_dict.items():
    print(f"{key} county has a total of {value} voters")

print("--------------")
print("Print each county and registered voter from the dictionary") 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for dictio in voting_data:
    print(f"{dictio['county'] } county has a total of {dictio['registered_voters']} voters")
