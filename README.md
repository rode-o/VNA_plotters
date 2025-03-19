VNA Plotters
This repository contains scripts and data for analyzing and visualizing frequency response measurements from a Vector Network Analyzer (VNA). Two primary types of files are included:

.S2P Files (Keysight format): These are S-Parameter data files typically used with Keysight equipment.
.CSV Files (General multi-chemical data): These are frequency vs. S21 measurements from a custom setup or different instrumentation.
Repository Structure
plaintext
Copy code
VNA_plotters/
├── keysight_data/
│   ├── Patch_Antenna.S2P
│   ├── Patch_Antenna_with_PDMS.S2P
│   ├── WITH_PDMS_0.01gmL.S2P
│   ├── WITH_PDMS_0.02gmL.S2P
│   └── ... (more .S2P files)
│
├── multi_chem_data/
│   ├── Empty_Sensing_Chamber.csv
│   ├── IPA_91%.csv
│   ├── Saline_50%.csv
│   └── Water.csv
│
├── plots/
│   ├── combined_plot_<timestamp>.svg
│   └── keysight_combined_plot_<timestamp>.svg
│
├── run/
│   ├── multi_chem_plotter.py
│   └── process_keysight_plotter.py
│
└── README.md
keysight_data/
Contains .S2P files exported from Keysight VNA measurements. These files typically include frequency data in Hz along with real/imag components of S-parameters.

multi_chem_data/
Contains .CSV files with frequency (in GHz or another unit) and S21 (dB) data for various chemical or sensor conditions.

plots/
Destination folder for all generated plots. Each Python script in the run folder saves its SVG output here with a timestamped filename.

run/
Holds the Python scripts you will run:

multi_chem_plotter.py: Reads all .csv files from multi_chem_data and plots their frequency vs. S21(dB), saving a combined SVG in the plots folder.
process_keysight_plotter.py: Reads all .S2P files from keysight_data and plots their frequency vs. S21(dB), also saving a combined SVG in the plots folder.
Getting Started
Clone this repository:

bash
Copy code
git clone https://github.com/rode-o/VNA_plotters.git
cd VNA_plotters
Install Dependencies (if needed):

Python 3.x
pandas, matplotlib, etc. (Install via pip install pandas matplotlib.)
Run a Script:

Plot Multi-Chemical CSV Data:

bash
Copy code
python run/multi_chem_plotter.py
By default, it looks in multi_chem_data for .csv files and outputs an SVG in plots.

Plot Keysight .S2P Data:

bash
Copy code
python run/process_keysight_plotter.py
By default, it looks in keysight_data for .s2p files and outputs an SVG in plots.

View Output:

Look in the plots folder for SVG files named something like combined_plot_<timestamp>.svg. You can open them in any browser or vector graphics editor.
Contributing
If you want to improve or extend the scripts:

Fork or clone the repository.
Create a new branch for your feature/fix:
bash
Copy code
git checkout -b feature/awesome-improvement
Make changes, then commit and push:
bash
Copy code
git commit -m "Describe your changes"
git push -u origin feature/awesome-improvement
Open a pull request on GitHub.
License
This repository is open-source. See LICENSE (if you have one) for details. If no license file is provided, treat it as all rights reserved until clarified.

Enjoy exploring and visualizing your VNA data!