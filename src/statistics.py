"""Functions for computing summary statistics and data description."""

import pandas as pd
import numpy as np
from typing import Dict, Any


def get_data_overview(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Get a comprehensive overview of the dataset.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary containing dataset overview
    """
    return {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'missing_percentages': (df.isnull().sum() / len(df) * 100).to_dict(),
        'duplicates': df.duplicated().sum()
    }


def get_numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get summary statistics for numeric columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with summary statistics
    """
    return df.describe().T


def get_categorical_summary(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Get summary statistics for categorical columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with value counts for each categorical column
    """
    categorical_cols = df.select_dtypes(include=['object']).columns
    return {col: df[col].value_counts() for col in categorical_cols}


def correlation_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute correlation matrix for numeric columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Correlation matrix as DataFrame
    """
    return df.select_dtypes(include=[np.number]).corr()


def generate_data_dictionary(df: pd.DataFrame, descriptions: Dict[str, str] = None) -> pd.DataFrame:
    """
    Generate a data dictionary for the DataFrame.
    
    Args:
        df: Input DataFrame
        descriptions: Optional dictionary mapping column names to descriptions
        
    Returns:
        DataFrame containing the data dictionary
    """
    dictionary = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.values,
        'Non-Null Count': df.count().values,
        'Unique Values': [df[col].nunique() for col in df.columns],
        'Sample Values': [', '.join(df[col].dropna().astype(str).head(2).tolist()) for col in df.columns]
    })
    
    if descriptions:
        dictionary['Description'] = dictionary['Column'].map(descriptions).fillna('No description')
    
    return dictionary
