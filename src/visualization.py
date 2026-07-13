"""Functions for creating charts and visualizations."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import List, Optional, Tuple

# Set default style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)


def plot_distribution(df: pd.DataFrame, column: str, kind: str = 'hist', **kwargs) -> None:
    """
    Plot the distribution of a column.
    
    Args:
        df: Input DataFrame
        column: Column name to plot
        kind: 'hist' for histogram, 'kde' for kernel density estimate
        **kwargs: Additional arguments passed to matplotlib
    """
    plt.figure(figsize=(10, 6))
    if kind == 'hist':
        df[column].hist(bins=30, edgecolor='black')
    elif kind == 'kde':
        df[column].plot(kind='density')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency' if kind == 'hist' else 'Density')
    plt.tight_layout()
    plt.show()


def plot_categorical(df: pd.DataFrame, column: str, top_n: int = 10) -> None:
    """
    Plot categorical data as bar chart.
    
    Args:
        df: Input DataFrame
        column: Column name to plot
        top_n: Show only top N categories
    """
    plt.figure(figsize=(12, 6))
    df[column].value_counts().head(top_n).plot(kind='bar', edgecolor='black')
    plt.title(f'Top {top_n} Categories: {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame, figsize: Tuple[int, int] = (12, 10)) -> None:
    """
    Plot correlation heatmap for numeric columns.
    
    Args:
        df: Input DataFrame
        figsize: Figure size (width, height)
    """
    plt.figure(figsize=figsize)
    correlation = df.select_dtypes(include=['number']).corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, fmt='.2f', square=True)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()


def plot_scatter(df: pd.DataFrame, x: str, y: str, hue: Optional[str] = None) -> None:
    """
    Plot scatter plot for two variables.
    
    Args:
        df: Input DataFrame
        x: Column name for x-axis
        y: Column name for y-axis
        hue: Optional column for coloring points
    """
    plt.figure(figsize=(10, 6))
    if hue:
        sns.scatterplot(data=df, x=x, y=y, hue=hue, s=100, alpha=0.6)
    else:
        sns.scatterplot(data=df, x=x, y=y, s=100, alpha=0.6)
    plt.title(f'{y} vs {x}')
    plt.tight_layout()
    plt.show()


def plot_boxplot(df: pd.DataFrame, column: str, groupby: Optional[str] = None) -> None:
    """
    Plot boxplot for data distribution.
    
    Args:
        df: Input DataFrame
        column: Column to plot
        groupby: Optional column to group by
    """
    plt.figure(figsize=(10, 6))
    if groupby:
        sns.boxplot(data=df, x=groupby, y=column)
        plt.title(f'Distribution of {column} by {groupby}')
    else:
        sns.boxplot(data=df, y=column)
        plt.title(f'Distribution of {column}')
    plt.tight_layout()
    plt.show()
