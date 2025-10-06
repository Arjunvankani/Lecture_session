import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
fake = Faker()

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Parameters
num_rows = 500
departments = ['Cardiology', 'Pediatrics', 'Orthopedics', 'Oncology', 'Neurology']
doctors = ['Dr. Smith', 'Dr. Lee', 'Dr. White', 'Dr. Adams', 'Dr. Brown']
transaction_types = ['Donation', 'Appointment', 'Prescription', 'Lab Test', 'Billing']
payment_modes = ['Cash', 'Credit Card', 'Online', 'Cheque']
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# Generate data
data = []
for i in range(1, num_rows+1):
    record_id = f"R{i:03d}"
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    patient_name = fake.name()
    
    # Introduce missing values randomly
    department = random.choice(departments + [None]*5)  # ~10% missing
    doctor_name = random.choice(doctors)
    transaction_type = random.choice(transaction_types)
    amount = round(random.uniform(100, 10000), 2)
    if random.random() < 0.1:  # ~10% missing
        amount = None
    payment_mode = random.choice(payment_modes + [None]*5)  # ~10% missing
    notes = random.choice([fake.sentence(), None])  # ~50% missing
    
    data.append([record_id, date, patient_name, department, doctor_name,
                 transaction_type, amount, payment_mode, notes])

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Record_ID','Date','Patient_Name','Department','Doctor_Name',
                                 'Transaction_Type','Amount','Payment_Mode','Notes'])

# Introduce some duplicate rows (~5%)
duplicates = df.sample(frac=0.05, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv("synthetic_medical_data.csv", index=False)

print("Synthetic dataset created: synthetic_medical_data.csv")
print(df.head(10))
