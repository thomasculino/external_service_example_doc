from time import time

from baselayer.app.env import load_env
from baselayer.log import make_log

env, cfg = load_env()
log = make_log("example_external_service")

params = cfg.get("services.external.example_external_service.params", {})

def main():    
    while True:
      log.info(f"Running example_external_service for {time()} seconds")
      time.sleep(5)

if __name__ == "__main__":
    main()