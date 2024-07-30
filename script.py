import pandas as pd
import numpy
import argparse
import sys
from datetime import datetime


class UberStats:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):

        data = pd.read_csv(self.file_path)

        def transform_begin_time(df_line):
            return datetime.strptime(df_line['Begin Trip Time'], "%Y-%m-%d %H:%M:%S %z %Z")

        data['Begin Trip Time'] = data.apply(transform_begin_time, axis=1)

        def transform_end_time(df_line):
            return datetime.strptime(df_line['Dropoff Time'], "%Y-%m-%d %H:%M:%S %z %Z")

        def transform_duration(df_line):
            # TODO: remove line with invalid duration
            if df_line['Begin Trip Time'] > df_line['Dropoff Time']:
                return 0

            return (df_line['Dropoff Time'] - df_line['Begin Trip Time']).seconds

        data['Dropoff Time'] = data.apply(transform_end_time, axis=1)
        data['duration_seconds'] = data.apply(transform_duration, axis=1)

        return data

    def total_money_spent(self):
        return self.data['Fare Amount'].sum()

    def total_rides(self):
        total = len(self.data)
        completed = len(self.data[self.data['Trip or Order Status'] == 'COMPLETED'])
        canceled = len(self.data[self.data['Trip or Order Status'] == 'CANCELED'])
        return total, completed, canceled

    def total_rides_per_year(self):
        return self.data.groupby(self.data['Begin Trip Time'].dt.year).size()

    def total_rides_per_city(self):
        return self.data['City'].value_counts()

    def total_rides_per_month(self):
        return self.data.groupby(self.data['Begin Trip Time'].dt.to_period('M')).size()

    def total_distance(self):
        return self.data['Distance (miles)'].sum()

    def rides_per_product(self):
        return self.data['Product Type'].value_counts()

    def total_time_spent(self):
        total_seconds = self.data['duration_seconds'].sum()
        total_minutes = total_seconds / 60
        total_hours = total_minutes / 60
        total_days = total_hours / 24
        return total_seconds, total_minutes, total_hours, total_days

    def shortest_ride(self):
        # Filter trips with 0 seconds
        non_zeros = self.data[self.data['duration_seconds'] != 0]
        return non_zeros['duration_seconds'].min()

    def longest_ride(self):
        return self.data['duration_seconds'].max()

    def generate_statistics(self):
        if self.data is None:
            print("No data to process.")
            return

        print(f"Total Money Spent: {self.total_money_spent()}")
        total, completed, canceled = self.total_rides()
        print(f"Total Rides: {total}")
        print(f"  Completed: {completed}")
        print(f"  Canceled: {canceled}")
        print(f"Total Rides per Year:\n{self.total_rides_per_year()}")
        print(f"Total Rides per City:\n{self.total_rides_per_city()}")
        print(f"Total Rides per Month:\n{self.total_rides_per_month()}")
        print(f"Total Distance (km): {self.total_distance()}")
        print(f"Rides per Product:\n{self.rides_per_product()}")
        total_seconds, total_minutes, total_hours, total_days = self.total_time_spent()
        print(
            f"Total Time Spent in Rides: {total_seconds:.2f} seconds, {total_minutes:.2f} minutes, {total_hours:.2f} hours, {total_days:.2f} days")
        print(f"Shortest Ride (minutes): {self.shortest_ride() / 60:.2f}")
        print(f"Longest Ride (minutes): {self.longest_ride() / 60:.2f}")


def main():
    parser = argparse.ArgumentParser(description='Process Uber rides data.')
    parser.add_argument('file', type=str, nargs='?', help='CSV file containing Uber rides data')
    args = parser.parse_args()

    if not args.file:
        print("Please provide a CSV file.")
        sys.exit(1)

    stats = UberStats(args.file)
    stats.generate_statistics()


if __name__ == '__main__':
    main()
