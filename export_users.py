import os
import csv
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

PRIVY_API_KEY = os.getenv("PRIVY_API_KEY")
PRIVY_APP_ID = os.getenv("PRIVY_APP_ID")
if not PRIVY_API_KEY:
    raise RuntimeError("Please set PRIVY_API_KEY in .env")
if not PRIVY_APP_ID:
    raise RuntimeError("Please set PRIVY_APP_ID in .env")

headers = {
    "privy-app-id": PRIVY_APP_ID,
    "Content-Type": "application/json"
}

BASE_URL = "https://api.privy.io/v1/users"
LIMIT = 100  # Number of users to fetch per request (check documentation for maximum limit)

def fetch_all_users():
    users = []
    params = {"limit": LIMIT}
    
    while True:
        print(f"Fetching users... (current count: {len(users)})")
        resp = requests.get(BASE_URL, headers=headers, auth=(PRIVY_API_KEY, PRIVY_APP_ID), params=params)
        resp.raise_for_status()
        data = resp.json()
        
        # Get user data from response
        page_users = data.get("data", [])
        if not page_users:
            break
            
        users.extend(page_users)
        print(f"Fetched {len(page_users)} users")
        
        # Set cursor for next page
        next_cursor = data.get("next_cursor")
        if not next_cursor:
            print("No more pages available")
            break
        params["cursor"] = next_cursor
        print(f"Moving to next page with cursor: {next_cursor}")
        
    print(f"Total users fetched: {len(users)}")
    return users

def save_to_csv(users, filename="users.csv"):
    if not users:
        print("No users found.")
        return

    # CSV headers are automatically generated from the keys of the first user dictionary
    fieldnames = list(users[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)
    print(f"Saved {len(users)} users into {filename}")

if __name__ == "__main__":
    all_users = fetch_all_users()
    save_to_csv(all_users)