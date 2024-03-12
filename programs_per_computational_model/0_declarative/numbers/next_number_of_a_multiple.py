def next_number_of_a_multiple(base_number, multiple):
    number_system_base = 10
    tens = (base_number // number_system_base) * number_system_base
    if base_number % multiple == 0:
        return base_number + multiple
    elif base_number % number_system_base < multiple:
        return tens + multiple
    else:
        return tens + number_system_base


print(next_number_of_a_multiple(67, 5))
print(next_number_of_a_multiple(73, 5))
print(next_number_of_a_multiple(38, 5))
