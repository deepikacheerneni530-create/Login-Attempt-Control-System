import csv
from login_control import LoginAttemptControl

# Create security system
security = LoginAttemptControl()

filename = "login_events.csv"

print("LOGIN ATTEMPT CONTROL SYSTEM")
print("=" * 40)

with open(filename, "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    for row in reader:

        username = row["Username"]
        ip_address = row["SourceIP"]
        result = row["Result"].strip().lower()

        success = result == "success"

        print("\nEvent:", row["EventID"])
        print("Username:", username)
        print("IP Address:", ip_address)
        print("Result:", result)

        security.check_login(
            username,
            ip_address,
            success
        )

print("\nDataset processing completed!")
print("Check audit.log for security events.")