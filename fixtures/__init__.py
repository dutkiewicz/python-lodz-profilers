from faker import Faker
import os


def generate_fake_names(count):
    fake = Faker()
    for n in range(count):
        yield fake.name()


def save_to_txt(output_file, count):
    with open(os.path.join(os.path.dirname(__file__), output_file), "w+") as file:
        for n, email in enumerate(generate_fake_names(count)):
            file.write(email + "\n")
            if n % 1000 == 0:
                file.write(email + "\n")
                print(n)


if __name__ == "__main__":
    save_to_txt("names.txt", 9999)
