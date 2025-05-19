from backend.models import create_inventory_table, insert_inventory

# Ensure the table exists first
create_inventory_table()

sample_data = [
    ("Resistor Pack", 1200, 300, "ElectroMart", "2025-05-01"),
    ("Capacitor 220uF", 80, 100, "ElectroMart", "2025-05-10"),
    ("MCU STM32G0", 50, 100, "ST Distributor", "2025-05-11"),
    ("LED Red", 500, 200, "BrightLEDs Inc.", "2025-05-02"),
    ("L293D Motor Driver", 25, 40, "Texas Motors", "2025-05-04"),
    ("ESP32 Module", 10, 50, "Espressif Partner", "2025-05-08"),
    ("TMS320F28379D", 5, 20, "TI Vendor", "2025-05-12")
]

for item in sample_data:
    insert_inventory(*item)

print("Database seeded successfully 🚀")
