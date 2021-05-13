import datetime
import json


class LambdaLogIntegration:
    def __init__(self):
        self.message = ""
        self.log_message = {}
        self.event_timestamp = 0

    def logInfo(self, event_message):
        self.message = event_message
        self.event_timestamp = int(datetime.datetime.now().strftime("%s")) * 1000
        self.log_message.update({"timestamp": self.event_timestamp,
                                 "message": {
                                     "log_level": "INFO",
                                     "event": self.message}
                                 })
        return json.dumps(self.log_message)

    def logError(self, event_message):
        self.message = event_message
        self.event_timestamp = int(datetime.datetime.now().strftime("%s")) * 1000
        self.log_message.update({"timestamp": self.event_timestamp,
                                 "message": {
                                     "log_level": "ERROR",
                                     "event": self.message}
                                 })
        return json.dumps(self.log_message)
