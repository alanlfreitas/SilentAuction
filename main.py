# -------------------- Silent Auction -------------------- #
# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.",
#   "Function": "A piece of code that you can easily call over and over again.",
# }
# #Retrieving item from dictionary
# # print(programming_dictionary["Bug"])

# #Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."


# #Creating an empty dictionary
# empty_dictionary = {}

# #wipe and existing dictionary
# #programming_dictionary = {}
# # print(programming_dictionary)

# #Editing and item in the dictionary
# programming_dictionary["Bug"] = "Just a bug."
# # print(programming_dictionary)

# #Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"

# print(student_grades)

# ########## Nesting ##########
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# # Nesting a List in a Dictionary
# travel_log1 = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nesting a Dictionary in a Dictionary
# travel_log2 = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 3},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 3},
#   "Brazil": {"cities_visited": ["Fortaleza", "Rio", "Presidente Figueiredo",
#   "Itacoatiara", "Iranduba", "Boa Vista"], "total_visits": 6}
# }

# # Nesting Dictionary in a List

# travel_log = [
#   {
#     "country": "France", 
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 3
#   },
#   {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 3
#   },
#   {
#     "country": "Brazil",
#     "cities_visited": ["Fortaleza", "Rio", "Presidente Figueiredo"],
#     "total_visits": 3
#   }
# ]
# print(travel_log)

# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]

# def add_new_country(name, times_visited, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = times_visited
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)

# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  #bidding_record = {"Alan": 123, "Hothna": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
  
while not bidding_finished:
  name = input("What's your name? ")
  bid_price = int(input("What's your bid? $"))
  bids[name] = bid_price
  should_continue = input("Are there any other bidders? 'Yes' or 'No'. ").lower()
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

