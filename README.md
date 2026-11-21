# Login Attempt Control System

## Project Description
A Python-based cybersecurity project that
prevents brute-force login attacks using
failed login counters and account lockout.

## Objectives
- Track failed login attempts.
- Monitor usernames and IP addresses.
- Lock accounts after 5 consecutive failures.
- Apply a 15-minute lockout.
- Record security events in audit.log.

## Technologies Used
- Python
- Visual Studio Code
- CSV Dataset

## Project Files
- main.py
- login_control.py
- test_security.py
- login_events.csv
- audit.log

## How to Run

Run the main program:

python main.py

Run security tests:

python test_security.py

## Security Features
1. Failed login detection
2. Account lockout
3. IP-based rate limiting
4. Security audit logging

## Testing
Tested with simulated failed login attempts.
The system successfully locked an account
after five consecutive failures.

## Note
This is an educational demonstration.
Login counters and lockout states are stored
in memory and reset when the program exits.
