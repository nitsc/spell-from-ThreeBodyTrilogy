import numpy as np
from scipy.io.wavfile import write
import os
from tqdm import tqdm

# 读取信号文件
with open("D:\\temp\\incantation-from-ThreeBodyTrilogy-main\\data\\result\\solar-sys\\signal\\signal.txt", 'r') as file:
    signal = file.read().strip()  # 读取并去除任何可能的空白字符

# 参数设置
sample_rate = 44100  # 采样率，单位为 Hz
bit_rate = 367  # 每秒播放的比特数
duration_per_bit = 1.0 / bit_rate  # 每个比特的持续时间，单位为秒
samples_per_bit = int(sample_rate * duration_per_bit)  # 每个比特对应的采样点数

# 频率设置：低频表示0，高频表示1
freq_0 = 440  # 0 对应的频率，单位为 Hz
freq_1 = 880  # 1 对应的频率，单位为 Hz

# 生成音频信号
audio_signal = np.array([])
total_bits = len(signal)
for i, bit in enumerate(tqdm(signal, desc="Generating audio signal", total=total_bits)):
    if bit == '0':
        t = np.linspace(0, duration_per_bit, samples_per_bit, endpoint=False)
        wave = np.sin(2 * np.pi * freq_0 * t)
    else:
        t = np.linspace(0, duration_per_bit, samples_per_bit, endpoint=False)
        wave = np.sin(2 * np.pi * freq_1 * t)
    audio_signal = np.concatenate((audio_signal, wave))

# 归一化到[-1, 1]
audio_signal = audio_signal / np.max(np.abs(audio_signal))

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 保存为WAV文件
output_path = os.path.join(desktop_path, "output.wav")
write(output_path, sample_rate, audio_signal.astype(np.float32))

print(f"Audio file generated as '{output_path}'")
