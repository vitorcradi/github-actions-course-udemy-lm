from os import getenv
import subprocess

def run():
  url = getenv("INPUT_URL")
  delay = getenv("INPUT_DELAY")
  max_trials = int(getenv("INPUT_MAX_TRIALS"))
  ping_url(url, delay, max_trials)

def ping_url(url, delay, max_trials):
  curl_command = f"curl {url} -is | grep '^HTTP\/' | cut -c 10-12"
  curl_command1 = "curl -s -o /dev/null -w '%{http_code}' " + url
  command_result = subprocess.check_call(curl_command, shell=True, text=True)
  print(curl_command)
  print(curl_command1)
  print(command_result)
  sleep_command = f"sleep {delay}"
  trials = 1
  while trials <= max_trials:
    if subprocess.check_output(curl_command, shell=True, text=True) != 200:
      subprocess.call(sleep_command)
      subprocess.check_call(curl_command, shell=True, text=True)
      trials += 1
    else:
      return('True')
      break
  if trials > max_trials:
    return('False')
    

if __name__ == "__main__":
  print("ping test")
  run()