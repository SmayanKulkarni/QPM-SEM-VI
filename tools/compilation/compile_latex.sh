#!/bin/bash
# Script to compile the generated LaTeX study material

if [ "$#" -ne 1 ]; then
    echo "Usage: ./compile_latex.sh <filename.tex>"
    exit 1
fi

TEX_FILE=$1
# Remove extension if provided
BASE_NAME="${TEX_FILE%.tex}"

echo "Compiling $BASE_NAME.tex (Pass 1)..."
pdflatex -interaction=nonstopmode "$BASE_NAME.tex"

echo "Compiling $BASE_NAME.tex (Pass 2 for outlines & TOC)..."
pdflatex -interaction=nonstopmode "$BASE_NAME.tex"

if [ -f "$BASE_NAME.pdf" ]; then
    echo "Success! Output generated: $BASE_NAME.pdf"
else
    echo "Error compiling PDF. Check the .log file."
fi
