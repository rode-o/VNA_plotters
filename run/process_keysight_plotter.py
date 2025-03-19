import os
import math
import matplotlib.pyplot as plt
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def parse_keysight_s2p_file(filepath):
    freq_list = []
    s21_dB_list = []

    with open(filepath, "r") as f:
        header_found = False
        for line in f:
            line = line.strip()
            if not line or line.startswith("!"):
                continue

            if line.startswith("#"):
                header_found = True
                continue

            if header_found:
                parts = line.split()
                if len(parts) < 3:
                    continue

                freq = float(parts[0])
                real_s21 = float(parts[1])
                imag_s21 = float(parts[2])

                mag_s21 = math.sqrt(real_s21**2 + imag_s21**2)
                s21_dB = 20 * math.log10(mag_s21) if mag_s21 > 0 else -999.0

                freq_list.append(freq)
                s21_dB_list.append(s21_dB)

    return freq_list, s21_dB_list


def plot_all_keysight_s2p(data_folder="../keysight_data", output_folder="../plots"):
    if not os.path.isdir(data_folder):
        logging.error(f"The directory '{data_folder}' does not exist.")
        return

    s2p_files = [f for f in os.listdir(data_folder) if f.lower().endswith(".s2p")]

    if not s2p_files:
        logging.warning(f"No .S2P files found in '{data_folder}'.")
        return

    plt.figure(figsize=(10, 6))

    for s2p_file in s2p_files:
        filepath = os.path.join(data_folder, s2p_file)
        freq, s21_dB = parse_keysight_s2p_file(filepath)

        freq_ghz = [f / 1e9 for f in freq]

        label = os.path.splitext(s2p_file)[0].replace('_', ' ')
        plt.plot(freq_ghz, s21_dB, label=label)

    plt.title("Keysight Data: S21 Frequency Response")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("S21 (dB)")
    plt.legend(loc='best', fontsize='small')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_folder, f"keysight_combined_plot_{timestamp}.svg")

    plt.savefig(output_filename, format="svg")
    logging.info(f"Plot saved as '{output_filename}'.")

    plt.show()


if __name__ == "__main__":
    plot_all_keysight_s2p()