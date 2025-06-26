# File Compare Words

A small Python tool that compares the **words** from two text files and shows which words are **missing** in either file.

---

## Features

- Compares word-by-word
- Shows:
  - Words in file1 but not in file2
  - Words in file2 but not in file1
- Optionally writes the missing words to a separate output file if the user agrees. The user can specify the name of the output file.

---

## Usage

```bash
python3 compare.py file1 file2
```

---

## Output

```
Words in file1.txt but not in file2.txt:
apple
banana

Words in file2.txt but not in file1.txt:
grapefruit
```
