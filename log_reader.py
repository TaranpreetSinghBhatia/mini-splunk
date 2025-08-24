#log_reader.py
#First version of our mini-splunk project

def read_log(file_path):
    """Reads and prints log file line by line"""
    try:
        with open(file_path, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Log file {file_path} not found.")

if __name__ == "__main__":
    #For now, test with a sample log file
    read_log("sample.log")