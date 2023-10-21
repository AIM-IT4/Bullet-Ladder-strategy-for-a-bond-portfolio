
# Bullet Strategy Bond Portfolio Backtest

## Overview

This repository contains all the essential components for backtesting a bullet strategy bond portfolio. The bullet strategy involves buying bonds that all mature at the same time, targeting a specific segment of the yield curve. This strategy is useful for investors who have a specific time horizon in mind and want to mitigate the interest rate risk to some extent.

## Repository Structure

- **`python_files/`**: This directory contains Python scripts that are crucial for running the backtest. The main file, `backtest_code.py`, includes code for generating synthetic interest rate data, initializing the bond portfolio, and performing the backtest.

- **`csv_files/`**: Data files in CSV format are stored here. The file `interest_rate_data.csv` contains the synthetic interest rate data, and `portfolio_data.csv` contains detailed information about the portfolio over time.

- **`plots/`**: Graphical representations of the portfolio performance are stored in this directory. The file `portfolio_performance.png` shows how the portfolio value changes over time along with fluctuating interest rates.

## Requirements

- Python 3.x
- NumPy
- pandas
- Matplotlib

## How to Run the Backtest

1. **Environment Setup**: Make sure you have Python 3.x installed along with the required packages: NumPy, pandas, and Matplotlib.
   
2. **Clone the Repository**: Clone this repository to your local machine.

3. **Run the Python Script**: Navigate to the `python_files/` directory and run `backtest_code.py`. This will execute the backtest based on the synthetic interest rate data.

4. **Analyze the Results**: Once the backtest is complete, you can analyze the portfolio's performance using the generated CSV files and plots.

## Contributing

Feel free to fork this repository and make your own modifications. Pull requests for improvements or bug fixes are welcome.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.

## Contact

For any questions or clarifications, please open an issue in this repository.
