from faker import Faker

class DataGenerator:
    """Фабрика для генерации пользовательских данных"""
    fake = Faker()


    @classmethod
    def generate_random_email(cls) -> str:
        return cls.fake.email()

    @classmethod
    def generate_random_password(cls) -> str:
        return cls.fake.password(length=12)

    @classmethod
    def generate_random_username(cls) -> str:
        return cls.fake.user_name()