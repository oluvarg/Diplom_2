from faker import Faker


class Helper:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data
