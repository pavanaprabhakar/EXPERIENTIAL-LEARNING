
def parse_seat(seat):
    if not isinstance(seat, str) or len(seat) < 2:
        raise ValueError("Invalid seat format")

    row = seat[0].upper()
    number = seat[1:]

    if not row.isalpha() or not number.isdigit() or int(number) <= 0:
        raise ValueError("Invalid seat format")

    return row, int(number)


def total_price(prices_csv):
    if not isinstance(prices_csv, str) or not prices_csv.strip():
        raise ValueError("Invalid ticket prices")

    try:
        prices = [int(p.strip()) for p in prices_csv.split(',')]
    except ValueError:
        raise ValueError("Ticket prices must be valid integers")

    if any(price < 0 for price in prices):
        raise ValueError("Ticket prices cannot be negative")

    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    if not isinstance(ratings, str) or not ratings.strip():
        raise ValueError("Ratings cannot be empty")

    try:
        values = [int(r) for r in ratings.split()]
    except ValueError:
        raise ValueError("Ratings must be integers")

    if any(r < 1 or r > 5 for r in values):
        raise ValueError("Ratings must be between 1 and 5")

    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    try:
        result = parse_seat(user_input)
        print("Row and Seat:", result)
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    try:
        result = total_price(user_input)
        print("Total with GST:", result)
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    try:
        result = average_rating(user_input)
        print("Average Rating:", result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
