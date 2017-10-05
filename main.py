from src.data_fetcher import DataFetcher
from src import serializer


def main():
    fetcher = DataFetcher()
    prs = fetcher.get_pull_requests()
    serializer.to_json(prs)


if __name__ == '__main__':
    main()
