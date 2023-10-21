
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic interest rate data
years = 10
time_steps = years * 2  # Semi-annual data points
initial_interest_rate = 0.02  # 2%
volatility = 0.01  # 1% volatility

# Generate interest rate path using a random walk
interest_rates = [initial_interest_rate]
for t in range(1, time_steps):
    change = np.random.normal(0, volatility)
    new_rate = interest_rates[-1] + change
    new_rate = max(0, new_rate)  # No negative interest rates
    interest_rates.append(new_rate)

# Create a DataFrame to hold interest rate data
interest_rate_df = pd.DataFrame({
    'Time': np.arange(0, years, 1/2),
    'Interest Rate': interest_rates
})

# Plot the synthetic interest rate data
plt.figure(figsize=(12, 6))
plt.plot(interest_rate_df['Time'], interest_rate_df['Interest Rate'], label='Interest Rate')
plt.xlabel('Time (Years)')
plt.ylabel('Interest Rate')
plt.title('Synthetic Interest Rate Data')
plt.legend()
plt.grid(True)
plt.show()
# Initialize portfolio variables
initial_capital = 1000000  # 1 Million USD
face_value = 1000  # Face value of each bond
maturity = 5  # 5 years maturity
coupon_frequency = 2  # Semi-annual coupon payments

# Calculate the number of bonds to purchase initially
num_bonds_initial = int(initial_capital / face_value)

# Initialize portfolio DataFrame
columns = ['Time', 'Interest Rate', 'Num Bonds', 'Portfolio Value', 'Coupon Payments']
portfolio_df = pd.DataFrame(columns=columns)

# Populate the portfolio with initial bonds
initial_row = {
    'Time': 0,
    'Interest Rate': initial_interest_rate,
    'Num Bonds': num_bonds_initial,
    'Portfolio Value': initial_capital,
    'Coupon Payments': 0
}
portfolio_df = portfolio_df.append(initial_row, ignore_index=True)

portfolio_df
# Function to calculate bond price given interest rate, maturity, and coupon rate
def bond_price(interest_rate, maturity, coupon_rate, face_value=1000, frequency=2):
    cash_flows = [coupon_rate * face_value / frequency for _ in range(int(maturity * frequency))]
    cash_flows[-1] += face_value  # Add face value to the last cash flow
    discount_factors = [(1 + interest_rate / frequency) ** -(t+1) for t in range(int(maturity * frequency))]
    price = np.dot(cash_flows, discount_factors)
    return price

# Backtest the portfolio
for t in range(1, time_steps):
    prev_row = portfolio_df.iloc[-1]
    curr_interest_rate = interest_rates[t]
    
    # Calculate current bond prices based on the prevailing interest rate
    curr_bond_price = bond_price(curr_interest_rate, maturity, curr_interest_rate, face_value, coupon_frequency)
    
    # Calculate coupon payments
    coupon_payments = prev_row['Num Bonds'] * curr_interest_rate * face_value / coupon_frequency
    
    # Reinvest coupon payments into new bonds
    new_bonds_bought = int(coupon_payments / curr_bond_price)
    
    # Update number of bonds and portfolio value
    num_bonds = prev_row['Num Bonds'] + new_bonds_bought
    portfolio_value = num_bonds * curr_bond_price
    
    # Append to portfolio DataFrame
    new_row = {
        'Time': t / 2,  # Convert time steps to years
        'Interest Rate': curr_interest_rate,
        'Num Bonds': num_bonds,
        'Portfolio Value': portfolio_value,
        'Coupon Payments': coupon_payments
    }
    portfolio_df = portfolio_df.append(new_row, ignore_index=True)

portfolio_df.head()
# Plot the portfolio performance
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot Portfolio Value
ax1.plot(portfolio_df['Time'], portfolio_df['Portfolio Value'], label='Portfolio Value', color='b')
ax1.set_xlabel('Time (Years)')
ax1.set_ylabel('Portfolio Value (USD)', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.legend(loc='upper left')
ax1.grid(True)

# Create a second y-axis to plot Interest Rates
ax2 = ax1.twinx()
ax2.plot(portfolio_df['Time'], portfolio_df['Interest Rate'], label='Interest Rate', color='g')
ax2.set_ylabel('Interest Rate', color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax2.legend(loc='upper right')

plt.title('Backtest of Bullet Strategy Bond Portfolio')
plt.show()
