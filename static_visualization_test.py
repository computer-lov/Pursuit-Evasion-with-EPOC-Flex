import mne
import matplotlib.pyplot as plt 
from topograph import get_psds, plot_topomap

if __name__ == "__main__":
    for num in range(1,26):
        file = 'trial' + str(num) + '.edf'
        data = mne.io.read_raw_edf(file)
        raw_data = data.get_data()
        ch_data = raw_data[2:16,:]
        pwrs, _ = get_psds(ch_data)

        fig, ax = plt.subplots(figsize=(10,8))
        plot_topomap(pwrs, ax, fig)
        plt.show()
        newFile = 'trialResult' + str(num) + '.png'
        fig.savefig(newFile, bbox_inches='tight')