# VNA Plotters

This repository contains scripts and data for analyzing and visualizing frequency response measurements from a Vector Network Analyzer (VNA). Specifically, it includes plotting scripts for:

- **Keysight `.S2P` data files** (S-parameters from Keysight VNAs).
- **libreVNA `.CSV` data files** (frequency vs. S21 measurements for various chemicals and conditions).

## Repository Structure

```
VNA_plotters/
├── keysight_data/
│   ├── Patch_Antenna.S2P
│   ├── Patch_Antenna_with_PDMS.S2P
│   ├── WITH_PDMS_0.01gmL.S2P
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
```

### Directory Contents:

- **`keysight_data/`**
  - Contains `.S2P` files from Keysight VNAs, typically used for S21 parameter analysis.

- **`multi_chem_data/`**
  - Holds `.CSV` files with frequency and corresponding S21 (in dB) data from chemical sensing experiments.

- **`plots/`**
  - Generated plots (SVG files) are saved here with timestamped filenames for clear versioning and record-keeping.

- **`run/`**
  - Contains Python scripts for data processing and visualization:
    - `multi_chem_plotter.py`: Plots CSV data from the `multi_chem_data` folder.
    - `process_keysight_plotter.py`: Plots S2P data from the `keysight_data` folder.

## Getting Started

### Clone the Repository:

```bash
git clone https://github.com/rode-o/VNA_plotters.git
cd VNA_plotters
```

### Install Dependencies:

Ensure you have Python installed (version 3.x recommended). Then install required packages:

```bash
pip install pandas matplotlib
```

### Running Scripts:

- **Plot CSV data:**

```bash
python run/multi_chem_plotter.py
```

- **Plot Keysight S2P data:**

```bash
python run/process_keysight_plotter.py
```

After running, plots will be generated and saved in the `plots/` directory.

## Viewing Results:

Check the generated plots (`.svg` files) in the `plots/` folder. These SVG files can be opened in web browsers or vector graphic viewers for high-quality visualization.