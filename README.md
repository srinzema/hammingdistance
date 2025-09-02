# hammingdistance

Calculate the maximum Hamming distance among a set of sequences.

## Installation

Install via pip:

```bash
pip install git+https://github.com/srinzema/hammingdistance.git
```

Or via conda:

```bash
conda install -c bioconda hammingdistance
```

## Usage

### Command-line

```bash
# Using space-separated sequences
hammingdistance -s ACTG ACGG TCGG ACTA

# Using a file with one sequence per line
hammingdistance -f sequences.txt
```

This will output the maximum hamming distance as an integer.

### Python API

```python
from hammingdistance import max_hamming_distance

seqs = ["ACTG", "ACGG", "TCGG", "ACTA"]
max_dist = max_hamming_distance(seqs)
print(max_dist)
```

## License

MIT License

```text
MIT License

Copyright (c) [2025] [Sybren Rinzema]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
