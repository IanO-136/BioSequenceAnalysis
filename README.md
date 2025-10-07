# DNA/Protein Sequence Alignment Visualizer
An alignment visualizer implementing Needleman–Wunsch (global) and Smith–Waterman (local) using Streamlit.
It supports simple DNA scoring (match/mismatch) and amino-acid scoring with a small BLOSUM62 subset.

## Features
- Global (Needleman–Wunsch) and Local (Smith–Waterman) alignment
- Adjustable penalties
- DNA and Amino Acid Scoring
- Visualizes the alignment into a heat map

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open the local URL that Streamlit prints.