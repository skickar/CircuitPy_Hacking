import wifi

try: # Try to import Wi-Fi creds from secrets.py, exit if it doesn't exist
    from secrets import secrets # Import SSID and password from secrets.py folder
except ImportError: # This error means they aren't there
    print("WiFi secrets are kept in secrets.py. To fix this error, add your Wi-Fi SSID and password to secrets.py!")
    raise # Show the error that caused the crash

try: # Connecting to Wi-Fi network from secrets.py file
    print("Connecting to {}s...".format(secrets["ssid"]))
    wifi.radio.connect(secrets["ssid"], secrets["password"])
except:
    print("Error connecting to WiFi")
    raise

print("Connected to {}s!".format(secrets["ssid"])) # Announce we are connected
print("My IP address is", wifi.radio.ipv4_address) # Print the IP address we were given
