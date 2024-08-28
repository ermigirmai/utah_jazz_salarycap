# utah_jazz_salarycap project
Simple python project to analyze salary cap trends in the NBA from 2011-2029.

main.py vs. main_gui.py:
Originally wanted to have a UI to make this analysis easier, so created the main_gui.py file. But for the sake of time just stuck to command line interaction, so to run this use the main.py file.

Essentially what's happening is there's a csv file with all the raw data being run through this pipeline:
EXTRACT --> CLEAN --> TRANSFORM --> VISUALIZE

/data directory holds the raw .csv file and a jazz logo that was used as the icon for the gui.
/plots is the output directory where all the plots get saved to during runtime
/src is the source code running these operations.

Everything else should be self-explanatory.
