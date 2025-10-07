import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from alignments.scoring import dna_score, blosum62
from alignments.needleman_wunsch import needleman_wunsch
from alignments.smith_waterman import smith_waterman
from alignments.utils import draw_matrix, path_from_directions

st.set_page_config(page_title="Sequence Alignment Visualizer", layout="wide")

st.title("Sequence Alignment Visualizer")
st.write("Global: Needleman–Wunsch • Local: Smith–Waterman")

with st.sidebar:
    st.header("Inputs")
    seq_a = st.text_input("Sequence A", value="GATTACA")
    seq_b = st.text_input("Sequence B", value="GCATGCU")

    algorithm_choice = st.selectbox("Algorithm", ["Needleman–Wunsch (Global)", "Smith–Waterman (Local)"])
    scoring_choice = st.selectbox("Scoring", ["DNA (match/mismatch)", "Protein (BLOSUM62 subset)"])

    if scoring_choice == "DNA (match/mismatch)":
        match_val = st.number_input("Match score", value=1, step=1)
        mismatch_val = st.number_input("Mismatch score", value=-1, step=1)

        def score_fn(a, b):
            return dna_score(a, b, match=match_val, mismatch=mismatch_val)
    else:
        fallback_val = st.number_input("Fallback score (if AA pair missing)", value=-1, step=1)

        def score_fn(a, b):
            return blosum62(a, b, fallback=fallback_val)

    gap_penalty = st.number_input("Gap penalty (negative)", value=-2, step=1)


col_left, col_right = st.columns([1, 1])

run_clicked = st.button("Run Alignment")

if run_clicked:
    if algorithm_choice.startswith("Needleman"):
        dp, direction, aln_a, aln_b, fill_order = needleman_wunsch(
            seq_a, seq_b, score_fn, gap_penalty=gap_penalty
        )
        end_cell = (len(seq_a), len(seq_b))
        score_value = dp[-1][-1]
    else:
        dp, direction, aln_a, aln_b, fill_order, max_cell = smith_waterman(
            seq_a, seq_b, score_fn, gap_penalty=gap_penalty
        )
        end_cell = max_cell
        score_value = dp[end_cell[0]][end_cell[1]]

    with col_left:
        st.subheader("Alignment")
        st.code(aln_a)
        st.code(aln_b)
        st.write(f"Score: **{score_value}**")

    with col_right:
        st.subheader("DP Matrix")
        try:
            path_cells = path_from_directions(direction, end_cell[0], end_cell[1])
        except Exception:
            path_cells = None

        fig = draw_matrix(dp, path_cells=path_cells, title="Dynamic Programming Matrix")
        st.pyplot(fig)
