x = 3
 
print(x)

numbers = [-4, 3, -2, -1, 0, 2, 4, 6]
newlist = [number for number in numbers if number <= 0]
print(newlist)
#2
lists_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened_lists = []
for sublist in lists_of_lists:
  for items in sublist:
    flattened_lists.append(items)
    print(flattened_lists)
#3
output = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range (11)]  
print(output)
#4
countries =[[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
output =[[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]
print(output)

#5
Countries = [[("Finland", "Helsink")], [("sweden", "Stockholm")], [("Norway", "Oslo")]]
output = [{"country": country.upper(), "city": city.upper()} for sublist in countries for(country, city) in sublist]
print(output)
#6
names = [[("Asabeneh", "Yetaeyeh")], [("David", "Smith")],[("Donald", "Trump")],[("Bill","Gates")]]
fullnames = []
for sublist in names:
  for first, last in sublist:
    fullnames.append(f"{first} {last}")
    print(fullnames)
 

