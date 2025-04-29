"""
Utilities Module

This module provides utility functions for data processing, visualization, and analysis.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from IPython.display import display, HTML

def setup_visualization():
    """
    Configure visualization settings.
    """
    # Set up matplotlib
    plt.style.use('fivethirtyeight')
    plt.rcParams['figure.figsize'] = (14, 8)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 12
    
    # Set up seaborn
    sns.set(style="whitegrid")
    
    # Suppress warnings
    warnings.filterwarnings('ignore')
    
    print("Visualization settings configured successfully.")

def display_header(title="Challenge Ingredion - Sprint 1", subtitle="Análise de Dados de NDVI/EVI para Previsão de Produtividade Agrícola"):
    """
    Display a header for the notebook.
    """
    header_html = f"""
    <div style="background-color:#4472C4; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">{title}</h1>
        <h3 style="color:white; text-align:center;">{subtitle}</h3>
    </div>
    """
    display(HTML(header_html))
    print("Header displayed successfully.")

def load_data(file_path, verbose=True):
    """
    Load data from a CSV file.
    
    Parameters:
    -----------
    file_path : str
        Path to the CSV file.
    verbose : bool, optional
        Whether to print information about the loaded data. Default is True.
    
    Returns:
    --------
    pandas.DataFrame
        The loaded data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path)
    
    if verbose:
        print(f"Loaded data from {file_path}")
        print(f"Shape: {df.shape}")
        print(f"Columns: {', '.join(df.columns)}")
        print("\nSample data:")
        print(df.head())
    
    return df

def save_data(df, file_path, verbose=True):
    """
    Save data to a CSV file.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The data to save.
    file_path : str
        Path to the CSV file.
    verbose : bool, optional
        Whether to print information about the saved data. Default is True.
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    df.to_csv(file_path, index=False)
    
    if verbose:
        print(f"Saved data to {file_path}")
        print(f"Shape: {df.shape}")

def plot_time_series(df, x, y, title, xlabel, ylabel, figsize=(14, 8), color='blue', alpha=0.7, marker=None, label=None):
    """
    Plot a time series.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The data to plot.
    x : str
        The column name for the x-axis.
    y : str
        The column name for the y-axis.
    title : str
        The title of the plot.
    xlabel : str
        The label for the x-axis.
    ylabel : str
        The label for the y-axis.
    figsize : tuple, optional
        The size of the figure. Default is (14, 8).
    color : str, optional
        The color of the line. Default is 'blue'.
    alpha : float, optional
        The transparency of the line. Default is 0.7.
    marker : str, optional
        The marker style. Default is None.
    label : str, optional
        The label for the line. Default is None.
    
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object.
    matplotlib.axes._axes.Axes
        The axes object.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(df[x], df[y], color=color, alpha=alpha, marker=marker, label=label)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    if label is not None:
        ax.legend()
    
    plt.grid(True)
    plt.tight_layout()
    
    return fig, ax

def plot_comparison(df1, df2, x, y, title, xlabel, ylabel, label1, label2, figsize=(14, 8), color1='blue', color2='red', alpha=0.7, marker=None):
    """
    Plot a comparison between two time series.
    
    Parameters:
    -----------
    df1 : pandas.DataFrame
        The first data to plot.
    df2 : pandas.DataFrame
        The second data to plot.
    x : str
        The column name for the x-axis.
    y : str
        The column name for the y-axis.
    title : str
        The title of the plot.
    xlabel : str
        The label for the x-axis.
    ylabel : str
        The label for the y-axis.
    label1 : str
        The label for the first line.
    label2 : str
        The label for the second line.
    figsize : tuple, optional
        The size of the figure. Default is (14, 8).
    color1 : str, optional
        The color of the first line. Default is 'blue'.
    color2 : str, optional
        The color of the second line. Default is 'red'.
    alpha : float, optional
        The transparency of the lines. Default is 0.7.
    marker : str, optional
        The marker style. Default is None.
    
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object.
    matplotlib.axes._axes.Axes
        The axes object.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(df1[x], df1[y], color=color1, alpha=alpha, marker=marker, label=label1)
    ax.plot(df2[x], df2[y], color=color2, alpha=alpha, marker=marker, label=label2)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    
    plt.grid(True)
    plt.tight_layout()
    
    return fig, ax

def plot_scatter(df, x, y, title, xlabel, ylabel, figsize=(14, 8), color='blue', alpha=0.7, add_trendline=True):
    """
    Plot a scatter plot.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The data to plot.
    x : str
        The column name for the x-axis.
    y : str
        The column name for the y-axis.
    title : str
        The title of the plot.
    xlabel : str
        The label for the x-axis.
    ylabel : str
        The label for the y-axis.
    figsize : tuple, optional
        The size of the figure. Default is (14, 8).
    color : str, optional
        The color of the points. Default is 'blue'.
    alpha : float, optional
        The transparency of the points. Default is 0.7.
    add_trendline : bool, optional
        Whether to add a trendline. Default is True.
    
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object.
    matplotlib.axes._axes.Axes
        The axes object.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.scatter(df[x], df[y], color=color, alpha=alpha)
    
    if add_trendline:
        z = np.polyfit(df[x], df[y], 1)
        p = np.poly1d(z)
        ax.plot(df[x], p(df[x]), 'r--', linewidth=1)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    plt.grid(True)
    plt.tight_layout()
    
    return fig, ax

def evaluate_model(y_true, y_pred, model_name=None):
    """
    Evaluate a model using various metrics.
    
    Parameters:
    -----------
    y_true : array-like
        The true values.
    y_pred : array-like
        The predicted values.
    model_name : str, optional
        The name of the model. Default is None.
    
    Returns:
    --------
    dict
        A dictionary containing the evaluation metrics.
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    metrics = {
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae,
        'R2': r2
    }
    
    if model_name is not None:
        print(f"Evaluation metrics for {model_name}:")
    else:
        print("Evaluation metrics:")
    
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R2: {r2:.4f}")
    
    return metrics

def plot_residuals(y_true, y_pred, figsize=(14, 8)):
    """
    Plot the residuals of a model.
    
    Parameters:
    -----------
    y_true : array-like
        The true values.
    y_pred : array-like
        The predicted values.
    figsize : tuple, optional
        The size of the figure. Default is (14, 8).
    
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object.
    matplotlib.axes._axes.Axes
        The axes object.
    """
    residuals = y_true - y_pred
    
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.scatter(y_pred, residuals, color='blue', alpha=0.7)
    ax.axhline(y=0, color='r', linestyle='--')
    
    ax.set_title('Residual Plot')
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Residuals')
    
    plt.grid(True)
    plt.tight_layout()
    
    return fig, ax

def plot_actual_vs_predicted(y_true, y_pred, figsize=(14, 8)):
    """
    Plot the actual vs. predicted values.
    
    Parameters:
    -----------
    y_true : array-like
        The true values.
    y_pred : array-like
        The predicted values.
    figsize : tuple, optional
        The size of the figure. Default is (14, 8).
    
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object.
    matplotlib.axes._axes.Axes
        The axes object.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.scatter(y_true, y_pred, color='blue', alpha=0.7)
    
    # Add a diagonal line representing perfect predictions
    min_val = min(np.min(y_true), np.min(y_pred))
    max_val = max(np.max(y_true), np.max(y_pred))
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=1)
    
    ax.set_title('Actual vs. Predicted Values')
    ax.set_xlabel('Actual Values')
    ax.set_ylabel('Predicted Values')
    
    plt.grid(True)
    plt.tight_layout()
    
    return fig, ax
