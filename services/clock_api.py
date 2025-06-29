import requests
from datetime import datetime
from pokepython.models.clock_models import TimeData #import class

def get_current_time():
    url = "https://worldtimeapi.org/api/timezone/Etc/UTC"
    
    response = requests.get(url)

    if response.status_code == 200: #code for succesful request
        data = response.json()
        dt_str = data["datetime"]
        dt = datetime.fromisoformat(dt_str)
        timezone = data.get("timezone","UTC")
        hour = dt.hour
        minute = dt.minute
        return TimeData(hour=hour, minute=minute, timezone=timezone)
    else:
        return None

## For testing

##if __name__ == "__main__":
   ## current_time = get_current_time()
    ##if current_time:
    ##    print(f"Current time is {current_time.hour}:{current_time.minute} ({current_time.timezone})")
    ##else:
      ##  print("Failed to get current time")