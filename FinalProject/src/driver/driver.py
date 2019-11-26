from FinalProject.src.database.stock_database import *
from FinalProject.src.file.stock_file_loader import StockFileLoader
from FinalProject.src.analysis.selector import Selector
from FinalProject.src.analysis.analysis_data_collector import AnalysisDataCollector
from FinalProject.src.analysis.analysis_data_aggregator import AnalysisDataAggregator
from FinalProject.src.file.analysis_file_printer import AnalysisFilePrinter
from FinalProject.src.gui.analysis_gui import AnalysisGUI

if __name__ == '__main__':
    database = StockDatabase()
    # database.initialize_database()
    #
    # file_loader = StockFileLoader()
    # file_loader.load_to_database()

    # selector = Selector()
    # selector.price_book = True
    # selector.roa = True
    # selector.pe_ratio = True
    # selector.profit = True
    # selector.five_year_rev = True
    #
    # analysis_data = AnalysisDataCollector(selector)
    # data = analysis_data.get_analysis_data()
    # aggregated = AnalysisDataAggregator(data)
    # file_writer = AnalysisFilePrinter(aggregated)
    # file_writer.write_file("testFile.csv")

    gui = AnalysisGUI()
    gui.mainloop()