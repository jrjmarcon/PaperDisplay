from dataclasses import dataclass

@dataclass
class TimeData:
    hour: int
    minute: int
    timezone: str