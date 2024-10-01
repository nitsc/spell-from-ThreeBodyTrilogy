import numpy as np
from scipy.io.wavfile import read
from scipy.fft import fft

def demodulate(audio_file, sample_rate=44100, freq_0=440, freq_1=880, samples_per_bit=int(44100 * 1 / 367)):
    """
    反编译音频信号，恢复原始文本信号

    Args:
        audio_file: 音频文件路径
        sample_rate: 采样率
        freq_0: 0 对应的频率
        freq_1: 1 对应的频率
        samples_per_bit: 每个比特对应的采样点数

    Returns:
        str: 恢复的文本信号
    """

    # 读取音频文件
    fs, data = read(audio_file)

    # 分段处理
    num_bits = len(data) // samples_per_bit
    recovered_signal = ""
    for i in range(num_bits):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        segment = data[start:end]

        # 频谱分析
        fft_result = fft(segment)
        freqs = np.fft.fftfreq(len(segment), 1/fs)

        # 找到主频
        max_index = np.argmax(np.abs(fft_result))
        max_freq = freqs[max_index]

        # 比较频率，确定比特值
        if np.abs(max_freq - freq_0) < np.abs(max_freq - freq_1):
            recovered_signal += '0'
        else:
            recovered_signal += '1'

    return recovered_signal

# 示例用法
audio_file = "F:\project\zhouyu\data\\result\solar_sys\smaller_scale\\audio\signal_audio.wav"
recovered_signal = demodulate(audio_file)
print(recovered_signal)
output_path = "F:/recovered_signal.txt"
with open(output_path, 'w') as f:
    f.write(recovered_signal)