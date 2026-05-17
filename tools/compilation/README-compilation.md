# Study Material Generator Workflow

This directory contains a standardized toolchain to convert raw lecture slides (PPTX) and notes (PDF) into high-density, audit-ready LaTeX study guides with strictly structured numerical examples.

## Prerequisites
Ensure you have the required Python libraries installed:
```bash
pip install PyMuPDF python-pptx Pillow
```

## The Standard Workflow

### Step 1: Extract Text and Images
Place all your source material (`.pdf`, `.pptx`) for a specific subject/module into a single folder (e.g., `~/Desktop/QPM/Data/Module7`).

Run the extraction script, passing your input folder and desired output folder:
```bash
python3 extract_and_prep.py ~/Desktop/QPM/Data/Module7 --output_folder ./outputs/Module7
```
**What this does:**
- Scans the folder and extracts all raw text from slides and PDF pages into `outputs/Module7/raw_extracted_content.txt`.
- Extracts all embedded images (useful for architecture diagrams) into `outputs/Module7/images/`.
- Generates a highly specific LLM Prompt in `outputs/Module7/LLM_PROMPT.md`.

### Step 2: Generate LaTeX Code (AI Generation)
Open the generated `LLM_PROMPT.md` file. It contains a strictly engineered system prompt that forces an LLM (like Antigravity, ChatGPT, or Claude) to structure the notes exactly according to your study standards:
- Bullet points spaced properly (`enumitem`).
- Dedicated `\subsection{Solved Numericals}` at the end of each module.
- Numericals placed in colored `tcolorbox` elements formatted as `Given -> Objective -> Steps -> Interpretation`.

Copy the prompt and the contents of `raw_extracted_content.txt` into your LLM and ask it to generate the `.tex` file. Save the LLM's output as `study_guide.tex` inside your output folder.

### Step 3: Insert Image References
Review the `images/` directory generated in Step 1. Pick the best diagrams (e.g., model architectures). 
In your `study_guide.tex` file, ensure the images are referenced properly:
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\textwidth]{images/extracted_diagram_p4_img1.png}
    \caption{Model Architecture}
\end{figure}
```

### Step 4: Compile the PDF
Run the compilation script. It automatically runs `pdflatex` twice to ensure your Table of Contents and cross-references are built correctly:
```bash
chmod +x compile_latex.sh
./compile_latex.sh ./outputs/Module7/study_guide.tex
```

You now have a clean, perfectly structured, exam-ready PDF!
