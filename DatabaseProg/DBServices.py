class CarData:
    def __init__(self):
        self.query = None
        self.car_brand = "Toyota"
        self.car_model = "Rav4"
        self.color = "Red"
        self.fuel_type = "Gas"
        self.year = 2015

    def car_construct(self, car_brand, car_model, color, fuel_type, year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.color = color
        self.fuel_type = fuel_type
        self.year = year

    def car_insert(self):
        self.query = ("INSERT INTO CARS VALUES"
                      "(%s,%s,%s,%s,%s)")
        return self.query

    def car_make_new_table(self):
        self.query = ("CREATE TABLE IF NOT EXISTS CARS ("
                      "car_brand VARCHAR(30),"
                      "car_model VARCHAR(30),"
                      "color VARCHAR(15),"
                      "fuel_type VARCHAR(30),"
                      "year INT"
                      ")")
        return self.query

    def car_select(self):
        self.query = (f"SELECT * "
                      f"FROM CARS ")

        return self.query
