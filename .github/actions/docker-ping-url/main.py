from os import getenv
import subprocess

def run():
  url = getenv(url)
  delay = getenv(delay)
  max_trials = getenv(max_trials)
  ping_url(url, delay, max_trials)

def ping_url(url, delay, max_trials):
  curl_command = "curl ${url}"
  sleep_command = "sleep ${delay}"
  trials = 1
  while trials <= max_trials:
    if subprocess.check_output(curl_command, shell=True, text=True) != 200:
      subprocess.call(sleep_command)
      trials =+ 1
    else:
      return('True')
      break
  if trials > max_trials:
    return('False')
    

if __name__ == "__main__":
  print("ping test")
  run()