import numpy as np
from scipy.io.wavfile import write
import os
from tqdm import tqdm

# 定义新目录
new_directory = "F:/project/zhouyu"
os.chdir(new_directory)

# 读取信号文件
with open("F:/project/zhouyu/data/result/solar_sys/max_scale/signal/signal.txt", 'r') as file:
    signal = file.read().strip()  # 读取并去除任何可能的空白字符

# 参数设置
sample_rate = 44100  # 采样率，单位为 Hz
bit_rate = 367  # 每秒播放的比特数
duration_per_bit = 1.0 / bit_rate  # 每个比特的持续时间，单位为秒
samples_per_bit = int(sample_rate * duration_per_bit)  # 每个比特对应的采样点数

# 频率设置：低频表示0，高频表示1
freq_0 = 440  # 0 对应的频率，单位为 Hz
freq_1 = 880  # 1 对应的频率，单位为 Hz

# 分割信号并生成音频
total_bits = len(signal)

# 获取用户输入以确定要处理的信号段
task_number = int(input("请输入任务号（1至10）: ")) - 1  # 任务号从1开始，但数组索引从0开始

# 计算每个任务的信号片段
signal_segments = [signal[i * total_bits // 10:(i + 1) * total_bits // 10] for i in range(10)]
signal_to_process = signal_segments[task_number]

# 生成音频信号
audio_signal = np.array([])
for i, bit in enumerate(tqdm(signal_to_process, desc=f"Generating audio signal for task {task_number + 1}", total=len(signal_to_process))):
    if bit == '0':
        t = np.linspace(0, duration_per_bit, samples_per_bit, endpoint=False)
        wave = np.sin(2 * np.pi * freq_0 * t)
    else:
        t = np.linspace(0, duration_per_bit, samples_per_bit, endpoint=False)
        wave = np.sin(2 * np.pi * freq_1 * t)
    audio_signal = np.concatenate((audio_signal, wave))

# 归一化到[-1, 1]
audio_signal = audio_signal / np.max(np.abs(audio_signal))

# 保存为WAV文件
output_path = "F:/project/zhouyu/data/result/solar_sys/max_scale/audio/signal_audio_{task_number + 1}.wav"
write(output_path, sample_rate, audio_signal.astype(np.float32))

print(f"Audio file generated as '{output_path}'")
