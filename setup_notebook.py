"""
Setup Notebook Module

This module provides functions to set up the environment for Jupyter notebooks.
It includes functions to install required packages, configure paths, and set up
visualization settings.
"""

import sys
import os
import subprocess
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from IPython.display import display, HTML

def install_packages():
    """
    Install required packages if they are not already installed.
    """
    required_packages = [
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'statsmodels',
        'plotly',
        'ipywidgets',
        'tqdm'
    ]
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} installed successfully.")

def configure_paths():
    """
    Configure paths for the project.
    """
    # Add the project root directory to the Python path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.append(project_root)
    
    # Create assets directory if it doesn't exist
    assets_dir = os.path.join(project_root, 'assets')
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    
    return project_root, assets_dir

def configure_visualization():
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

def display_header():
    """
    Display a header for the notebook.
    """
    header_html = """
    <div style="background-color:#4472C4; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">Challenge Ingredion - Sprint 1</h1>
        <h3 style="color:white; text-align:center;">Análise de Dados de NDVI/EVI para Previsão de Produtividade Agrícola</h3>
    </div>
    """
    display(HTML(header_html))

def setup_environment():
    """
    Set up the environment for the notebook.
    """
    install_packages()
    project_root, assets_dir = configure_paths()
    configure_visualization()
    display_header()
    
    print(f"Environment setup complete.")
    print(f"Project root: {project_root}")
    print(f"Assets directory: {assets_dir}")
    
    return project_root, assets_dir

if __name__ == "__main__":
    setup_environment()
