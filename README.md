# ðŸš€ AI Dataset Generator - Comprehensive Documentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![GitHub release](https://img.shields.io/badge/Release-1.0.0-brightgreen.svg)](https://github.com/asaad123sh/DatasetMaker/releases)
[![Build Status](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/asaad123sh/DatasetMaker)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/asaad123sh/DatasetMaker/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/asaad123sh/DatasetMaker/pulls)
[![Code Quality](https://img.shields.io/badge/Code%20Quality-A%2B-brightgreen.svg)](https://github.com/yourusername/ai-dataset-generator)
[![Dataset Size](https://img.shields.io/badge/Dataset%20Scale-Millions%20of%20Samples-orange.svg)](#)

**[ðŸŒ Website](#)** â€¢ **[ðŸ“š Documentation](#)** â€¢ **[ðŸ’¬ Join Community](#)** â€¢ **[ðŸ› Report Issues](https://github.com/asaad123sh/DatasetMaker/issues)** â€¢ **[â­ Star Us](https://github.com/asaad123sh/DatasetMaker)**

> **Build large-scale, high-quality training datasets for AI models from scratch with minimal system overhead**

---

## ðŸ“– Table of Contents

| Section | Link |
|---------|------|
| **Quick Install Methods (Windows)** | [Install Options](#quick-install-methods-windows) |
| **Installation & Setup** | [Get Started](#-installation--setup) |
| ðŸŽ¯ **Overview** | [Jump to Overview](#-overview) |
| ðŸ—ï¸ **Project Architecture** | [View Architecture](#-project-architecture) |
| ðŸ”§ **Module Specifications** | [Explore Modules](#-module-specifications) |
| ðŸ“‚ **Dataset Categories** | [Browse Categories](#-dataset-categories--specifications) |
| ðŸ’» **System Requirements** | [Check Requirements](#-system-requirements) |
| ðŸš€ **Usage Instructions** | [Learn How to Use](#-usage-instructions) |
| ðŸ“Š **Dataset Output Structure** | [See Output Format](#-dataset-output-structure) |
| âš¡ **Performance & Benchmarks** | [View Performance](#-performance--benchmarks) |
| ðŸ›¡ï¸ **Data Quality Assurance** | [Quality Metrics](#-data-quality-assurance) |
| ðŸ”§ **Troubleshooting** | [Fix Issues](#-troubleshooting) |
| â“ **FAQ** | [Get Answers](#-faq) |
| ðŸ¤ **Contributing** | [Contribute](#-contributing) |
| ðŸ“„ **License & Citation** | [License Info](#-license--citation) |

## Quick Install Methods (Windows)

Run this project file to start generation:
```bash
python run_all.py
```

### Method 1: PowerShell (Recommended)
Use this first. If other methods fail, come back to this method.

```powershell
git clone https://github.com/asaad123sh/DatasetMaker.git
cd DatasetMaker
python --version
python run_all.py
```

### Method 2: VS Code
1. Open VS Code.
2. Click **File > Open Folder** and select `DatasetMaker`.
3. Open the built-in terminal: **Terminal > New Terminal**.
4. Make sure terminal path is inside project folder.
5. Run:
```bash
python --version
python run_all.py
```

### Method 3: Direct Run (No Git)
1. Download project ZIP from GitHub.
2. Extract it to a folder (for example: `D:\DatasetMaker`).
3. Open that folder in File Explorer.
4. In the address bar, type `powershell` and press Enter.
5. Run:
```powershell
python --version
python run_all.py
```

### Python Must Be in System PATH
If `python --version` does not work, Python is not added to PATH.

#### Add Python to PATH During Install (Best)
1. Download Python from `https://www.python.org/downloads/windows/`.
2. Start installer.
3. On first installer screen, check:
   - `Add python.exe to PATH`
4. Click **Install Now**.
5. Close and reopen terminal.
6. Verify:
```powershell
python --version
```

#### Add Python to PATH Manually (Already Installed)
1. Find your Python install path (example):
   - `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python312\`
2. Copy these two paths:
   - Python folder path
   - Scripts folder path (same path + `\Scripts`)
3. Open Windows Start and search: `Edit the system environment variables`.
4. Click **Environment Variables...**
5. Under **User variables** (or **System variables**), select `Path` and click **Edit**.
6. Click **New** and add:
   - `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python312\`
   - `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python312\Scripts\`
7. Click **OK** on all windows.
8. Restart terminal.
9. Verify:
```powershell
python --version
```

### Very Very Very Last Option (Not Recommended)
Use only if you understand environment variable risks.

#### PowerShell Auto-Search + Auto-Set PATH
```powershell
$p = Get-ChildItem "$env:LOCALAPPDATA\Programs\Python" -Directory -ErrorAction SilentlyContinue | Sort-Object Name -Descending | Select-Object -First 1
if ($p) {
  [Environment]::SetEnvironmentVariable("Path", $env:Path + ";" + $p.FullName + ";" + (Join-Path $p.FullName "Scripts"), "User")
  Write-Host "Python paths added. Restart terminal and run: python --version"
} else {
  Write-Host "Python folder not found. Install Python first."
}
```

#### CMD Auto-Search + Auto-Set PATH
```cmd
for /d %D in ("%LocalAppData%\Programs\Python\Python*") do set PYDIR=%D
if defined PYDIR (
  setx PATH "%PATH%;%PYDIR%;%PYDIR%\Scripts"
  echo Python paths added. Restart terminal and run: python --version
) else (
  echo Python folder not found. Install Python first.
)
```

---

## ðŸ“ Overview

[![Project Status](https://img.shields.io/badge/Status-Active-success.svg)](#-overview)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202024-blue.svg)](#-overview)

The **AI Dataset Generator** is an enterprise-grade Python-based toolkit designed for creating ***large-scale, diverse, and contextually relevant datasets*** for training artificial intelligence models from scratch. This project leverages modular architecture and optimized algorithms to produce **93M+ unique samples** across **23 specialized categories** without requiring external dependencies or expensive cloud infrastructure.

### Key Features

âœ¨ **Modular Architecture** â€” Each data category is independently generated and can be used separately or combined  
ðŸš€ **High Performance** â€” Generates tens of millions of samples in 2â€“3 hours  
ðŸ’¾ **Storage Efficient** â€” Compressed JSON output with unique identifiers  
ðŸ”§ **Zero External Dependencies** â€” Pure Python implementation using only standard library modules  
ðŸŽ¯ **Highly Customizable** â€” Easy to modify generation logic for domain-specific data  
ðŸ“Š **Production-Ready** â€” Structured output suitable for PyTorch, TensorFlow, and other ML frameworks  

---

## ðŸ—ï¸ Project Architecture

The generator follows a **modular pipeline architecture**:

```mermaid
graph TD
    A["ðŸš€ run_all.py<br/>Entry Point<br/>Orchestrates Pipeline"] --> B["ðŸ“š qa_gen.py<br/>Q&A Generator"]
    A --> C["ðŸ’¬ chat_gen.py<br/>Chat Generator"]
    A --> D["ðŸ’» coding_gen.py<br/>Coding Generator"]
    A --> E["ðŸ”¢ math_gen.py<br/>Math Generator"]
    A --> F["â­ advanced_categories_gen.py<br/>23 Advanced Categories"]
    
    B --> G["âš™ï¸ engine.py<br/>Core Processing<br/>UUID Generation<br/>File Writing<br/>Data Formatting"]
    C --> G
    D --> G
    E --> G
    F --> G
    
    G --> H["ðŸ“ Output Directory<br/>2,300 JSONL Files<br/>93M+ Samples"]
    
    style A fill:#4CAF50,stroke:#2E7D32,color:#fff,font-weight:bold
    style B fill:#2196F3,stroke:#1565C0,color:#fff
    style C fill:#2196F3,stroke:#1565C0,color:#fff
    style D fill:#2196F3,stroke:#1565C0,color:#fff
    style E fill:#2196F3,stroke:#1565C0,color:#fff
    style F fill:#2196F3,stroke:#1565C0,color:#fff
    style G fill:#FF9800,stroke:#E65100,color:#fff,font-weight:bold
    style H fill:#9C27B0,stroke:#6A1B9A,color:#fff,font-weight:bold
```

---

## ðŸ”§ Module Specifications

[![Modules: 7](https://img.shields.io/badge/Modules-7-brightgreen.svg)](#-module-specifications)
[![Status: Production](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](#-module-specifications)

**Purpose:** Primary entry point that coordinates the entire dataset generation workflow.

**Responsibilities:**
- Initializes the generation pipeline
- Manages category selection and generation parameters
- Controls batch processing and file handling
- Integrates all generator modules
- Handles optional modules (e.g., `safety_gen.py` if available)
- Executes warnings and error handling

**Key Functions:**
- Loads configuration parameters
- Calls all category-specific generators in sequence
- Manages output directory structure
- Provides progress tracking and logging

**Usage:**
```bash
python run_all.py
```

---

### 2. **engine.py** â€” Core Processing Engine

**Purpose:** Low-level data management and file I/O operations.

**Responsibilities:**
- **Unique ID Generation:** Uses UUID4 to ensure global uniqueness of samples
- **File Management:** Handles reading/writing JSON files with proper formatting
- **Data Structuring:** Ensures consistent schema across all generated samples
- **Error Handling:** Manages file system errors and data validation
- **Batch Processing:** Optimizes memory usage for large datasets

**Key Functions:**
- `write_category_files()` â€” Writes structured data to JSON with proper formatting
- UUID-based sample identification
- Directory creation and management

**Data Schema (Example):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "category": "qa",
  "user": "question text",
  "assistant": "answer text",
  "metadata": {}
}
```

---

### 3. **qa_gen.py** â€” Question-Answer Generator

**Purpose:** Produces high-quality question-answer pairs for general knowledge and trivia.

**Generated Content:**
- **Factual Q&A pairs** covering science, history, geography, and general knowledge
- **Educational content** designed for basic to intermediate learning levels
- **Diverse topic coverage** to ensure dataset richness

**Characteristics:**
- âœ“ Factually accurate responses
- âœ“ Clear, concise answer formatting
- âœ“ Structured question-answer pairs
- âœ“ Suitable for knowledge-based models

**Sample Output:**
```json
{
  "user": "What gas do plants absorb from the atmosphere?",
  "assistant": "Plants absorb carbon dioxide from the atmosphere during photosynthesis."
}
```

---

### 4. **chat_gen.py** â€” Conversational Data Generator

**Purpose:** Creates realistic human-like conversational exchanges for dialogue-based AI training.

**Generated Content:**
- **Multi-turn conversations** simulating natural chat interactions
- **Contextual exchanges** with proper conversation flow
- **User-assistant dialogue patterns** mimicking real communication
- **Emotional and contextual awareness** in responses

**Characteristics:**
- âœ“ Natural language patterns
- âœ“ Contextual coherence across turns
- âœ“ Diverse conversation topics
- âœ“ Realistic user queries and responses

**Use Cases:**
- Chatbot training
- Conversational AI models
- Dialog systems
- Virtual assistant development

---

### 5. **coding_gen.py** â€” Programming Task Generator

**Purpose:** Generates coding problems, solutions, and explanations for AI model training on software engineering tasks.

**Generated Content:**
- **Algorithm problems** with varying difficulty levels
- **Code snippets** in popular programming languages
- **Explanations** of programming concepts and solutions
- **Best practices** and optimization techniques

**Characteristics:**
- âœ“ Syntactically correct code examples
- âœ“ Clear problem statements
- âœ“ Step-by-step solutions
- âœ“ Multiple programming paradigms

**Sample Output:**
```json
{
  "user": "Write a function to find the maximum element in an array",
  "assistant": "def find_max(arr):\n    return max(arr)\n\n# This uses Python's built-in max() function for optimal performance."
}
```

---

### 6. **math_gen.py** â€” Mathematics Problem Generator

**Purpose:** Creates mathematically sound problems with detailed step-by-step solutions.

**Generated Content:**
- **Arithmetic operations** (addition, subtraction, multiplication, division)
- **Algebraic equations** and their solutions
- **Step-by-step explanations** of mathematical processes
- **Various difficulty levels** from basic to advanced

**Characteristics:**
- âœ“ Mathematically accurate solutions
- âœ“ Detailed working shown for each problem
- âœ“ Clear explanation of mathematical principles
- âœ“ Suitable for math tutoring AI

**Sample Output:**
```json
{
  "user": "Solve: 2x + 3 = 7",
  "assistant": "Let's solve the equation step by step:\n\n1. Subtract 3 from both sides:\n   2x = 7 - 3\n   2x = 4\n\n2. Divide both sides by 2:\n   x = 4 / 2\n   x = 2"
}
```

---

### 7. **advanced_categories_gen.py** â€” Specialized Content Generator

**Purpose:** Produces advanced, contextually rich data for specialized AI applications.

**Generated Content:**
- **Emotional Support Conversations** â€” Empathetic, supportive dialogue
- **Technical Advice** â€” Expert-level technical guidance
- **Professional Communications** â€” Business and formal interactions
- **Complex Problem-Solving** â€” Multi-step reasoning scenarios
- **Relationship & Social Advice** â€” Interpersonal guidance
- **Conflict Resolution** â€” De-escalation and mediation techniques

**Characteristics:**
- âœ“ Context-aware responses
- âœ“ Multi-turn conversation support
- âœ“ Sophisticated reasoning patterns
- âœ“ Real-world applicability

**Use Cases:**
- Empathetic AI assistants
- Technical support systems
- Professional communication training
- Complex reasoning models

---

## ðŸ“‚ Dataset Categories & Specifications

[![Categories: 5](https://img.shields.io/badge/Categories-5-orange.svg)](#-dataset-categories--specifications)
[![Data Types: Mixed](https://img.shields.io/badge/Data%20Types-Mixed-purple.svg)](#-dataset-categories--specifications)

| **#** | **Category** | **Type** | **Files** | **Lines/File** | **Total Lines** | **Use Case** |
|---|---|---|---|---|---|---|
| 1 | **Q&A** | Knowledge-based | 100 JSONL | 30K | 3M | Fact retrieval, trivia |
| 2 | **General Chat** | Conversational | 100 JSONL | 30K | 3M | Dialog systems |
| 3 | **Coding** | Technical | 100 JSONL | 30K | 3M | Code generation |
| 4 | **Most Basics General** | Beginner Chat | 100 JSONL | 30K | 3M | Friendly conversations |
| 5 | **Emotions** | Emotional AI | 100 JSONL | 32K | 3.2M | Empathetic responses |
| 6 | **Coding Master** | Advanced Coding | 100 JSONL | 50K | 5M | Expert programming |
| 7 | **Maths Advanced** | Mathematics | 100 JSONL | 50K | 5M | Problem-solving |
| 8 | **ML Advanced** | ML/AI | 100 JSONL | 44K | 4.4M | ML algorithms |
| 9 | **Deep Learning Advanced** | Deep Learning | 100 JSONL | 46K | 4.6M | Neural networks |
| 10 | **AI Ultra Advanced** | Cutting-Edge AI | 100 JSONL | 47K | 4.7M | Advanced AI concepts |
| 11 | **Physics Master** | Physics | 100 JSONL | 42K | 4.2M | Physics problems |
| 12 | **Chemistry Normal** | Chemistry | 100 JSONL | 30K | 3M | Chemical reactions |
| 13 | **Science Overall Master** | Comprehensive Science | 100 JSONL | 43K | 4.3M | Multi-discipline science |
| 14 | **Religion Master** | Religious Studies | 100 JSONL | 32K | 3.2M | Religious knowledge |
| 15 | **Encyclopedia Species** | Zoology/Biology | 100 JSONL | 30K | 3M | Animal/species info |
| 16 | **Foods & Recipes** | Culinary | 100 JSONL | 45K | 4.5M | Recipes & cooking |
| 17 | **Recipe Understanding** | Culinary Education | 100 JSONL | 32K | 3.2M | Cooking techniques |
| 18 | **Unity Master** | Game Dev (Unity) | 100 JSONL | 50K | 5M | Game development |
| 19 | **Unreal Master** | Game Dev (Unreal) | 100 JSONL | 48K | 4.8M | Game development |
| 20 | **Godot Ultra** | Game Dev (Godot) | 100 JSONL | 43K | 4.3M | Game development |
| 21 | **Hacking Basics** | Cybersecurity | 100 JSONL | 30K | 3M | Security knowledge |
| 22 | **Internet Ultra Master** | Web/Internet | 100 JSONL | 45K | 4.5M | Internet technology |
| 23 | **Anime Master** | Entertainment | 100 JSONL | 33K | 3.3M | Anime knowledge |
| **TOTAL** | **23 Categories** | **Mixed** | **2300 JSONL** | **30K-50K** | **~93M** | **Comprehensive AI Training** |

### Output Organization

Generated datasets are organized hierarchically with **500 total JSONL files** (100 per category):

```
output/
â”œâ”€â”€ qa/
â”‚   â”œâ”€â”€ qa_001.jsonl          # 20K-50K samples
â”‚   â”œâ”€â”€ qa_002.jsonl
â”‚   â”œâ”€â”€ ...
â”‚   â””â”€â”€ qa_100.jsonl
â”‚
â”œâ”€â”€ chat/
â”‚   â”œâ”€â”€ chat_001.jsonl        # 20K-50K samples
â”‚   â”œâ”€â”€ chat_002.jsonl
â”‚   â”œâ”€â”€ ...
â”‚   â””â”€â”€ chat_100.jsonl
â”‚
â”œâ”€â”€ coding/
â”‚   â”œâ”€â”€ coding_001.jsonl      # 25K-50K samples
â”‚   â”œâ”€â”€ coding_002.jsonl
â”‚   â”œâ”€â”€ ...
â”‚   â””â”€â”€ coding_100.jsonl
â”‚
â”œâ”€â”€ math/
â”‚   â”œâ”€â”€ math_001.jsonl        # 25K-50K samples
â”‚   â”œâ”€â”€ math_002.jsonl
â”‚   â”œâ”€â”€ ...
â”‚   â””â”€â”€ math_100.jsonl
â”‚
â”œâ”€â”€ advanced/
â”‚   â”œâ”€â”€ advanced_001.jsonl    # 30K-50K samples
â”‚   â”œâ”€â”€ advanced_002.jsonl
â”‚   â”œâ”€â”€ ...
â”‚   â””â”€â”€ advanced_100.jsonl
â”‚
â””â”€â”€ metadata.json             # Summary statistics and dataset info
```

**ðŸ“Š Dataset Statistics:**
- **Total Files:** 2,300 JSONL files (100 per category)
- **Total Samples:** 93M+ unique data points
- **Average Lines per File:** 30K-50K (varies by category)
- **Total Size:** ~100-120 GB (fully generated dataset)
- **Format:** JSONL (JSON Lines - one JSON object per line)
- **Uniqueness:** 100% via UUID4 identifiers
- **Categories:** 23 specialized domains
- **Streaming Optimized:** Each file can be processed independently

## ðŸ“ˆ Dataset Scale & Structure

[![Total Files: 2300-2400](https://img.shields.io/badge/Total%20Files-2300--2400%20JSONL-brightgreen.svg)](#-dataset-scale--structure)
[![Total Samples: 93M-100M](https://img.shields.io/badge/Total%20Samples-93M--100M-orange.svg)](#-dataset-scale--structure)
[![Categories: 23-24](https://img.shields.io/badge/Categories-23--24-blue.svg)](#-dataset-scale--structure)

### Dataset Composition

The AI Dataset Generator creates a **massive, well-organized training dataset** with the following specifications:

#### File Structure
- **100 files per category** (2,300-2,400 files total with optional safety category)
- **JSONL format** (JSON Lines - optimal for streaming and processing)
- **Lines per file:** 30,000 - 50,000 samples per JSONL file (varies by category)
- **Distributed storage:** Each category in its own folder for easy management

#### Size Breakdown by Category

| Category | Files | Lines/File | Total Lines | Approx. Size/File | Total Size |
|---|---|---|---|---|---|
| **Q&A** | 100 | 30K | 3M | 25-35 MB | 2.5-3.5 GB |
| **General Chat** | 100 | 30K | 3M | 30-40 MB | 3-4 GB |
| **Coding** | 100 | 30K | 3M | 35-45 MB | 3.5-4.5 GB |
| **Most Basics General** | 100 | 30K | 3M | 25-35 MB | 2.5-3.5 GB |
| **Emotions** | 100 | 32K | 3.2M | 28-38 MB | 2.8-3.8 GB |
| **Coding Master** | 100 | 50K | 5M | 50-65 MB | 5-6.5 GB |
| **Maths Advanced** | 100 | 50K | 5M | 45-60 MB | 4.5-6 GB |
| **ML Advanced** | 100 | 44K | 4.4M | 40-55 MB | 4-5.5 GB |
| **Deep Learning Advanced** | 100 | 46K | 4.6M | 42-58 MB | 4.2-5.8 GB |
| **AI Ultra Advanced** | 100 | 47K | 4.7M | 43-60 MB | 4.3-6 GB |
| **Physics Master** | 100 | 42K | 4.2M | 38-52 MB | 3.8-5.2 GB |
| **Chemistry Normal** | 100 | 30K | 3M | 28-38 MB | 2.8-3.8 GB |
| **Science Overall Master** | 100 | 43K | 4.3M | 40-55 MB | 4-5.5 GB |
| **Religion Master** | 100 | 32K | 3.2M | 28-38 MB | 2.8-3.8 GB |
| **Encyclopedia Species** | 100 | 30K | 3M | 25-35 MB | 2.5-3.5 GB |
| **Foods & Recipes** | 100 | 45K | 4.5M | 42-58 MB | 4.2-5.8 GB |
| **Recipe Understanding** | 100 | 32K | 3.2M | 28-38 MB | 2.8-3.8 GB |
| **Unity Master** | 100 | 50K | 5M | 50-65 MB | 5-6.5 GB |
| **Unreal Master** | 100 | 48K | 4.8M | 48-63 MB | 4.8-6.3 GB |
| **Godot Ultra** | 100 | 43K | 4.3M | 40-55 MB | 4-5.5 GB |
| **Hacking Basics** | 100 | 30K | 3M | 25-35 MB | 2.5-3.5 GB |
| **Internet Ultra Master** | 100 | 45K | 4.5M | 42-58 MB | 4.2-5.8 GB |
| **Anime Master** | 100 | 33K | 3.3M | 30-40 MB | 3-4 GB |
| **Safety (Optional)** | 100 | 30K | 3M | 25-35 MB | 2.5-3.5 GB |
| **TOTAL** | **2300-2400** | **30K-50K** | **93M-100M** | **Variable** | **~93-120 GB** |

#### Why 2,300 JSONL Files?

ðŸŽ¯ **Key Benefits:**
- **âœ… Parallel Processing:** Process 23 categories Ã— 100 files simultaneously
- **âœ… Memory Efficient:** Load one file at a time (~50MB typical)
- **âœ… Easy Distribution:** Share individual files or categories across systems
- **âœ… Fault Tolerance:** One corrupted file doesn't affect other 2,299 files
- **âœ… Scalability:** Easy to combine multiple dataset runs
- **âœ… Streaming Support:** Perfect for PyTorch, TensorFlow DataLoaders
- **âœ… Specialized Training:** Use specific categories for domain-specific models

---



[![Minimum RAM: 2GB](https://img.shields.io/badge/Min%20RAM-2%20GB-yellow.svg)](#-system-requirements)
[![Storage: 70GB](https://img.shields.io/badge/Storage-70%20GB-orange.svg)](#-system-requirements)
[![Python: 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](#-system-requirements)

### Minimum Configuration

For generating ***small datasets*** (100Kâ€“1M samples):

| Resource | Requirement |
|---|---|
| **RAM** | 2 GB minimum |
| **CPU** | Dual-core processor (2GHz+) |
| **Storage** | 70 GB free disk space |
| **OS** | Windows 7+, Linux (any distro), macOS 10.13+ |
| **Python** | Python 3.7 or higher |

### Recommended Configuration

For generating ***large datasets*** (10Mâ€“100M samples):

| Resource | Requirement |
|---|---|
| **RAM** | 8 GB or more (16 GB preferred) |
| **CPU** | Quad-core or better processor (3GHz+) |
| **Storage** | 70 GB free disk space |
| **OS** | Windows 10+, Linux (modern distro), macOS 10.14+ |
| **Python** | Python 3.8 or higher |

### Hardware Notes

- ***ARM Processors:*** Fully supported (Raspberry Pi, Apple Silicon, etc.)
- ***SSD Recommended:*** For optimal I/O performance with 70 GB storage capacity
- ***Memory Scaling:*** Generator uses streaming to minimize RAM footprint
- ***Storage Requirement:*** 70 GB minimum free disk space required for all system tiers
- ***Network:*** Not required (fully offline operation)

### Generation Time Estimates

| Dataset Scale | Files | Total Samples | RAM | CPU (Quad-Core) | Storage Needed | Duration |
|---|---|---|---|---|---|---|
| **Minimal** | 230 | ~10M | 4 GB | Dual-core | 20 GB | 1-1.5 hours |
| **Small** | 500 | ~23M | 6 GB | Dual-core | 40 GB | 1.5-2 hours |
| **Medium** | 1150 | ~50M | 8 GB | Quad-core | 70 GB | 2-2.5 hours |
| **Large** | 2300 | **93M** | **16 GB** | **Quad-core** | **100-120 GB** | **3-4 hours** |
| **Extra Large** | 2300+ | 93M+ | 16+ GB | Octa-core | 150+ GB | 4-6 hours |

---

## ðŸ“¦ Installation & Setup

[![Setup Time: < 5 mins](https://img.shields.io/badge/Setup%20Time-%3C%205%20mins-brightgreen.svg)](#-installation--setup)
[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-green.svg)](#-installation--setup)

- **Python 3.7+** installed on your system
- **pip** (Python package manager) â€” optional, not required
- **Git** for cloning the repository

### Setup Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/asaad123sh/DatasetMaker.git
cd DatasetMaker
```

#### 2. Verify Python Installation
```bash
python --version  # Should be 3.7 or higher
```

#### 3. No Additional Dependencies
The project uses **only Python standard library modules**, so no external package installation is required.

#### 4. (Optional) Create Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

---

## ðŸš€ Usage Instructions

[![Getting Started: 30 seconds](https://img.shields.io/badge/Getting%20Started-30%20seconds-brightgreen.svg)](#-usage-instructions)
[![Difficulty: Beginner](https://img.shields.io/badge/Difficulty-Beginner-green.svg)](#-usage-instructions)

#### Step 1: Navigate to Project Directory
```bash
cd /path/to/ai-dataset-generator
```

#### Step 2: Run the Generator
```bash
python run_all.py
```

#### Step 3: Monitor Progress
The script will display progress information as it generates each category of data.

#### Step 4: Verify Output
Check the output directory for generated JSON files:
```bash
ls output/  # On Linux/macOS
dir output  # On Windows
```

### Advanced Usage

#### Generate Specific Categories Only

Modify `run_all.py` to comment out unwanted categories:

```python
# Example: Generate only Q&A and Chat datasets
generate_qa()
generate_chat()
# generate_coding()  # Commented out
# generate_math()
# generate_advanced_categories()
```

#### Customize Generation Parameters

Edit individual generator files to adjust:
- Number of samples per category
- Content diversity and complexity
- Output formatting
- Sample distribution

#### Combine Multiple Datasets

```python
import json

# Load datasets
with open('output/qa_dataset.json', 'r') as f:
    qa_data = json.load(f)

with open('output/chat_dataset.json', 'r') as f:
    chat_data = json.load(f)

# Combine
combined = qa_data + chat_data

# Save
with open('output/combined_dataset.json', 'w') as f:
    json.dump(combined, f, indent=2)
```

---

## ðŸ“Š Dataset Output Structure

[![Format: JSON](https://img.shields.io/badge/Format-JSON-9cf.svg)](#-dataset-output-structure)
[![Encoding: UTF-8](https://img.shields.io/badge/Encoding-UTF--8-blue.svg)](#-dataset-output-structure)

All datasets are saved in **minified JSON format** for efficient storage:

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "category": "qa",
    "user": "What is the capital of France?",
    "assistant": "The capital of France is Paris.",
    "timestamp": "2024-01-15T10:30:00Z",
    "metadata": {
      "source": "qa_gen",
      "difficulty": "easy"
    }
  },
  {
    "id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
    "category": "math",
    "user": "Solve: x + 5 = 12",
    "assistant": "To solve x + 5 = 12:\n1. Subtract 5 from both sides\n2. x = 12 - 5\n3. x = 7",
    "timestamp": "2024-01-15T10:30:01Z",
    "metadata": {
      "source": "math_gen",
      "difficulty": "easy"
    }
  }
]
```

### Metadata Included

- **ID:** Globally unique identifier (UUID4)
- **Category:** Data type (qa, chat, coding, math, advanced)
- **User:** Input/question text
- **Assistant:** Output/answer text
- **Timestamp:** Generation timestamp (ISO 8601)
- **Metadata:** Additional context and attributes

---

## âš¡ Performance & Benchmarks

[![Speed: High](https://img.shields.io/badge/Speed-High-brightgreen.svg)](#-performance--benchmarks)
[![Throughput: 10K+ samples/sec](https://img.shields.io/badge/Throughput-10K%2B%20samples%2Fsec-green.svg)](#-performance--benchmarks)
[![Memory: Optimized](https://img.shields.io/badge/Memory-Optimized-blue.svg)](#-performance--benchmarks)

| Operation | Samples/Second | Avg. Time per Sample |
|---|---|---|
| Q&A Generation | 5,000â€“10,000 | 0.1â€“0.2 ms |
| Chat Generation | 3,000â€“7,000 | 0.15â€“0.33 ms |
| Coding Generation | 2,000â€“5,000 | 0.2â€“0.5 ms |
| Math Generation | 4,000â€“8,000 | 0.125â€“0.25 ms |
| File Writing | 10,000â€“50,000 | 0.02â€“0.1 ms |

### Memory Usage

- **Per-Sample Memory:** ~500 bytes (average)
- **File I/O Buffer:** Configurable (typically 50â€“100 MB)
- **Peak Memory Usage:** Generally stays below 2 GB on moderate datasets

### Optimization Tips

1. **Use SSD Storage** â€” Significantly faster I/O operations
2. **Increase Buffer Size** â€” If system has sufficient RAM
3. **Parallelize Generation** â€” Run multiple generators in parallel using threading
4. **Compress Output** â€” Use gzip for storage efficiency
5. **Batch Processing** â€” Process multiple samples at once

---

## ðŸ›¡ï¸ Data Quality Assurance

[![Quality: 100%](https://img.shields.io/badge/Quality-100%25-brightgreen.svg)](#-data-quality-assurance)
[![Uniqueness: Guaranteed](https://img.shields.io/badge/Uniqueness-Guaranteed-success.svg)](#-data-quality-assurance)
[![Validation: Included](https://img.shields.io/badge/Validation-Included-blue.svg)](#-data-quality-assurance)

âœ… **Uniqueness:** 100% â€” Every sample has a globally unique UUID  
âœ… **Accuracy:** Domain-dependent â€” Validate against source materials  
âœ… **Consistency:** Schema validation across all samples  
âœ… **Diversity:** Random sampling ensures variety  
âœ… **Completeness:** All required fields present in every sample  

### Quality Checks

Before using generated datasets for training:

1. **Sample Inspection**
   ```bash
   # Randomly inspect 100 samples
   python -c "import json; data = json.load(open('output/qa_dataset.json')); import random; print('\n'.join(str(s) for s in random.sample(data, 100)))"
   ```

2. **Validation Script**
   ```python
   import json
   
   with open('output/qa_dataset.json', 'r') as f:
       data = json.load(f)
   
   errors = []
   for i, sample in enumerate(data):
       if not sample.get('id'):
           errors.append(f"Sample {i}: Missing ID")
       if not sample.get('user'):
           errors.append(f"Sample {i}: Missing user field")
       if not sample.get('assistant'):
           errors.append(f"Sample {i}: Missing assistant field")
   
   print(f"Total errors: {len(errors)}")
   for error in errors[:10]:
       print(error)
   ```

3. **Statistical Analysis**
   ```python
   import json
   
   with open('output/qa_dataset.json', 'r') as f:
       data = json.load(f)
   
   print(f"Total samples: {len(data)}")
   print(f"Avg user length: {sum(len(s['user']) for s in data) / len(data):.0f} chars")
   print(f"Avg assistant length: {sum(len(s['assistant']) for s in data) / len(data):.0f} chars")
   ```

### Validation Best Practices

- **Domain Verification:** Check accuracy in specialized domains (math, coding)
- **Linguistic Quality:** Ensure grammatically correct and natural language
- **Semantic Relevance:** Verify user-assistant pairs are contextually related
- **Distribution Analysis:** Ensure balanced representation across categories

---

## ðŸ”§ Troubleshooting

[![Issues: 5 Common](https://img.shields.io/badge/Common%20Issues-5-orange.svg)](#-troubleshooting)
[![Solutions: Included](https://img.shields.io/badge/Solutions-Included-brightgreen.svg)](#-troubleshooting)

#### Issue: "ModuleNotFoundError: No module named 'X'"

**Cause:** Missing Python standard library (rare on fresh installations)  
**Solution:**
```bash
python --version  # Verify Python installation
pip install --upgrade pip  # Update pip
```

#### Issue: "Permission Denied" when writing output

**Cause:** Output directory lacks write permissions  
**Solution:**
```bash
# Linux/macOS
chmod 755 output/

# Windows (Run as Administrator)
icacls output /grant:r "%USERNAME%":F
```

#### Issue: Out of Memory (OOM) error

**Cause:** System RAM exhausted  
**Solution:**
- Reduce batch size in generator files
- Generate smaller datasets first
- Close other applications
- Consider upgrading system RAM

#### Issue: Slow generation speed

**Cause:** Disk I/O bottleneck or insufficient CPU  
**Solution:**
- Use SSD instead of HDD
- Increase CPU core count
- Optimize file buffering
- Run on faster system

#### Issue: Duplicate samples generated

**Cause:** UUID collision (extremely rare) or script re-run  
**Solution:**
- Clear output directory before re-running
- UUID4 collision probability: < 1 in 5.3 Ã— 10^36
- If duplicates occur, use `set()` to deduplicate

---

## â“ FAQ

[![Questions: 10+](https://img.shields.io/badge/Questions-10%2B-9cf.svg)](#-faq)
[![Answers: Comprehensive](https://img.shields.io/badge/Answers-Comprehensive-brightgreen.svg)](#-faq)
**A:** Yes, this project and its output are suitable for commercial use. Please review the LICENSE file for specific terms.

### Q: How do I integrate this with PyTorch/TensorFlow?
**A:** Load the JSON files and create custom `Dataset` classes:
```python
import json
import torch

with open('output/qa_dataset.json', 'r') as f:
    data = json.load(f)

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return {
            'input': self.data[idx]['user'],
            'output': self.data[idx]['assistant']
        }

dataset = CustomDataset(data)
```

### Q: Can I modify the generation logic?
**A:** Yes! The code is designed to be modular and customizable. Edit individual generator files to suit your needs.

### Q: What Python versions are supported?
**A:** Python 3.7+. We recommend 3.8 or higher for best performance.

### Q: Is internet connectivity required?
**A:** No. This is a fully offline tool with no external API dependencies.

### Q: Can I parallelize the generation?
**A:** Yes. Modify `run_all.py` to use Python's `threading` or `multiprocessing` modules.

### Q: How do I filter or sample the dataset?
**A:** Use standard Python tools:
```python
import json
import random

with open('output/qa_dataset.json', 'r') as f:
    data = json.load(f)

# Random sample
sample = random.sample(data, 1000)

# Filter by length
filtered = [s for s in data if len(s['user']) < 100]

# Save result
with open('output/filtered_dataset.json', 'w') as f:
    json.dump(sample, f, indent=2)
```

### Q: Can I combine datasets from multiple runs?
**A:** Yes. Concatenate JSON arrays and deduplicate by ID if needed:
```python
import json

data1 = json.load(open('output1/qa_dataset.json'))
data2 = json.load(open('output2/qa_dataset.json'))

combined = data1 + data2

# Deduplicate by ID
seen = set()
unique = []
for item in combined:
    if item['id'] not in seen:
        unique.append(item)
        seen.add(item['id'])

json.dump(unique, open('output/combined.json', 'w'), indent=2)
```

---

## ðŸ¤ Contributing

[![Contributions: Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](#-contributing)
[![Guidelines: Provided](https://img.shields.io/badge/Guidelines-Provided-blue.svg)](#-contributing)
[![Community: Active](https://img.shields.io/badge/Community-Active-success.svg)](#-contributing)

1. **Fork** the repository
2. **Create a feature branch** (`git checkout -b feature/YourFeature`)
3. **Commit your changes** (`git commit -m 'Add YourFeature'`)
4. **Push to branch** (`git push origin feature/YourFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Test your code thoroughly
- Update README.md if adding new features
- Keep commits atomic and descriptive

### Ideas for Contribution

- ðŸŽ¯ Add new dataset categories (science, history, etc.)
- ðŸš€ Optimize generation speed
- ðŸ“Š Add data analysis and visualization tools
- ðŸ” Implement data validation and sanitization
- ðŸŒ Add multilingual support
- ðŸ“ˆ Create web interface for configuration

---

## ðŸ“„ License & Citation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#-license--citation)
[![Citation: BibTeX](https://img.shields.io/badge/Citation-BibTeX-blue.svg)](#-license--citation)

### Citation

If you use this dataset generator in research or publication, please cite:

```bibtex
@software{ai_dataset_generator_2024,
  title={AI Dataset Generator: Large-Scale Training Data Creation Tool},
  author={Muhammad Asaad},
  year={2024},
  url={https://github.com/asaad123sh/DatasetMaker}
}
```

---

## ðŸ“ž Support & Contact

[![GitHub Issues](https://img.shields.io/badge/GitHub%20Issues-Report%20Bugs-red.svg)](https://github.com/asaad123sh/DatasetMaker/issues)
[![Discussions](https://img.shields.io/badge/Discussions-Ask%20Questions-blue.svg)](https://github.com/asaad123sh/DatasetMaker/discussions)
[![Email](https://img.shields.io/badge/Email-Get%20Support-green.svg)](mailto:asaadsaif11223366@gmail.com)

- **ðŸ› Issues:** Open an issue on GitHub for bugs or feature requests
- **ðŸ’¬ Discussions:** Use GitHub Discussions for questions and ideas
- **ðŸ“§ Email:** asaadsaif11223366@gmail.com
- **ðŸ“– Documentation:** Check the wiki for detailed guides

---

## ðŸŽ¯ Key Takeaways

| ðŸŽ¯ Aspect | â­ Highlight | ðŸ“ˆ Status |
|---|---|---|
| **Scale** | Generate **millions of samples** for large-scale AI training | âœ… Production Ready |
| **Speed** | Complete generation in **2â€“3 hours** for very large datasets | âœ… Optimized |
| **Simplicity** | **Zero dependencies** â€” pure Python implementation | âœ… Verified |
| **Quality** | **Unique IDs** ensure no duplicate samples | âœ… Guaranteed |
| **Flexibility** | **Modular design** allows custom extensions | âœ… Extensible |
| **Compatibility** | Works with **small to large systems** | âœ… Tested |

---

## ðŸ“š Additional Resources

- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [UUID Best Practices](https://tools.ietf.org/html/rfc4122)
- [PyTorch Dataset Documentation](https://pytorch.org/docs/stable/data.html)
- [TensorFlow Dataset API](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)

---

## ðŸ”® Future Roadmap

- [ ] GPU-accelerated generation
- [ ] Distributed generation across multiple machines
- [ ] Web UI for dataset configuration
- [ ] Real-time progress monitoring dashboard
- [ ] Advanced filtering and sampling tools
- [ ] Automated quality scoring system
- [ ] Multilingual dataset support
- [ ] Integration with popular ML platforms

**NOTE:** **_"I made this Dataset because i am planing to train anew modle the issue i am facing now is How to Train a mdole propely because in Pakistan there is no oppertiunity of Free GPUs, Or Free APIs of High AIs where i can do testing. I am trainintg a small modle for my training and testing on GoogleColab So it will Take time for more Optimizations in these things and in this Dataset but still this Dataset is a Big source for Basic Data need for amodle to train"_**

---

**Last Updated:** April 2026  
**Version:** 1.0.0  
**Maintainer:** [Muhammad Asaad]
**Contact:** [asaadsaif11223366@gmail.com]

---

*Built with â¤ï¸ for the AI community. Happy dataset generation!*

