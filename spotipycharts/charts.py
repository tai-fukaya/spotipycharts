import enum
from . import client


class ChartType(enum.Enum):
    TOP200 = 'regional'
    VIRAL = 'viral'


class FrequencyType(enum.Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'


class Frequency():
    _freq_type = FrequencyType.DAILY
    _chart_type = ChartType.TOP200

    def __init__(self, chart_type):
        self._chart_type = chart_type

    def get_duration_list(self, country):
        return client.get_duration_list(self._chart_type.value, country, self._freq_type.value)

    def download_csv(self, country, duration):
        return client.download_csv(self._chart_type.value, country, self._freq_type.value, duration)


class DailyFreq(Frequency):
    _freq_type = FrequencyType.DAILY


class WeeklyFreq(Frequency):
    _freq_type = FrequencyType.WEEKLY


class Chart():
    _chart_type = ChartType.TOP200

    def __init__(self):
        self.daily = DailyFreq(self._chart_type)
        self.weekly = WeeklyFreq(self._chart_type)


class Top200Chart(Chart):
    _chart_type = ChartType.TOP200


class ViralChart(Chart):
    _chart_type = ChartType.VIRAL


class Spotipycharts():
    def __init__(self):
        self.top200 = Top200Chart()
        self.viral = ViralChart()

    def get_country_list(self):
        return client.get_country_list()

    def get_duration_list(self, chart_type=ChartType.TOP200, country='', freq_type=FrequencyType.DAILY):
        return client.get_duration_list(chart_type.value, country, freq_type.value)

    def download_csv(self, chart_type=ChartType.TOP200, country='', freq_type=FrequencyType.DAILY, duration='latest'):
        return client.download_csv(chart_type.value, country, freq_type.value, duration)
