import math
import pandas as pd
import streamlit as st


# -------------------------
# ページ設定
# -------------------------
st.set_page_config(
    page_title="RLC交流回路計算",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ RLC交流回路計算アプリ")

st.write(
    "抵抗・コイル・コンデンサから、"
    "RLC直列回路のインピーダンスや電力を計算します。"
)


# -------------------------
# 入力
# -------------------------
st.header("① 回路条件を入力")

col1, col2 = st.columns(2)

with col1:
    R = st.number_input(
        "抵抗 R [Ω]",
        min_value=0.1,
        value=10.0,
        step=1.0
    )

    L = st.number_input(
        "インダクタンス L [H]",
        min_value=0.0,
        value=0.1,
        step=0.01,
        format="%.3f"
    )

    C = st.number_input(
        "静電容量 C [F]",
        min_value=0.000001,
        value=0.0001,
        step=0.00001,
        format="%.6f"
    )

with col2:
    f = st.number_input(
        "周波数 f [Hz]",
        min_value=0.1,
        value=50.0,
        step=1.0
    )

    V = st.number_input(
        "電源電圧 V [V]",
        min_value=0.1,
        value=100.0,
        step=10.0
    )


# -------------------------
# 計算
# -------------------------
omega = 2 * math.pi * f

XL = omega * L
XC = 1 / (omega * C)

X = XL - XC

Z = math.sqrt(R**2 + X**2)

I = V / Z

power_factor = R / Z

P = V * I * power_factor

Q = V * I * math.sin(math.atan2(X, R))

S = V * I

phase = math.degrees(math.atan2(X, R))


# -------------------------
# 回路状態
# -------------------------
if X > 0:
    circuit_type = "誘導性（コイルの影響が大きい）"
elif X < 0:
    circuit_type = "容量性（コンデンサの影響が大きい）"
else:
    circuit_type = "抵抗性（共振状態）"


# -------------------------
# 結果
# -------------------------
st.header("② 計算結果")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("インピーダンス |Z|", f"{Z:.2f} Ω")
    st.metric("電流 I", f"{I:.2f} A")

with col2:
    st.metric("力率", f"{power_factor:.3f}")
    st.metric("位相角", f"{phase:.2f}°")

with col3:
    st.metric("有効電力 P", f"{P:.2f} W")
    st.metric("無効電力 Q", f"{Q:.2f} var")

st.write(f"**皮相電力 S：{S:.2f} VA**")
st.write(f"**回路の状態：{circuit_type}**")


# -------------------------
# 詳細
# -------------------------
st.header("③ 詳細な計算値")

results = {
    "項目": [
        "角周波数 ω",
        "誘導リアクタンス XL",
        "容量リアクタンス XC",
        "合成リアクタンス X",
        "インピーダンス |Z|",
        "電流 I",
        "力率",
        "位相角",
        "有効電力 P",
        "無効電力 Q",
        "皮相電力 S"
    ],
    "値": [
        f"{omega:.2f} rad/s",
        f"{XL:.2f} Ω",
        f"{XC:.2f} Ω",
        f"{X:.2f} Ω",
        f"{Z:.2f} Ω",
        f"{I:.2f} A",
        f"{power_factor:.3f}",
        f"{phase:.2f}°",
        f"{P:.2f} W",
        f"{Q:.2f} var",
        f"{S:.2f} VA"
    ]
}

st.table(pd.DataFrame(results))


# -------------------------
# 周波数特性
# -------------------------
st.header("④ 周波数によるインピーダンスの変化")

frequencies = [
    max(1, f * 0.1 * i)
    for i in range(1, 21)
]

impedances = []

for freq in frequencies:
    w = 2 * math.pi * freq
    xl = w * L
    xc = 1 / (w * C)
    x = xl - xc
    z = math.sqrt(R**2 + x**2)

    impedances.append(z)

chart_data = pd.DataFrame(
    {
        "周波数 [Hz]": frequencies,
        "インピーダンス [Ω]": impedances
    }
)

st.line_chart(
    chart_data.set_index("周波数 [Hz]")
)


# -------------------------
# 説明
# -------------------------
st.header("⑤ このアプリについて")

st.write(
    """
    このアプリは、RLC直列交流回路を対象として、
    電気電子工学で学ぶ交流回路の計算をWebアプリ化したものです。

    PythonとStreamlitを使用して、
    入力値に応じてインピーダンス・電流・力率・電力などを
    リアルタイムで計算できるようにしています。
    """
)