# -*- coding: utf-8 -*-
"""
audio-to-midi: 使用 Spotify Basic Pitch 把音频转成 MIDI 乐谱。
用法:
    python transcribe.py --audio 输入音频.wav --out output
说明:
    - 适合清唱 / 单乐器(钢琴、吉他) ; 混音成品歌建议先分离人声再转。
    - 仅用于个人学习分析, 不得直接照搬旋律商用上架。
"""
import argparse
import os
import sys


def transcribe(audio_path: str, out_dir: str) -> str:
    from basic_pitch.inference import predict
    import pretty_midi

    if not os.path.isfile(audio_path):
        sys.exit(f"[错误] 找不到音频文件: {audio_path}")

    os.makedirs(out_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(audio_path))[0]
    out_mid = os.path.join(out_dir, f"{base}.mid")

    print(f"[1/2] 正在转写: {audio_path}")
    # predict: 音频 -> (模型输出, midi_data(pretty_midi), 音符事件)
    model_output, midi_data, note_events = predict(audio_path)

    print(f"[2/2] 写出MIDI: {out_mid}")
    midi_data.write(out_mid)

    # 打印基本信息供学习
    total_notes = sum(len(inst.notes) for inst in midi_data.instruments)
    duration = midi_data.get_end_time()
    print("-" * 40)
    print(f"音符总数: {total_notes}")
    print(f"时长: {duration:.2f} 秒")
    print(f"轨道数: {len(midi_data.instruments)}")
    print(f"输出: {out_mid}")
    return out_mid


def main():
    ap = argparse.ArgumentParser(description="Basic Pitch 音频转MIDI")
    ap.add_argument("--audio", required=True, help="输入音频路径 wav/mp3/m4a/flac")
    ap.add_argument("--out", default="output", help="MIDI输出目录(默认 output)")
    args = ap.parse_args()
    transcribe(args.audio, args.out)


if __name__ == "__main__":
    main()
