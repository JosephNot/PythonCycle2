# Resistance calculator

# Variables

base_resistance = 0
final_resistance = 0
temperature_range = 0
temperature_affect = 1.0045

def calculate_final_resistance(base_resistance, temperature_affect, temperature_range):
    final_resistance = base_resistance * (temperature_affect * temperature_range)
    print(final_resistance)

def calculate_base_resistance(final_resistance, temperature_affect, temperature_range):
    base_resistance = final_resistance / (temperature_affect * temperature_range)
    print(base_resistance)

def get_user_calculation():
    print("Put in an input but skip if not known")
    try:
        base_resistance = float(input("Base resistance: ") or 0.0)
        final_resistance = float(input("Final resistance: ") or 0.0)
        temperature_affect = float(input("Temperature affect: ") or 0.0)
        temperature_range = float(input("Temperature range: ") or 0.0)

        print()
        user_input = int(input("Calculate final resistance\nCalculate base resistance\nPick a option from 1-2: "))
        if user_input not in [1,2]:
            raise ValueError

    except ValueError:
        print("Input not in range")
        return

    if user_input == 1:
        calculate_final_resistance(base_resistance, temperature_affect, temperature_range)

    elif user_input == 2:
        calculate_base_resistance(final_resistance, temperature_affect, temperature_range)

while True:
    get_user_calculation()
