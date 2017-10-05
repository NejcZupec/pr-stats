from src.data_fetcher import DataFetcher
from src.stats import StatsAggregator
from src import serializer


def main():
    # fetcher = DataFetcher()
    # prs = fetcher.get_pull_requests()
    # serializer.to_json(prs)
    aggregator = StatsAggregator()
    prs_opened_by_day = aggregator.prs_opened_by_day()
    prs_merged_by_day = aggregator.prs_merged_by_day()


if __name__ == '__main__':
    main()
