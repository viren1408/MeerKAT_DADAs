# DADA Diagnostic Tool

This repository contains a Python script for processing and analyzing DADA files, commonly used in radio astronomy. The tool provides several functionalities, including printing header information, analyzing power received by each antenna, checking pulse profiles per antenna, and examining the incoherent sum pulse profile. This tool is particularly useful for diagnostics and data inspection when dealing with raw voltage data from radio telescopes.

## Dependencies

To run this script, you need to have the following dependencies installed:

- Python 3.6+
- NumPy
- Matplotlib
- SciPy

You can install the required Python packages using pip:

\```bash
pip install numpy matplotlib scipy
\```

## Function Definitions

### `header_info(header)`
- **Description:** Parses the header of the DADA file and extracts relevant information into a dictionary.
- **Parameters:** `header` (str): The header string extracted from the DADA file.
- **Returns:** A dictionary containing key header parameters.

### `print_header(header_param)`
- **Description:** Prints the extracted header information in a readable format.
- **Parameters:** `header_param` (dict): The dictionary containing header information.

### `process_dada_file(file_path)`
- **Description:** Reads and processes a DADA file, extracting both header information and raw data.
- **Parameters:** `file_path` (str): The path to the DADA file.
- **Returns:** A tuple containing header information and processed data.

### `plot_antenna_diag(header_param, data)`
- **Description:** Plots the power spectra received by each antenna as a function of frequency.
- **Parameters:** 
  - `header_param` (dict): The dictionary containing header information.
  - `data` (np.ndarray): The processed data from the DADA file.
- **Output:** Saves a plot of the power spectra for each antenna.

### `plot_profile_antenna(header_param, data)`
- **Description:** Plots the pulse profile received by each antenna.
- **Parameters:** 
  - `header_param` (dict): The dictionary containing header information.
  - `data` (np.ndarray): The processed data from the DADA file.
- **Output:** Saves a plot of the pulse profile for each antenna.

### `plot_incoherent_beam_pulse(header_param, data)`
- **Description:** Plots the 0 DM incoherent sum pulse profile, summing across frequency channels and antennas.
- **Parameters:** 
  - `header_param` (dict): The dictionary containing header information.
  - `data` (np.ndarray): The processed data from the DADA file.
- **Output:** Saves a plot of the incoherent sum pulse profile.

## Usage

To use this script, you can run it from the command line with various options:

\```bash
python dada_diagnostic.py -f <DADA_FILE> [OPTIONS]
\```

### Command-Line Options:

- `-f`, `--files`: The DADA file(s) to process. (Required)
- `-head`, `--header`: Print header information.
- `-d_ant`, `--antenna_diag`: Plot power spectra received by each antenna.
- `-prof_ant`, `--profile_antenna`: Plot pulse profile received by each antenna.
- `-incoh_pulse`, `--incoherent_beam_pulse`: Plot 0 DM incoherent sum pulse profile.

### Example Usage:

To print the header and plot the power spectra for a DADA file:

\```bash
python dada_diagnostic.py -f example.dada -head -d_ant
\```

To check the pulse profile for each antenna:

\```bash
python dada_diagnostic.py -f example.dada -prof_ant
\```

To plot the incoherent sum pulse profile:

\```bash
python dada_diagnostic.py -f example.dada -incoh_pulse
\```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
