from datetime import datetime, timedelta

MAX_ATTEMPTS = 5
MAX_IP_ATTEMPTS = 10
LOCKOUT_MINUTES = 15

AUDIT_FILE = "audit.log"


class LoginAttemptControl:

    def __init__(self):
        self.failed_attempts = {}
        self.ip_attempts = {}
        self.locked_accounts = {}

    def write_log(self, message):
        with open(AUDIT_FILE, "a", encoding="utf-8") as file:
            file.write(
                f"{datetime.now()} - {message}\n"
            )

    def check_login(self, username, ip_address, success):

        current_time = datetime.now()

        # Check account lockout
        if username in self.locked_accounts:

            if current_time < self.locked_accounts[username]:
                print("Account is locked!")
                return False

            del self.locked_accounts[username]
            self.write_log(
                f"Lockout expired: {username}"
            )

        key = (username, ip_address)

        # Successful login resets consecutive failures
        if success:

            self.failed_attempts.pop(key, None)

            self.ip_attempts[ip_address] = 0

            print("Login successful!")
            return True

        # Count failed login attempts
        self.failed_attempts[key] = (
            self.failed_attempts.get(key, 0) + 1
        )

        self.ip_attempts[ip_address] = (
            self.ip_attempts.get(ip_address, 0) + 1
        )

        attempts = self.failed_attempts[key]
        ip_count = self.ip_attempts[ip_address]

        print("Login failed!")
        print("Username/IP failures:", attempts)
        print("IP failures:", ip_count)

        # IP rate limiting
        if ip_count >= MAX_IP_ATTEMPTS:

            message = f"IP RATE LIMIT: {ip_address}"
            print(message)
            self.write_log(message)

        # Account lockout
        if attempts >= MAX_ATTEMPTS:

            lock_until = current_time + timedelta(
                minutes=LOCKOUT_MINUTES
            )

            self.locked_accounts[username] = lock_until

            message = (
                f"ACCOUNT LOCKED: {username}, "
                f"IP: {ip_address}, "
                f"Until: {lock_until}"
            )

            print(message)
            self.write_log(message)

            return False

        return False