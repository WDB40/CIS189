from FinalProject.src.analysis.analysis_data_aggregator import AnalysisDataAggregator
import csv
import datetime


class AnalysisFilePrinter:
    def __init__(self, analysis_data_aggregator):
        self.data = analysis_data_aggregator.get_analysis_data()
        self.headers = analysis_data_aggregator.get_headers()
        self.file_name = "default.csv"

    def write_file(self, filename):
        with open(filename, 'w', newline='') as analysis_results:
            writer = csv.writer(analysis_results)
            file_info = ["Name:", filename, "Created On:", datetime.datetime.now()]
            writer.writerow(file_info)
            headers = ["Ticker", "Average Rank", self.headers[0], f"{self.headers[0]} Rank", self.headers[1], f"{self.headers[1]} Rank", self.headers[2], f"{self.headers[2]} Rank", self.headers[3], f"{self.headers[3]} Rank", self.headers[4], f"{self.headers[4]} Rank"]
            writer.writerow(headers)

            for key, record in self.data.items():
                row = [key, record.average_rank, record.factor_one, record.rank_one, record.factor_two, record.rank_two, record.factor_three, record.rank_three, record.factor_four, record.rank_four, record.factor_five, record.rank_five]
                writer.writerow(row)
