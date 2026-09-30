# DSA Preparation in Python

A scalable, clean repository structure for practicing and mastering Data Structures and Algorithms in Python, managed with [uv](https://docs.astral.sh/uv/).

---

## 📁 Repository Structure

The repository is modularized into categories so you can fill in solutions and topics as you learn and grow:

```text
dsa_preparation/
├── pyproject.toml               # Project metadata, uv configuration, dependencies
├── .python-version              # Pinned Python version
├── .gitignore                   # Git ignore rules for caches & virtualenv
├── README.md
│
├── notes/                       # Notes, roadmaps, and reference materials
│   ├── progress_tracker.md      # Living inventory of all topics and files
│   ├── roadmap.md               # Progressive learning roadmap
│   ├── time_space_complexity.md # Big-O reference and operation costs
│   ├── python_dsa_cheatsheet.md # Python standard library reference
│   └── problem_solving_patterns.md # 14 interview problem-solving patterns
│
├── src/
│   └── dsa/
│       ├── __init__.py
│       ├── collections/         # Built-in collections (list, dict, set, string, tuple)
│       ├── star_patterns/       # 22 Star & number pattern problems
│       ├── basic_math/          # Number theory & mathematical foundations
│       ├── recursion/           # Recursion pillars, math, arrays, strings & backtracking
│       └── algorithms/          # Core algorithmic implementations
│           └── sorting/         # Selection, Bubble, Insertion, Merge, Quick Sort & Pseudocode
│
└── tests/                       # Unit tests with pytest
    ├── conftest.py
    └── test_setup.py
```

> **Note**: New folders (e.g., `searching/`, `linked_lists/`, `trees/`, `graphs/`, `dynamic_programming/`) will be incrementally added as we study each topic.

---

## 🚀 Getting Started with `uv`

### 1. Synchronize the environment
Create and sync the virtual environment with installed dependencies:
```bash
uv sync
```

### 2. Running a Python file
Execute any script directly inside the managed environment:
```bash
uv run python path/to/script.py
```

### 3. Running tests
Execute the test suite using pytest:
```bash
uv run pytest
```

Run a specific test file:
```bash
uv run pytest tests/test_setup.py
```

### 4. Code Formatting & Linting
Check and format your code using [ruff](https://github.com/astral-sh/ruff):
```bash
# Check for lint issues
uv run ruff check .

# Automatically fix lint issues
uv run ruff check --fix .

# Auto-format code
uv run ruff format .
```

### 5. Adding dependencies
If you ever want to add new packages (e.g., `pytest-benchmark`, `networkx`, `matplotlib`):
```bash
uv add <package-name>
# or as a development dependency:
uv add --dev <package-name>
```

---

## ✍️ How to Add Your Solutions

1. **Pick a Topic / Pattern**:
   For instance, when solving a two-pointer problem, create a file under:
   `src/dsa/patterns/two_pointers/two_sum_sorted.py`

2. **Add a Corresponding Test (Optional but Recommended)**:
   Create a test under `tests/`:
   `tests/test_two_sum_sorted.py`

3. **Importing Modules**:
   Because `src` is configured in `pyproject.toml`, you can import directly from anywhere:
   ```python
   from dsa.common import ListNode
   ```
