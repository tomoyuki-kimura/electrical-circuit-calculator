# ⚡ RLC交流回路計算アプリ

PythonとStreamlitを用いて開発した、RLC直列交流回路の計算Webアプリです。

## 🌐 Webアプリ

[こちらから実際にアプリを使用できます](https://electrical-circuit-calculator-ztbhnfiwefkd8dqxakxbjk.streamlit.app/)

## 概要

抵抗・コイル・コンデンサ・周波数・電圧を入力することで、交流回路に関する各種電気量を計算できます。

## 主な機能

- インピーダンスの計算
- 電流の計算
- 力率の計算
- 位相角の計算
- 有効電力の計算
- 無効電力の計算
- 皮相電力の計算
- 回路状態の判定
- 周波数によるインピーダンス変化の可視化

## 使用技術

- Python
- Streamlit
- Pandas

## 開発目的

大学で学んでいる電気電子工学の知識と、Pythonによるプログラミングを組み合わせ、実際に利用できるWebアプリとして実装することを目的に開発しました。

## 学んだこと

電気回路の数式をプログラムとして実装することで、数式をコードに変換する考え方や、ユーザーが入力した値に応じて結果を動的に表示するWebアプリ開発について学びました。

## 実行方法

```bash
pip install -r requirements.txt
python -m streamlit run app.py