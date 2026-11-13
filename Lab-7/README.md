
# L6_L7_15_movie_tickets — Movie Tickets

## Lab 7: Fuzz Testing Using Hypothesis

### Objective
To identify input-validation bugs in the Movie Tickets application using property-based testing with Hypothesis and fix the identified issues.

### Files

| File | Description |
|------|-------------|
| `movie_tickets.py` | Corrected application with input validation and error handling |
| `test_movie_tickets.py` | Hypothesis-based fuzz tests for all three functions |
| `README.md` | Project documentation |

### Functions Tested
1. `parse_seat()` – Validates and parses seat numbers.
2. `total_price()` – Calculates the total ticket price including GST.
3. `average_rating()` – Calculates the average of customer ratings.

### Testing
Run the tests using:

`python -m pytest test_movie_tickets.py`

### Result
All three Hypothesis tests passed after fixing the input-validation bugs.

### Technologies Used
- Python
- pytest
- Hypothesis
