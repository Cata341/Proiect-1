import pandas as pd
import sys
from datetime import timedelta


class UberStats:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self._read_data()

    def _read_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            self.data['date'] = pd.to_datetime(self.data['date'])
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except pd.errors.EmptyDataError:
            print("No data found in the file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_stats(self):
        if self.data is None:
            return

        try:
            total_spent = self.data['price'].sum()
            total_rides = len(self.data)
            total_completed_rides = len(self.data[self.data['status'] == 'COMPLETED'])
            total_canceled_rides = len(self.data[self.data['status'] == 'CANCELED'])
            total_distance = self.data['distance'].sum()

            total_rides_per_year = self.data['date'].dt.year.value_counts().to_dict()
            total_rides_per_city = self.data['city'].value_counts().to_dict()
            total_rides_per_month = self.data['date'].dt.month.value_counts().to_dict()
            total_rides_per_product = self.data['product'].value_counts().to_dict()

            total_duration_seconds = self.data['duration_seconds'].sum()
            total_duration = timedelta(seconds=int(total_duration_seconds))
            shortest_ride = self.data['duration_seconds'].min() / 60
            longest_ride = self.data['duration_seconds'].max() / 60

            print(f"Total bani cheltuiti: {total_spent} USD")
            print(f"Total curse: {total_rides}")
            print(f"  COMPLETED: {total_completed_rides}")
            print(f"  CANCELED: {total_canceled_rides}")
            print(f"Total curse per an: {total_rides_per_year}")
            print(f"Total curse per oras: {total_rides_per_city}")
            print(f"Total curse per luna: {total_rides_per_month}")
            print(f"Distanta totala (in km): {total_distance} km")
            print(f"Curse per produs: {total_rides_per_product}")
            print(f"  UberX: {total_rides_per_product.get('UberX', 0)}")
            print(f"  Comfort: {total_rides_per_product.get('Comfort', 0)}")
            print(f"  Black: {total_rides_per_product.get('Black', 0)}")
            print(f"Perioada totala petrecuta in curse:")
            print(f"  Secunde: {total_duration_seconds} secunde")
            print(f"  Minute: {total_duration_seconds / 60} minute")
            print(f"  Ore: {total_duration_seconds / 3600} ore")
            print(f"  Zile: {total_duration.days} zile")
            print(f"Cea mai scurta cursa (in minute): {shortest_ride} minute")
            print(f"Cea mai lunga cursa (in minute): {longest_ride} minute")
        except Exception as e:
            print(f"An error occurred while calculating stats: {e}")

def main():
    if len(sys.argv) < 2:
        print("Please provide the path to the CSV file.")
        return

    file_path = sys.argv[1]
    uber_stats = UberStats(file_path)
    uber_stats.calculate_stats()

if __name__ == "__main__":
    main()

x=pd.read_csv("C:/Users/preda/Desktop/trips_data.csv")
print(x)
