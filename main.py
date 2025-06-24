import time
from baselayer.log import make_log

log = make_log("example_external_service")

def main():    
    start_time = time.time()
    while True:
      elapsed_time = time.time() - start_time
      log(f"Running example_external_service for {elapsed_time} seconds")
      time.sleep(2)

if __name__ == "__main__":
    main()