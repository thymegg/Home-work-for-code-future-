def generate_registration_string(first_name, last_name, middle_name, age):
    registration_string = f"{last_name} {first_name} {middle_name} {age} г.р. зарегистрирован"
    return registration_string

result = generate_registration_string(first_name, last_name, middle_name, age)
print(result)