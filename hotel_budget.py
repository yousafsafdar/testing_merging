def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    if days >= 7:
        cost = 40 * days - 50
        return cost
    elif days >= 3:
        cost = 40 * days - 20
        return cost
    else:
        return "please enter greater than 3 and less than 7 value"


def trip_cost(days, nights, city):
    total_amount = rental_car_cost(days) + hotel_cost(nights) + plane_ride_cost(city)
    return total_amount


def main():
    output = trip_cost(42, 3, "Pittsburgh")
    print(output)


if __name__ == '__main__':
    main()
