# This is a test file for NeuralMind Cortex
import os

# 1. Hardcoded Password (Risk)
password = "super_secret_password_123"

# 2. Dangerous Execution (Risk)
user_input = "print('hacked')"
exec(user_input)

# 3. SQL Injection (Risk)
query = "SELECT * FROM users WHERE name = " + user_input
