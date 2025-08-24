import sys

# Step 1: Define which log file to read
LOG_FILE = "sample.log"

def read_logs():
    """Reads all lines from the log file."""
    with open(LOG_FILE, "r") as f:
        return f.readlines()

def search_logs(keyword=None):
    """Search logs for a keyword. If no keyword, show all logs."""
    logs = read_logs()
    if keyword:
        # Only keep logs that contain the keyword
        return [line for line in logs if keyword in line]
    return logs

def main():
    # sys.argv gives command-line arguments (like python log_reader.py ERROR)
    keyword = sys.argv[1] if len(sys.argv) > 1 else None

    results = search_logs(keyword)

    if results:
        print("\n--- Search Results ---")
        for line in results:
            print(line.strip())  # .strip() removes newline at the end
    else:
        print("No logs found for your search.")

if __name__ == "__main__":
    main()
