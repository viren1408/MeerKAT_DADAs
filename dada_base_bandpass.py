import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import argparse

def header_info(header):
    header_dict = {}
    for line in header.split('\n'):
        if line and not line.startswith('#') and ' ' in line:
            key, value = line.split(None, 1)
            header_dict[key] = value.strip()

    return {
        'nbit': int(header_dict['NBIT']),
        'ndim': int(header_dict['NDIM']),
        'npol': int(header_dict['NPOL']),
        'nchan': int(header_dict['NCHAN']),
        'nant': int(header_dict['NANT']),
        'order': header_dict['ORDER'],
        'inner_t': int(header_dict['INNER_T']),
        'hdr_size': int(header_dict['HDR_SIZE']),
        'chan_idx': int(header_dict['CHAN0_IDX']),
        'Lowest_freq (MHz)': (int(header_dict['CHAN0_IDX'])*0.208984375 + 856),
    }

def process_dada_file(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(4096).decode('ascii')

    header_param = header_info(header)

    with open(file_path, 'rb') as f:
        f.seek(header_param['hdr_size'])
        raw_data = np.fromfile(f, dtype=np.int8)

    if header_param['order'] == 'TAFTP':
        data = np.asarray(np.reshape(raw_data, (-1, header_param['nant'], header_param['nchan'], header_param['inner_t'], header_param['npol'], header_param['ndim'])), dtype='float32').view('complex64').squeeze()

    return header_param, data

def main(file_name, polarization, antenna1, antenna2):
    header_param, data = process_dada_file(file_name)

    combined_data = data.transpose(0, 3, 1, 2, 4).reshape(-1, data.shape[1], data.shape[2], data.shape[4])

    num_channels = combined_data.shape[2]  

    plt.figure(figsize=(14, 6))

    data1 = combined_data[:, antenna1, :, :]
    data2 = combined_data[:, antenna2, :, :]

    for channel in range(num_channels):
        data_channel_antenna1 = data1[:, channel, :]
        data_channel_antenna2 = data2[:, channel, :]

        num_samples = data_channel_antenna1.shape[0]
        num_chunks = num_samples // 1024

        data_channel_antenna1 = data_channel_antenna1[:num_chunks *1024]
        data_channel_antenna2 = data_channel_antenna2[:num_chunks *1024]

        data_chunks_antenna1 = data_channel_antenna1.reshape(num_chunks,1024, data_channel_antenna1.shape[1])
        data_chunks_antenna2 = data_channel_antenna2.reshape(num_chunks,1024, data_channel_antenna2.shape[1])

        fft_chunks_antenna1 = np.fft.fftshift(np.fft.fft(data_chunks_antenna1, axis=1))
        fft_chunks_antenna2 = np.fft.fftshift(np.fft.fft(data_chunks_antenna2, axis=1))

        cross_power_spectrum = np.abs(fft_chunks_antenna1 * np.conj(fft_chunks_antenna2)) ** 2

        average_cross_power_spectrum_chunks = np.mean(cross_power_spectrum, axis=0)

        bandpass = average_cross_power_spectrum_chunks[:, polarization]

        plt.plot(np.arange(1024)+ 1024*channel, bandpass, color='black')

    plt.xlabel('Frequency Index (across all channels)')
    plt.ylabel('Cross-Power Spectrum (arbitrary units)')
    plt.title(f'Combined Bandpass Across All Channels for Baseline {antenna1}-{antenna2} (Polarization {polarization})')
    plt.grid(True)

    plt.xticks(np.arange(0, 1024*num_channels,1024), labels=[f'Ch {i}' for i in range(num_channels)], rotation=90)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot the bandpass for a given baseline and polarization")
    
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the input DADA file')
    
    parser.add_argument('-p', '--polarization', type=int, choices=[0, 1], required=True, help='Polarization index (0 or 1)')
    
    parser.add_argument('-ants', '--antennas', nargs=2, type=int, required=True, help='Two antenna indices for baseline')
    
    args = parser.parse_args()
    
    main(file_name=args.file, polarization=args.polarization, antenna1=args.antennas[0], antenna2=args.antennas[1])
