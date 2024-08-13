import subprocess
import time

# Function to read URLs from a file and open them in Tor Browser
def open_websites_with_tor(file_path, tor_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            urls = file.readlines()
            # Strip any extra whitespace characters (like newline)
            urls = [url.strip() for url in urls if url.strip()]
            
            # Launch the Tor Browser with all URLs as arguments
            subprocess.Popen([tor_path] + urls)
            print("Opening Tor Browser with the following URLs:")
            for url in urls:
                print(f" - {url}")
                
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to your text file containing URLs
file_path = 'websites.txt'

# Path to the Tor Browser executable
tor_path = r'C:\Users\zsomb\Desktop\Tor Browser\Browser\firefox.exe'

# Call the function to open websites with Tor Browser
open_websites_with_tor(file_path, tor_path)
