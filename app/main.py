class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if self.cleaning_capacity(car) > 0:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * self.cleaning_capacity(car)
                     * (self.average_rating / self.distance), 1)

    def wash_single_car(self, car: Car) -> None:
        if self.cleaning_capacity(car) > 0:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        total_rate_before = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_rate_before + rate)
                                    / self.count_of_ratings, 1)

    def cleaning_capacity(self, car: Car) -> int:
        return self.clean_power - car.clean_mark
