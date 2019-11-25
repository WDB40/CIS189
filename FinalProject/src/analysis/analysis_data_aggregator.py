from FinalProject.src.analysis.analysis_data_collector import AnalysisDataCollector
from FinalProject.src.model.analysis_record import AnalysisRecord


class AnalysisDataAggregator:
    def __init__(self, analysis_data_collector):
        self.analysis_data_collector = analysis_data_collector
        self.analysis_records = {}
        self.analysis_headers = []
        self.factorOneData = []
        self.factorOneHeader = ""
        self.factorTwoData = []
        self.factorTwoHeader = ""
        self.factorThreeData = []
        self.factorThreeHeader = ""
        self.factorFourData = []
        self.factorFourHeader = ""
        self.factorFiveData = []
        self.factorFiveHeader = ""

    def load_factor_data(self):
        factor_one = self.analysis_data_collector.popitem()
        self.factorOneHeader = factor_one[0]
        self.factorOneData = factor_one[1]

        factor_two = self.analysis_data_collector.popitem()
        self.factorTwoHeader = factor_two[0]
        self.factorTwoData = factor_two[1]

        factor_three = self.analysis_data_collector.popitem()
        self.factorThreeHeader = factor_three[0]
        self.factorThreeData = factor_three[1]

        factor_four = self.analysis_data_collector.popitem()
        self.factorFourHeader = factor_four[0]
        self.factorFourData = factor_four[1]

        factor_five = self.analysis_data_collector.popitem()
        self.factorFiveHeader = factor_five[0]
        self.factorFiveData = factor_five[1]

    def load_analysis_records(self):
        for stock in range(0, len(self.factorOneData)):
            record = AnalysisRecord()
            record.ticker = self.factorOneData[stock][0]
            record.factor_one = self.factorOneData[stock][1]
            record.rank_one = self.factorOneData[stock][2]
            record.factor_two = self.factorTwoData[stock][1]
            record.rank_two = self.factorTwoData[stock][2]
            record.factor_three = self.factorThreeData[stock][1]
            record.rank_three = self.factorThreeData[stock][2]
            record.factor_four = self.factorFourData[stock][1]
            record.rank_four = self.factorFourData[stock][2]
            record.factor_five = self.factorFiveData[stock][1]
            record.rank_five = self.factorFiveData[stock][2]
            record.average_rank = self.get_average(record)
            self.analysis_records[record.ticker] = record

    def get_analysis_data(self):
        self.load_factor_data()
        self.load_analysis_records()
        return self.analysis_records

    def get_headers(self):
        self.analysis_headers.append(self.factorOneHeader)
        self.analysis_headers.append(self.factorTwoHeader)
        self.analysis_headers.append(self.factorThreeHeader)
        self.analysis_headers.append(self.factorFourHeader)
        self.analysis_headers.append(self.factorFiveHeader)

        return self.analysis_headers

    def get_average(self, record):
        rank_one = int(record.rank_one)
        rank_two = int(record.rank_two)
        rank_three = int(record.rank_three)
        rank_four = int(record.rank_four)
        rank_five = int(record.rank_five)

        return (rank_one + rank_two + rank_three + rank_four + rank_five) / 5
