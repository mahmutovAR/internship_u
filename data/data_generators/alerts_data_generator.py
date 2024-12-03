from data.data_classes import AlertsData
from . import BaseGenerator


class AlertsDataGenerator(BaseGenerator):
    def generate_alert_data(self, first_name: str = None, last_name: str = None):

        yield AlertsData(first_name=self.generate_first_name(first_name),
                         last_name=self.generate_last_name(last_name))
