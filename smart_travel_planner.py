"""A beginner-friendly console program for planning a travel budget."""


def calculate_transportation_cost(cost_per_traveler: float, travelers: int) -> float:
    """Return the total transportation cost for all travelers."""
    return cost_per_traveler * travelers


def calculate_hotel_cost(cost_per_day: float, days: int) -> float:
    """Return the total hotel cost for the whole trip."""
    return cost_per_day * days


def calculate_food_cost(cost_per_traveler_per_day: float, travelers: int, days: int) -> float:
    """Return the total food cost for all travelers and days."""
    return cost_per_traveler_per_day * travelers * days


def calculate_activity_cost(cost_per_traveler: float, travelers: int) -> float:
    """Return the total activity cost for all travelers."""
    return cost_per_traveler * travelers


def calculate_overall_trip_cost(
    transportation_cost: float,
    hotel_cost: float,
    food_cost: float,
    activity_cost: float,
) -> float:
    """Return the sum of all trip costs."""
    return transportation_cost + hotel_cost + food_cost + activity_cost


def calculate_cost_per_traveler(overall_cost: float, travelers: int) -> float:
    """Return the average trip cost for one traveler."""
    return overall_cost / travelers


def calculate_average_daily_cost(overall_cost: float, days: int) -> float:
    """Return the average cost for one day of the trip."""
    return overall_cost / days


def get_positive_integer(prompt: str) -> int:
    """Read an integer greater than zero from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


def get_non_negative_float(prompt: str) -> float:
    """Read a number that is zero or greater from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Cost cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def display_summary(travel: dict[str, str | int | float], calculations: dict[str, float]) -> None:
    """Display the collected information and calculated travel budget."""
    print("\n" + "=" * 50)
    print("SMART TRAVEL PLANNER - TRAVEL SUMMARY")
    print("=" * 50)
    print(f"Travel name:              {travel['name']}")
    print(f"Destination:              {travel['destination']}")
    print(f"Number of travelers:      {travel['travelers']}")
    print(f"Number of travel days:    {travel['days']}")
    print("-" * 50)
    print(f"Total transportation:     ${calculations['transportation']:,.2f}")
    print(f"Total hotel:              ${calculations['hotel']:,.2f}")
    print(f"Total food:               ${calculations['food']:,.2f}")
    print(f"Total activities:         ${calculations['activity']:,.2f}")
    print("-" * 50)
    print(f"Overall trip cost:        ${calculations['overall']:,.2f}")
    print(f"Cost per traveler:        ${calculations['per_traveler']:,.2f}")
    print(f"Average daily cost:       ${calculations['daily_average']:,.2f}")
    print("=" * 50)


def main() -> None:
    """Collect travel information, calculate the budget, and show a summary."""
    print("Welcome to Smart Travel Planner!")
    print("Enter your travel information below.\n")

    travel: dict[str, str | int | float] = {
        "name": input("Travel name: ").strip(),
        "destination": input("Destination: ").strip(),
        "travelers": get_positive_integer("Number of travelers: "),
        "days": get_positive_integer("Number of travel days: "),
        "transportation_per_traveler": get_non_negative_float(
            "Transportation cost per traveler: $"
        ),
        "hotel_per_day": get_non_negative_float("Hotel cost per day: $"),
        "food_per_traveler_per_day": get_non_negative_float(
            "Food cost per traveler per day: $"
        ),
        "activity_per_traveler": get_non_negative_float(
            "Activity cost per traveler: $"
        ),
    }

    travelers = int(travel["travelers"])
    days = int(travel["days"])
    transportation = calculate_transportation_cost(
        float(travel["transportation_per_traveler"]), travelers
    )
    hotel = calculate_hotel_cost(float(travel["hotel_per_day"]), days)
    food = calculate_food_cost(
        float(travel["food_per_traveler_per_day"]), travelers, days
    )
    activity = calculate_activity_cost(float(travel["activity_per_traveler"]), travelers)
    overall = calculate_overall_trip_cost(transportation, hotel, food, activity)

    calculations = {
        "transportation": transportation,
        "hotel": hotel,
        "food": food,
        "activity": activity,
        "overall": overall,
        "per_traveler": calculate_cost_per_traveler(overall, travelers),
        "daily_average": calculate_average_daily_cost(overall, days),
    }
    display_summary(travel, calculations)


if __name__ == "__main__":
    main()