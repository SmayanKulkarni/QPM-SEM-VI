# Converting Legacy .doc / .ppt Files

LibreOffice (`soffice`) can convert legacy formats, but **bare `soffice` hangs in this sandbox**
because the seccomp filter blocks the AF_UNIX sockets it uses for instance management.

Always use the wrapper script at `/mnt/skills/public/pptx/scripts/office/soffice.py`.

## Convert .doc → .docx

```python
import subprocess, shutil

result = subprocess.run([
    "python3", "/mnt/skills/public/pptx/scripts/office/soffice.py",
    "--convert-to", "docx",
    "--outdir", "/tmp/converted",
    "/mnt/user-data/uploads/old_notes.doc"
], capture_output=True, text=True)

if result.returncode != 0:
    print("STDERR:", result.stderr)
else:
    print("Converted to: /tmp/converted/old_notes.docx")
```

## Convert .ppt → .pptx

```python
result = subprocess.run([
    "python3", "/mnt/skills/public/pptx/scripts/office/soffice.py",
    "--convert-to", "pptx",
    "--outdir", "/tmp/converted",
    "/mnt/user-data/uploads/old_slides.ppt"
], capture_output=True, text=True)
```

## After conversion

- Process the converted file at `/tmp/converted/<filename>.docx` or `.pptx` normally.
- Image extraction works the same on the converted file.
- Quality note: some complex layouts may degrade slightly during conversion.
  Flag to the user if content looks truncated.

## Fallback: pandoc

If the soffice wrapper is unavailable:
```bash
pandoc /mnt/user-data/uploads/old_notes.doc -o /tmp/old_notes.md
```
Pandoc handles .doc reasonably well for text but does not preserve images.
