from datetime import datetime

preferred_airlines = [
    {"Airline": "Russia", "price": 3000, "Date": "1/11/24"},
    {"Airline": "Amarides Airlines", "price": 2000, "Date": "1/14/24"},
    {"Airline": "PIA", "price": 2000, "Date": "1/17/24"},
    {"Airline": "Air bangladesh", "price": 3200, "Date": "1/10/24"},
    {"Airline": "Alaska Air", "price": 1400, "Date": "1/20/24"},
    {"Airline": "sudia Arabia", "price": 1000, "Date": "2/2/24"},
    {"Airline": "IndiGo", "price": 1900, "Date": "1/10/24"}
]

def flight(destination, flexibility_days, budget, preferred_airlines):
    selected_flight = None
    for airline in preferred_airlines:
        if airline["Airline"].lower() in ["russia", "amarides airlines", "pia", "air bangladesh", "alaska air", "sudia arabia", "indigo"]:
            if airline["price"] <= budget:
                airline_date = datetime.strptime(airline["Date"], "%m/%d/%y")
                start_date, end_date = [datetime.strptime(date, "%m/%d/%y") for date in flexibility_days.split(" to ")]
                if start_date <= airline_date <= end_date:
                    budget = airline["price"]
                    selected_flight = airline
    return selected_flight

selected_airline = flight("some destination", "1/10/24 to 1/13/24", 2000, preferred_airlines)
if selected_airline:
    print(f"The flight is with {selected_airline['Airline']} for ${selected_airline['price']}")
else:
    print("No flights found with preferred airline.")
