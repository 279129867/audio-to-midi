# -*- coding: utf-8 -*-
"""
analyze_midi.py: 读取 MIDI 文件, 输出音符数、时长、音域、音符序列, 供学习分析。
用法:
    python analyze_midi.py output/piano_15s.mid
    python analyze_midi.py output/piano_15s.mid --out analysis.txt
"""
import argparse
import pretty_midi
import numpy as np

NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def note_name(pitch: int) -> str:
    return NAMES[pitch % 12] + str(pitch // 12 - 1)

def analyze(mid_path: str) -> str:
    pm = pretty_midi.PrettyMIDI(mid_path)
    notes = []
    for inst in pm.instruments:
        notes.extend(inst.notes)
    notes.sort(key=lambda n: n.start)

    pitches = [n.pitch for n in notes]
    lines = [
        f"文件: {mid_path}",
        f"音符数: {len(notes)}",
        f"时长: {pm.get_end_time():.2f}s",
        f"轨道数: {len(pm.instruments)}",
        f"音域: {note_name(min(pitches))}({min(pitches)}) ~ {note_name(max(pitches))}({max(pitches)})",
        f"平均音高: {np.mean(pitches):.1f}",
        "",
        "音符序列(音名 | 起始秒 | 时长秒):",
    ]
    for n in notes:
        lines.append(f"  {note_name(n.pitch):>4}  {n.start:7.2f}  时长 {n.end-n.start:.2f}")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(description="分析MIDI音符/音域/序列")
    ap.add_argument("midi", help="输入 .mid 路径")
    ap.add_argument("--out", help="可选: 写入文本文件, 默认打印到屏幕")
    args = ap.parse_args()
    text = analyze(args.midi)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"已写出: {args.out}")
    else:
        print(text)

if __name__ == "__main__":
    main()
