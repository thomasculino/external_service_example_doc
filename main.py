import time
from baselayer.log import make_log

log = make_log("external_service_example_doc")

def main():    
    start_time = time.time()
    while True:
      elapsed_time = time.time() - start_time
      log(f"Running external_service_example_doc for {elapsed_time} seconds")
      time.sleep(2)

if __name__ == "__main__":
    main()