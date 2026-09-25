# Smart Travel Planner

Smart Travel Planner is a beginner-friendly Python console program that estimates
the budget for a trip. It collects a travel name, destination, group size, trip
length, transportation cost, hotel cost, food cost, and activity cost. It then
prints a formatted travel summary.

## How to run

Open a terminal in this folder and run one of these commands:

```text
py smart_travel_planner.py
# or: python smart_travel_planner.py
```

The program asks for each value one at a time. Travelers and days must be whole
numbers greater than zero. Costs must be zero or greater.

## What the program demonstrates

- Variables and suitable data types: `str`, `int`, `float`, and `dict`
- Input conversion with `int()` and `float()`
- Input validation with loops and `try`/`except`
- Separate functions with parameters and return values for each calculation
- Arithmetic operations for transportation, hotel, food, and activity costs
- Formatted currency output in a final travel summary

The `travel` dictionary organizes related trip information, while the
`calculations` dictionary organizes the calculated results. The program uses
only Python built-in features and does not use files, databases, APIs,
external libraries, or classes.