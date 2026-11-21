from login_control import LoginAttemptControl

security = LoginAttemptControl()

username = "test_user"
ip_address = "192.168.1.50"

print("SECURITY TEST STARTED")

for attempt in range(1, 6):

    print(f"\nTesting attempt {attempt}")

    security.check_login(
        username,
        ip_address,
        False
    )

print("\nTEST COMPLETED")
