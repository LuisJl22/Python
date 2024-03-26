class CatsData:
    def __init__(self):
        self.query = None
        self.cat_id = '1'
        self.owner_id = '1'
        self.name = "Lucille"
        self.breed = 'bengal'
        self.age = "4"

    def cats_construct(self, cat_id, owner_id, name, breed, age):
        self.cat_id = cat_id
        self.owner_id = owner_id
        self.name = name
        self.breed = breed
        self.age = age

    def cats_insert(self):
        self.query = ("INSERT INTO CATS VALUES"
                      "(%s,%s,%s,%s,%s)")
        # self.query = (f"INSERT INTO CATS "
        #               f"VALUES('{self.cat_id}',"
        #               f" '{self.owner_id}',"
        #               f" '{self.name}',"
        #               f" '{self.breed}', "
        #               f"'{self.age}')"
        #               )
        return self.query

    def cats_select(self):
        self.query = (f"SELECT * "
                      f"FROM CATS ")

        return self.query
