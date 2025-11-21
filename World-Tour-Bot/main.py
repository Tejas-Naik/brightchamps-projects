# World Tour Planner Bot 

# Welcome message
print("Welcome to the World Tour Planner Bot!\n")
print("Answer a few questions to get your personalized travel destination.\n")

# Questions and user input
budget = input("What is your budget range? (low/medium/high): ").strip().lower()
season = input("What is your preferred season? (spring/summer/autumn/winter): ").strip().lower()
continent = input("Which continent would you like to visit? (north america/south america/europe/asia): ").strip().lower()

# Destination suggestions based on user input
destination = ""

# Budget: Low
if budget == "low":
    if continent == "asia":
        if season == "spring" or season == "autumn":
            destination = "Vietnam"
        else:
            destination = "Thailand"
    elif continent == "south america":
        if season == "autumn" or season == "winter":
            destination = "Peru"
        else:
            destination = "Brazil"
    elif continent == "europe":
        if season == "spring" or season == "summer":
            destination = "Greece"
        else:
            destination = "Italy"
    elif continent == "north america":
        destination = "Canada"

# Budget: Medium
elif budget == "medium":
    if continent == "north america":
        if season == "summer" or season == "autumn":
            destination = "Canada"
        else:
            destination = "USA"
    elif continent == "south america":
        destination = "Brazil"
    elif continent == "asia":
        destination = "Japan"
    elif continent == "europe":
        if season == "summer" or season == "autumn":
            destination = "Spain"
        else:
            destination = "France"

# Budget: High
else:
    if continent == "north america":
        if season == "summer" or season == "autumn":
            destination = "USA"
        else:
            destination = "Canada"
    elif continent == "south america":
        if season == "spring" or season == "summer":
            destination = "Argentina"
        else:
            destination = "Chile"
    elif continent == "asia":
        destination = "Maldives"
    elif continent == "europe":
        if season == "summer" or season == "autumn":
            destination = "Switzerland"
        else:
            destination = "Norway"

# Display the suggested destination
if destination:
    print("\nBased on your preferences, we recommend visiting " + destination + " for your world tour!")
else:
    print("\nSorry, we couldn't find a suitable destination based on your preferences.")



