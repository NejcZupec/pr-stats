from collections import Counter
from datetime import datetime as dt

import json

class StatsAggregator:
    def __init__(self, data_file='github_data.json'):
        self.data_file = data_file

    def prs_opened_by_day(self):
        data = self._load_data()

        def make_date(date_str):
            return dt.strptime(date_str.split(' ')[0], '%Y-%m-%d').date()

        pr_create_dates = (make_date(pr['created_at']) for pr in data.values())
        return Counter(pr_create_dates)

    def prs_merged_by_day(self):
        data = self._load_data()

        def make_date(date_str):
            return dt.strptime(date_str.split(' ')[0], '%Y-%m-%d').date()

        pr_merge_dates = (
            make_date(pr['merged_at'])
            for pr in data.values() if pr['merged_at']
        )
        return Counter(pr_merge_dates)

    def _load_data(self):
        with open(self.data_file, 'r') as f:
            json_data = f.read()
        return json.loads(json_data)
