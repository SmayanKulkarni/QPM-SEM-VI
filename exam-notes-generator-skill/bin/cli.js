#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const PKG_ROOT = path.resolve(__dirname, '..');
const TEMPLATES_DIR = path.join(PKG_ROOT, 'templates');

function printHelp() {
  console.log(`
exam-notes-generator-skill v${require('../package.json').version}

Usage:
  npx exam-notes-generator init [target-dir]    Scaffold the skill into a project
  npx exam-notes-generator --help              Show this help

Commands:
  init [dir]    Install .github/docs/skills/exam-notes-generator/ and all
                supporting files (copilot-instructions, prompts, references)
                into the specified directory (default: current working dir).

What gets installed:
  .github/
    docs/
      copilot-instructions.md
      prompts/
        exam-notes.prompt.md
      skills/
        exam-notes-generator/
          SKILL.md
          references/
            flashcard-format.md
            ocr-strategy.md
            soffice-convert.md
    reference-notes/
      (placeholder for reference .tex examples)

Examples:
  npx exam-notes-generator init
  npx exam-notes-generator init ./my-course-project
  npx exam-notes-generator init /home/user/workspace/bio-notes
`);
}

function scaffold(targetDir) {
  const destRoot = path.resolve(targetDir);
  const githubDir = path.join(destRoot, '.github');

  // Define the full directory structure we want to create
  const dirs = [
    path.join(githubDir, 'docs', 'prompts'),
    path.join(githubDir, 'docs', 'skills', 'exam-notes-generator', 'references'),
    path.join(githubDir, 'reference-notes'),
    path.join(githubDir, 'reference-notes', 'template'),
  ];

  for (const d of dirs) {
    if (!fs.existsSync(d)) {
      fs.mkdirSync(d, { recursive: true });
      console.log(`  created: ${path.relative(process.cwd(), d)}`);
    } else {
      console.log(`  exists:  ${path.relative(process.cwd(), d)}`);
    }
  }

  // Map of template files -> destination paths
  const files = [
    {
      src: path.join(TEMPLATES_DIR, 'copilot-instructions.md'),
      dst: path.join(githubDir, 'docs', 'copilot-instructions.md'),
    },
    {
      src: path.join(TEMPLATES_DIR, 'prompts', 'exam-notes.prompt.md'),
      dst: path.join(githubDir, 'docs', 'prompts', 'exam-notes.prompt.md'),
    },
    {
      src: path.join(TEMPLATES_DIR, 'skills', 'exam-notes-generator', 'SKILL.md'),
      dst: path.join(githubDir, 'docs', 'skills', 'exam-notes-generator', 'SKILL.md'),
    },
    {
      src: path.join(TEMPLATES_DIR, 'skills', 'exam-notes-generator', 'references', 'flashcard-format.md'),
      dst: path.join(githubDir, 'docs', 'skills', 'exam-notes-generator', 'references', 'flashcard-format.md'),
    },
    {
      src: path.join(TEMPLATES_DIR, 'skills', 'exam-notes-generator', 'references', 'ocr-strategy.md'),
      dst: path.join(githubDir, 'docs', 'skills', 'exam-notes-generator', 'references', 'ocr-strategy.md'),
    },
    {
      src: path.join(TEMPLATES_DIR, 'skills', 'exam-notes-generator', 'references', 'soffice-convert.md'),
      dst: path.join(githubDir, 'docs', 'skills', 'exam-notes-generator', 'references', 'soffice-convert.md'),
    },
    {
      src: path.join(TEMPLATES_DIR, 'reference', 'reference-study-source.tex'),
      dst: path.join(githubDir, 'reference-notes', 'template', 'reference-study-source.tex'),
    },
  ];

  let installed = 0;
  let updated = 0;

  for (const { src, dst } of files) {
    if (!fs.existsSync(src)) {
      console.error(`  missing template: ${src}`);
      continue;
    }
    const content = fs.readFileSync(src, 'utf-8');
    const exists = fs.existsSync(dst);
    fs.writeFileSync(dst, content, 'utf-8');
    if (exists) {
      console.log(`  updated: ${path.relative(process.cwd(), dst)}`);
      updated++;
    } else {
      console.log(`  installed: ${path.relative(process.cwd(), dst)}`);
      installed++;
    }
  }

  console.log(`\nDone. ${installed} new file(s) installed, ${updated} updated.`);
  console.log(`Target: ${destRoot}`);
  console.log(`\nNext steps:`);
  console.log(`  1. Add your source materials (PDF / PPTX / DOCX) to the project.`);
  console.log(`  2. Ask your AI assistant to generate notes using the skill.`);
  console.log(`  3. Or invoke the slash prompt: /exam-notes <source-path> [output-type]`);
}

function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
    printHelp();
    process.exit(0);
  }

  const command = args[0];

  if (command === 'init') {
    const target = args[1] || '.';
    scaffold(target);
  } else {
    console.error(`Unknown command: ${command}`);
    printHelp();
    process.exit(1);
  }
}

main();
