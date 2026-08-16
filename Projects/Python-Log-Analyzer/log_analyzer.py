import csv
import json

# Dictionaries
failed_users = {}
failed_ips = {}

# Threshold
threshold = 3

# Open log file
file = open("login.log", "r")

# Read log file
for line in file:
    if "LOGIN_FAILED" in line:
        parts = line.split()

        # Extract user
        user = parts[3]
        user = user.split("=")[1]

        # Count failed users
        if user in failed_users:
            failed_users[user] += 1
        else:
            failed_users[user] = 1

        # Extract IP
        ip = parts[4]
        ip = ip.split("=")[1]

        # Count failed IPs
        if ip in failed_ips:
            failed_ips[ip] += 1
        else:
            failed_ips[ip] = 1

file.close()


# Display user failed logins
print("User Failed Logins:")

for user, count in failed_users.items():
    print(user, count)


# Display IP failed logins
print("\nIP Failed Logins:")

for ip, count in failed_ips.items():
    print(ip, count)


# Detect suspicious IPs
print("\nSuspicious IPs:")

for ip, count in failed_ips.items():
    if count >= threshold:
        print(ip, count)


# Create CSV report
file = open("failed_ips.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["IP", "Failed_Attempts"])

for ip, count in failed_ips.items():
    writer.writerow([ip, count])

file.close()


# Create JSON report
file = open("failed_ips.json", "w")

json.dump(failed_ips, file, indent=4)

file.close()


# Read and verify CSV report
file = open("failed_ips.csv", "r")

reader = csv.reader(file)

print("\nCSV Report:")

for row in reader:
    print(row)

file.close()


# Read and verify JSON report
file = open("failed_ips.json", "r")

data = json.load(file)

print("\nJSON Report:")

print(data)

file.close()
