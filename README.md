# Data Analysis Internship Project

4-week internship focused on understanding data, cleaning data, visualization of data, and modeling.

## Project Structure

```
data-analysis-project/
├── data/                          # All data files
│   ├── raw/                       # Original datasets (read-only)
│   ├── processed/                 # Cleaned datasets ready for analysis
│   └── external/                  # Any external reference datasets
│
├── notebooks/                     # Jupyter notebooks for analysis
│   ├── exploration/               # Week 1 exploration notebooks
│   ├── cleaning/                  # Data preparation and cleaning notebooks
│   └── analysis/                  # EDA, modeling, visualization notebooks
│
├── reports/                       # Project deliverables and outputs
│   ├── week1_data_understanding/  # Data Dictionary + Summary Statistics
│   ├── week2_exploratory_analysis/# Upcoming deliverables
│   └── figures/                   # Exported charts and plots
│
├── src/                           # Reusable Python modules
│   ├── data_preparation.py        # Data cleaning and preprocessing functions
│   ├── statistics.py              # Summary statistics functions
│   └── visualization.py           # Chart and plot functions
│
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── .gitignore                     # Git ignore configuration
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd data-analysis-project
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Jupyter
```bash
jupyter notebook
```

## Workflow

- **Week 1**: Explore raw data, create data dictionary, generate summary statistics → Output in `reports/week1_data_understanding/`
- **Week 2+**: Perform exploratory data analysis, clean data, create visualizations → Output in respective week folders
- **Notebooks**: Save exploratory work in `notebooks/` organized by task
- **Scripts**: Reusable functions should be added to `src/` modules

## Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning
- **scipy**: Scientific computing
- **jupyter**: Interactive notebooks

## Notes

- Keep `data/raw/` read-only; all modifications go to `data/processed/`
- Use `.gitignore` to avoid committing large data files or environment files
- Document your analysis process in notebooks with clear markdown cells
