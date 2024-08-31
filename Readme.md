# DADA Diagnostic Tool

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

### Example Usage:

To print the header and plot the power spectra for a DADA file:

```bash
python dada_diagnostic.py -f example.dada -head -d_ant
```

To check the pulse profile for each antenna:

```bash
python dada_diagnostic.py -f example.dada -prof_ant
```

To plot the incoherent sum pulse profile:

```bash
python dada_diagnostic.py -f example.dada -incoh_pulse
```

