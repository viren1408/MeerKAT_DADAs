# DADA Diagnostic Tool dada : diagno_dada.py

This repository contains a Python script for processing and analyzing DADA files, commonly used in radio astronomy. The tool provides several functionalities, including printing header information, analyzing power received by each antenna, checking pulse profiles per antenna, and examining the incoherent sum pulse profile. This tool is handy for diagnostics and inspection of raw voltage data from radio telescopes.

## Dependencies

To run this script, you need to have the following dependencies installed:

- Python 3.6+
- NumPy
- Matplotlib
- SciPy


## Usage

To use this script, you can run it from the command line with various options:

```bash
python dada_diagnostic.py -f <DADA_FILE> [OPTIONS]
```

### Command-Line Options:

- `-f`, `--files`: The DADA file(s) to process. (Required)
- `-head`, `--header`: Print header information.
- `-d_ant`, `--antenna_diag`: Plot power spectra received by each antenna.
- `-prof_ant`, `--profile_antenna`: Plot pulse profile received by each antenna.
- `-incoh_pulse`, `--incoherent_beam_pulse`: Plot 0 DM incoherent sum pulse profile.

# Bandpass of Interferometric Data : dada_base_bandpass.py 

This Python tool processes interferometric data stored in DADA files and visualizes the bandpass for a specific baseline (two antennas) and polarization across all frequency channels. The bandpass is derived from the cross-power spectrum and plotted in a single combined plot. This script was made to observe the baseline dependence of RFI for a given dada file. The code to get RFI to baseline dependence is in progress. 

## Features
- Processes DADA file format and extracts relevant data.
- Calculates cross-power spectrum between two selected antennas (baseline).
- Uses FFT (1024-point) to compute power spectrum for each channel.
- Plots the combined bandpass for all frequency channels.
- Allows selection of specific polarization (Co-polarization or Cross-polarization).

### Command-Line Options:

- `-f`, `--files`: The DADA file(s) to process. (Required)
- `-p`, `--polarization {0,1}` : Polarization index (0 or 1)
-`ants`,`--antennas ANTENNA1 ANTENNA2`: Two antenna indices for baseline



