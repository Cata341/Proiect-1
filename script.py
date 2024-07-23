import pandas as pd
import argparse
import sys
from datetime import datetime


class UberStats:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            data['Begin Trip Time'] = pd.to_datetime(data['Begin Trip Time'])
            data['Drop off Time'] = pd.to_datetime(data['Drop off Time'])
            data['duration_seconds'] = (data['Drop off Time'] - data['Begin Trip Time']).dt.total_seconds()
            return data
        except Exception as e:
            print(f"Error loading file: {e}")
            return None

    def total_money_spent(self):
        return self.data['cost'].sum()

    def total_rides(self):
        total = len(self.data)
        completed = len(self.data[self.data['status'] == 'COMPLETED'])
        canceled = len(self.data[self.data['status'] == 'CANCELED'])
        return total, completed, canceled

    def total_rides_per_year(self):
        return self.data.groupby(self.data['Begin Trip Time'].dt.year).size()

    def total_rides_per_city(self):
        return self.data['city'].value_counts()

    def total_rides_per_month(self):
        return self.data.groupby(self.data['Begin Trip Time'].dt.to_period('M')).size()

    def total_distance(self):
        return self.data['distance'].sum()

    def rides_per_product(self):
        return self.data['Product Type'].value_counts()

    def total_time_spent(self):
        total_seconds = self.data['duration_seconds'].sum()
        total_minutes = total_seconds / 60
        total_hours = total_minutes / 60
        total_days = total_hours / 24
        return total_seconds, total_minutes, total_hours, total_days

    def shortest_ride(self):
        return self.data['duration_seconds'].min()

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
            f"Total Time Spent in Rides: {total_seconds} seconds, {total_minutes} minutes, {total_hours} hours, {total_days} days")
        print(f"Shortest Ride (minutes): {self.shortest_ride() / 60}")
        print(f"Longest Ride (minutes): {self.longest_ride() / 60}")


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