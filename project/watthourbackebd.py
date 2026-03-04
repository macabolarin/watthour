class Appliance:
    def __init__(self, name, power_rating, usage_hours):
        self.name = name
        self.power_rating = power_rating # in watts
        self.usage_hours = usage_hours # in hours
    def calculate_energy(self):
        return (self.power_rating / 1000) * self.usage_hours # in kwh
class Appliancecalculator:
    def __init__(self):
        self.appliance = []

    def add_appliance(self, appliance):
        self.appliance.append(appliance)

    def calculate_total_energy(self):
        return sum(appliance.calculate_energy() for appliance in self.appliance)
def main():
    calculator = Appliancecalculator()

    while True:
        print("\nAppliance calculator")
        print("1. Add appliance")
        print("2. Calculate total energy")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter appliance name: ")
            power-rating = float(input("Enter power rating (W): "))
            usage_hours = float(input("Enter usage hours (h): "))
            appliance = Appliance(name, "power_rating", usage_hours)
            calculator.add_appliance(appliance)
            print(f"Appliance '{name}' added successfully!")
        elif choice == "2":
            if not calculator.appliance:
                print("add appliance")
            else:
                total_energy = calculator.calculate_total_energy()
                print("Appliances and their energy consumption:")
                for appliance in calculator.appliances:
                    print(f"_ {appliance.name}: {appliance.calculate_energy():.2f} kwh")
                print(f"Total energy consumption: {total_energy:.2f} kwh")
        elif choice == "3":
            break
        else:
            print("try again")