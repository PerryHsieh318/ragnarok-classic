
import streamlit as st
import os

st.set_page_config(page_title="開服拓荒攻略站", layout="wide")

st.title("🔥 開服拓荒攻略 - 練等路線")
st.markdown("作者：派瑞 | 最後更新：2025-04-08")

# 圖片顯示 function（設定 width 為 50% 寬度）
image_path = "images/image"
def show_image(file, caption):
    st.image(os.path.join(image_path, file), caption=caption, width=400)

# 分頁切換 Day1 / Day2
tab1, tab2 = st.tabs(["📘 Day 1", "📗 Day 2"])

with tab1:
    st.header("📘 Day 1 練等路線")
    st.markdown("**1 ~ 27等**：主線任務（委託看板先不解）")

    st.markdown("**27等轉職後 ~ 34等**：巨石怪")
    show_image("rock_monster.jpg", "夢羅克")

    st.markdown("**34 ~ 40等**：金二打牛")
    show_image("bull_monster.jpg", "金字塔2F")

    st.markdown("**40 ~ 42等（二轉）**：主線任務")

    st.markdown("**42 ~ 48等**：九尾狐")
    show_image("nine_tail.jpg", "斐揚二樓")

    st.markdown("**48 ~ 50等**：邪骸獸人")
    show_image("undead_orc.jpg", "獸人地下")

    st.markdown("**50 ~ 52等**：主線任務")

    st.markdown("**52 ~ 60等**：綠貝勒斯")
    show_image("green_belros.jpg", "古城郊外")

    st.markdown("**60 ~ 63等**：主線任務")

    st.markdown("**63 ~ 65等**：巫婆")
    show_image("witch.jpg", "鐘塔1F")

    st.markdown("**65 ~ 進階二**：主線任務 + 巫婆刷完時長")

with tab2:
    st.header("📗 Day 2 練等路線")

    st.markdown("**73 ~ 75等**：機械獵犬")
    show_image("mech_hound.jpg", "機械獵犬")

    st.markdown("**75 ~ 78等**：異變堆積物")
    show_image("mutation_pile.jpg", "研究所")

    st.markdown("**78 ~ 81等**：暗.魔法師")
    show_image("dark_mage.jpg", "研究所")

    st.markdown("**81 ~ 82等**：高原佩瑞斯")
    show_image("highland_peris.jpg", "國境檢查站")

    st.markdown("**82 ~ 88等**：鬼娃樹")
    show_image("doll_tree.jpg", "霧之森林")

    st.markdown("**88 ~ 90等**：熊貓波利")
    show_image("panda_poring.jpg", "落日淺灘")

    st.markdown("**90 ~ 92等**：魚人")
    show_image("fishman.jpg", "銀魚湖底")

    st.markdown("**92 ~ 94等**：石頭波利")
    show_image("rock_poring.jpg", "伊達平原")

    st.markdown("**94 ~ 三轉**：紅尾人魚")
    show_image("red_mermaid.jpg", "銀魚湖底")

    st.markdown("**98 ~ 大師**：惡魔之眼")
    show_image("demon_eye.jpg", "聖殿")
