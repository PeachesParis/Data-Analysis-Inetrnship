"""Functions for data cleaning and preprocessing."""

import pandas as pd
import numpy as np
from typing import Tuple, List, Optional


def load_raw_data(filepath: str) -> pd.DataFrame:
    """
    Load raw data from a file.
    
    Args:
        filepath: Path to the data file (csv, xlsx, etc.)
        
    Returns:
        pandas DataFrame with loaded data
    """
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        return pd.read_excel(filepath)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")


def remove_duplicates(df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Remove duplicate rows from DataFrame.
    
    Args:
        df: Input DataFrame
        subset: Columns to consider for identifying duplicates. If None, uses all columns.
        
    Returns:
        DataFrame with duplicates removed
    """
    return df.drop_duplicates(subset=subset)


def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop', threshold: float = 0.5) -> pd.DataFrame:
    """
    Handle missing values in DataFrame.
    
    Args:
        df: Input DataFrame
        strategy: 'drop' (remove columns/rows with missing values) or 'fill' (fill with mean/median)
        threshold: Proportion of missing values above which to drop a column (0-1)
        
    Returns:
        DataFrame with missing values handled
    """
    # Drop columns with too many missing values
    df = df.dropna(thresh=len(df) * (1 - threshold), axis=1)
    
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(df.mean(numeric_only=True))
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names (lowercase, replace spaces with underscores).
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with standardized column names
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
    return df


def save_processed_data(df: pd.DataFrame, filepath: str) -> None:
    """
    Save processed data to file.
    
    Args:
        df: DataFrame to save
        filepath: Output file path
    """
    if filepath.endswith('.csv'):
        df.to_csv(filepath, index=False)
    elif filepath.endswith('.xlsx'):
        df.to_excel(filepath, index=False)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")
