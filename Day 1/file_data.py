import pandas as pd
import random
from datetime import datetime, timedelta

# Parameters
num_records = 50
departments = ["Cardiology", "Oncology", "Neurology", "Pediatrics", "Orthopedics"]
payment_modes = ["Cash", "Credit Card", "Online Transfer", "Cheque"]
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate random dataset
data = []
for i in range(1, num_records + 1):
    donor_id = f"D{i:03d}"
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    donation_amount = round(random.uniform(500, 10000), 2)
    department = random.choice(departments)
    payment_mode = random.choice(payment_modes)
    data.append([donor_id, date.strftime("%d-%m-%Y"), donation_amount, department, payment_mode])

# Create DataFrame
df = pd.DataFrame(data, columns=["Donor_ID", "Date", "Donation_Amount", "Department", "Payment_Mode"])

# Save to CSV
file_path = "hospital_donations_raw.csv"
df.to_csv(file_path, index=False)
print()
