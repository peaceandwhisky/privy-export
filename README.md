# Privy User Export

A Python script to export all users from Privy API to a CSV file.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/privy-export.git
cd privy-export
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Privy credentials:
```
PRIVY_API_KEY=your_api_key_here
PRIVY_APP_ID=your_app_id_here
```

## Usage

Run the script:
```bash
python export_users.py
```

The script will:
1. Fetch all users from Privy API
2. Save them to `users.csv` in the current directory

## Output

The script generates a CSV file containing all user data with the following information:
- User ID
- Verification timestamps
- Authentication methods
- Wallet addresses
- Other user metadata

## License

MIT 