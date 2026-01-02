
# Plaswrap

**Plaswrap** is a comprehensive wrapper tool for plasmid detection, classification, and downstream analysis. It integrates multiple state-of-the-art tools (PlasForest, Platon, Bakta, etc.) into a streamlined workflow.

---

## 📋 Table of Contents
- [Installation](#installation)
  - [Environment Setup](#environment-setup-crucial)
  - [Package Installation](#package-installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
  - [End-to-End Workflow](#end-to-end-workflow)
  - [Individual Modules](#individual-modules)
- [Output](#output)
- [License](#license)

---

## 🛠️ Installation

### Environment Setup (Crucial)
**Plaswrap operates using a multi-environment strategy.** The main wrapper runs in the `plaswrap` environment, while specific sub-modules rely on their own isolated Conda environments to handle conflicting dependencies.

You **MUST** create the following 5 conda environments before running Plaswrap. We provide YAML configuration files for each.

1.  **Main Environment (Plaswrap)**
    ```bash
    conda env create -f plaswrap.yaml
    ```
2.  **PlasForest Environment**
    ```bash
    conda env create -f plasforest.yaml
    ```
3.  **PlasX Environment**
    ```bash
    conda env create -f plasx.yaml
    ```
4.  **Plascad Environment** (for mobility analysis)
    ```bash
    conda env create -f plascad.yaml
    ```
5.  **Bakta Environment** (for annotation)
    ```bash
    conda env create -f bakta.yaml
    ```

### Package Installation
Once the environments are created, activate the main environment and install Plaswrap:

```bash
# 1. Activate the main environment
conda activate plaswrap

# 2. Clone the repository
git clone [https://github.com/yourusername/Plaswrap.git](https://github.com/yourusername/Plaswrap.git)
cd Plaswrap

# 3. Install via pip
pip install .

```

> **Note for Developers:** If you are modifying the code, use `pip install -e .` for editable mode.

---

## 💾 Database Setup

Plaswrap requires several databases. You can download them individually using the helper commands.

**Example: Downloading databases for PlasForest and Platon**

```bash
# Download PlasForest DB (Requires specifying output directory)
Plaswrap plasforest download-db -o /path/to/databases/plasforest_db

# Download Platon DB
Plaswrap platon download-db -o /path/to/databases/platon_db

# Download Bakta DB
Plaswrap annot download-db -o /path/to/databases/bakta_db

```

---

## 🚀 Usage

### End-to-End Workflow 

The default workflow (`end_to_end_wf`) now focuses on the most accurate predictors: **PlasForest** and **Platon**. It identifies plasmids from contigs and performs downstream analysis (Circularity, AMR, Virulence Factors, etc.).

**Command:**

```bash
Plaswrap end_to_end_wf \
  -i assemblies.fasta \
  -o results_output \
  --model /path/to/plasforest.sav \
  --database /path/to/plasmid_refseq.fasta \
  --platondb /path/to/platon_db \
  --baktadb /path/to/bakta_db \
  -t 16

```

> **Note:** For `end_to_end_wf`, you must specify `--model` and `--database` separately for PlasForest.

### Individual Modules

You can also run tools individually.

| Module | Command Example | Description |
| --- | --- | --- |
| **PlasForest** | `Plaswrap plasforest run -i input.fa -o out_dir --model model.sav --database db.fasta` | Machine learning-based detection |
| **Platon** | `Plaswrap platon run -i input.fa -o out_dir --platondb /path/to/db` | Replicon/protein-based detection |
| **Bakta** | `Plaswrap annot run -i plasmid.fa -o out_dir --baktadb /path/to/db` | Functional annotation |
| **AMR** | `Plaswrap amr -i plasmid.fa -o out_dir` | Antibiotic resistance gene detection |
| **Virulence** | `Plaswrap vf -i plasmid.fa -o out_dir` | Virulence factor detection |
| **Circularity** | `Plaswrap check_circularity -i input.fa -o out_dir` | Check for circular topology |

---

## 📂 Output

### Summary File

The main output of the `end_to_end_wf` is a CSV file named `<prefix>_final_summary.csv`.

**Example Content:**

| ID | Contig size | predicted_by | Circular | AMR | VF | Replicon | Function |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contig_1 | 45000 | plasforest | Yes | blaCTX-M-15 | iutA | IncFII | ... |
| contig_5 | 12000 | plasforest & platon | No | NA | NA | ColRNAI | ... |
| contig_9 | 3500 | platon | Yes | tet(A) | NA | NA | ... |

* **ID**: Contig identifier.
* **Contig size**: Length of the sequence.
* **predicted_by**: Which tool identified it (plasforest, platon, or both).
* **Circular**: Yes/No based on terminal repeats or mapping.
* **AMR/VF**: Detected resistance or virulence genes.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

Developed by HKU-Pasteur, 2026.
