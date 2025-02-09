class BloodBank:
    def __init__(self):
        self.donors = []  # List of donor records

    def add_donor(self, name, age, blood_type, contact):
        donor = {"Name": name, "Age": age, "Blood Type": blood_type, "Contact": contact}
        self.donors.append(donor)
        print(f"Donor {name} added successfully.")

    def search_donor(self, blood_type):
        print(f"\nSearching for donors with blood type {blood_type}...")
        found = [d for d in self.donors if d["Blood Type"] == blood_type]
        if found:
            for donor in found:
                print(f"{donor['Name']} - {donor['Contact']}")
        else:
            print("No matching donors found.")

    def display_donors(self):
        print("\nList of Donors:")
        for donor in self.donors:
            print(f"{donor['Name']} | Age: {donor['Age']} | Blood Type: {donor['Blood Type']} | Contact: {donor['Contact']}")

# Example usage
bank = BloodBank()
bank.add_donor("Alice", 28, "O+", "123-456-789")
bank.add_donor("Bob", 32, "A-", "987-654-321")
bank.display_donors()
bank.search_donor("O+")
