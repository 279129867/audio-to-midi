# audio-to-midi

基于 Spotify 开源的 **Basic Pitch**，把音频（清唱 / 单乐器）转成 MIDI 乐谱，并可进一步分析音符、音域与旋律序列。
纯 CPU 即可运行，无需独立显卡。

> 仅用于个人学习、研究和声与旋律走向；**不得直接照搬他人旋律商用或上架**，注意版权。

## 功能
- `transcribe.py`：音频 → MIDI（`.mid`）
- `analyze_midi.py`：读取 MIDI，输出音符数、时长、音域、音符序列

## 环境要求
- Windows / macOS / Linux
- Python 3.11（开发环境）
- CPU 即可，无需 NVIDIA 显卡

## 安装（建议虚拟环境）

```powershell
# 1. 建虚拟环境
python -m venv .venv
.venv\Scripts\activate

# 2. 先装 CPU 版 torch（避免下载 CUDA 大包）
python -m pip install torch --index-url https://download.pytorch.org/whl/cpu

# 3. 装项目依赖
python -m pip install -r requirements.txt
```

## 使用

### 1) 音频转 MIDI
```powershell
python transcribe.py --audio input/piano_15s.wav --out output
```
参数：
- `--audio`：输入音频（wav / mp3 / m4a / flac）
- `--out`：MIDI 输出目录（默认 `output`）

> 建议用清唱或单一乐器（钢琴/吉他）；混音成品歌建议先分离人声再转，否则音符会糊。

### 2) 分析 MIDI
```powershell
# 打印到屏幕
python analyze_midi.py output/piano_15s.mid

# 写入文本文件
python analyze_midi.py output/piano_15s.mid --out analysis.txt
```

## 项目结构
```
audio-to-midi/
├── transcribe.py          # 音频 -> MIDI
├── analyze_midi.py        # MIDI -> 音符/音域/序列分析
├── requirements.txt
├── input/                 # 放待转写音频
├── output/                # 生成的 MIDI
└── examples/              # 示例 MIDI 与分析结果
```

## 示例结果
`examples/piano_15s.mid` 由一段 15 秒钢琴转写得到，分析见 `examples/piano_15s_analysis.txt`。

## 说明
- Basic Pitch 由 Spotify Audio Intelligence Lab 开源（Apache 协议）。
- 本项目仅做封装与命令行分析，模型版权归原作者。
- MIDI 中的速度为默认估计值，精确节奏需在打谱软件（如 MuseScore）中二次校对。

## 版权与免责
本项目仅供学习个人使用。请勿将转写得到的他人作品旋律直接复制、改编并商用上架，由此产生的版权责任由使用者自行承担。
