```markdown
# Roblox Username Checker

A Python script that generates random usernames and checks their availability on Roblox.

## Features

- Generates random usernames with configurable length
- Checks username availability through Roblox's API
- Categorizes results (available, taken, or censored)
- Logs all activities to a file
- Handles API errors with retry logic
- Color-coded console output
- Saves available usernames to `valid.txt`

## Requirements

- Python 3.x
- Required Python packages (install with `pip install -r requirements.txt`):
  ```
  requests
  colorama
  ```

## Configuration

Edit the `CONFIG` dictionary in the script to change settings:

```python
CONFIG = {
    "USERNAME_LENGTH": 5,      # Length of generated usernames
    "DELAY": 0.5,             # Delay between checks (in seconds)
    "MAX_RETRIES": 3,         # Maximum retries on connection failure
    "RETRY_DELAY": 5,         # Delay between retries (in seconds)
    "API_TIMEOUT": 10         # API request timeout (in seconds)
}
```

## Usage

1. Run the script:
   ```
   python username_checker.py
   ```

2. The script will:
   - Generate random usernames
   - Check each one against Roblox's API
   - Display color-coded results in the console
   - Save available usernames to `valid.txt`

3. To stop the script, press `Ctrl+C`

## Output Files

- `valid.txt`: Contains all available usernames found
- `username_checker.log`: Contains detailed logs of all operations

## Status Codes

The script recognizes these Roblox API response codes:
- `0`: Username is available (green)
- `1`: Username is already taken (gray)
- `2`: Username is censored/invalid (red)
- Other codes: Unknown status (yellow)

## Error Handling

The script includes:
- Automatic retries on connection failures
- Error logging with tracebacks
- Graceful handling of keyboard interrupts
- Recovery from unexpected errors

## Notes

- Roblox may rate limit or block excessive requests
- The script includes delays to be more API-friendly
- For legal use only - check Roblox's terms of service
```

This README provides clear instructions on how to set up and use the script, explains its features, and includes important notes about usage. You can add this to your project repository or modify it as needed.
