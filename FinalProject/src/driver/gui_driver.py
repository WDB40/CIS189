"""
Program: gui_driver.py
Author: Wes Brown
Last date modified: 12/08/19

Purpose: Used for starting the GUI for the app
"""


from FinalProject.src.gui.analysis_gui import AnalysisGUI

if __name__ == '__main__':
    gui = AnalysisGUI()
    gui.mainloop()
