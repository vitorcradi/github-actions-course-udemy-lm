from os import getenv
import requests
import time

def write_to_output(file_path, key, value):
  with open (file_path, "a") as file:
    print(f'{key}={value}', file=file)
    

def ping_url(url, delay, max_trials):
  trials = 0

  while trials < max_trials:
    try:
      response = requests.get(url)
      if response.status_code == 200:
        print(f"Website {url} is reachable.")
        return True
    except requests.ConnectionError:
      print(f"Website {url} is unreachable. Retrying in {delay} seconds...")
      time.sleep(delay)
      trials += 1
    except requests.exceptions.MissingSchema:
      print(f"Invalid URL format: {url}. Make sure URL has a valid schema (e.g.: http:// or https://)")
      return False
  return False

def run():
  website_url = getenv("INPUT_URL")
  delay = int(getenv("INPUT_DELAY"))
  max_trials = int(getenv("INPUT_MAX_TRIALS"))
  github_output_file_path = getenv("GITHUB_OUTPUT")

  website_reachable = ping_url(website_url, delay, max_trials)

  write_to_output(github_output_file_path, 'url-reachable', website_reachable)

  if not website_reachable:
    raise Exception(f"Website {website_url} is malformed or unreachable.")
  
  print(f"Website {website_url} is reachable.")

if __name__ == "__main__":
  print("ping test")
  run()



# from os import getenv
# import subprocess

# def run():
#   url = getenv("INPUT_URL")
#   delay = getenv("INPUT_DELAY")
#   max_trials = int(getenv("INPUT_MAX_TRIALS"))
#   ping_url(url, delay, max_trials)

# def ping_url(url, delay, max_trials):
#   curl_command = f"curl {url} -is | grep '^HTTP\/' | cut -c 10-12"
#   curl_command1 = "curl -s -o /dev/null -w '%{http_code}' " + url
#   command_result = subprocess.check_call(curl_command, shell=True, text=True)
#   print(curl_command)
#   print(curl_command1)
#   print(command_result)
#   sleep_command = f"sleep {delay}"
#   trials = 1
#   while trials <= max_trials:
#     if subprocess.check_output(curl_command, shell=True, text=True) != 200:
#       subprocess.call(sleep_command)
#       subprocess.check_call(curl_command, shell=True, text=True)
#       trials += 1
#     else:
#       return('True')
#       break
#   if trials > max_trials:
#     return('False')
    

# if __name__ == "__main__":
#   print("ping test")
#   run()


