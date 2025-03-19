import os
import pandas as pd
import matplotlib.pyplot as plt
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def plot_all_csv_files(data_folder="../multi_chem_data", output_folder="../plots"):
    """
    Plots all CSV files in the specified 'data_folder' directory.
    Saves the resulting figure with a timestamped filename to 'output_folder'.
    """
    if not os.path.isdir(data_folder):
        logging.error(f"The directory '{data_folder}' does not exist.")
        return

    csv_files = [
        f for f in os.listdir(data_folder)
        if f.lower().endswith(".csv")
    ]

    if not csv_files:
        logging.warning(f"No CSV files found in '{data_folder}'.")
        return

    plt.figure(figsize=(10, 6))

    for csv_file in csv_files:
        file_path = os.path.join(data_folder, csv_file)

        try:
            df = pd.read_csv(file_path, header=0)

            if df.shape[1] < 2:
                logging.warning(f"File '{csv_file}' does not have at least two columns. Skipping.")
                continue

            x, y = df.iloc[:, 0], df.iloc[:, 1]
            label = os.path.splitext(csv_file)[0].replace('_', ' ')
            plt.plot(x, y, label=label)

        except pd.errors.EmptyDataError:
            logging.warning(f"File '{csv_file}' is empty. Skipping.")
        except Exception as e:
            logging.error(f"Failed to process '{csv_file}': {e}")

    plt.title("Effects of Various Chemicals on Sensor S21 Frequency Response")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("S21 (dB)")
    plt.legend(loc='best', fontsize='small')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_folder, f"combined_plot_{timestamp}.svg")

    plt.savefig(output_filename, format="svg")
    logging.info(f"Plot saved as '{output_filename}'.")

    plt.show()

if __name__ == "__main__":
    plot_all_csv_files()