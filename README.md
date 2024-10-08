
# Stock Profile Calculator

This Python program calculates key financial metrics related to stock trading based on user-provided inputs.

## Inputs

The program will prompt you to enter the following details:

- **Stock Symbol**: The ticker symbol of the stock.
- **Allotment**: The number of shares you are purchasing or selling.
- **Final Share Price**: The price at which the shares will be sold (in dollars).
- **Sell Commission**: The commission charged for selling the shares (in dollars).
- **Initial Share Price**: The price at which the shares were initially purchased (in dollars).
- **Buy Commission**: The commission charged for buying the shares (in dollars).
- **Capital Gain Tax Rate**: The tax rate applied to capital gains (in %).

## Outputs

After computation, the program will provide the following financial metrics:

- **Proceeds**: The total amount received from selling the shares, calculated as `Allotment x Final Share Price`.
- **Cost**: The total cost incurred, calculated as `Allotment x Initial Share Price + Commissions + Tax on Capital Gain`.
- **Net Profit**: The profit made from the transaction (in dollars).
- **Return on Investment (ROI)**: The return on investment expressed as a percentage.
- **Break-even Price**: The price per share at which no profit or loss is incurred (in dollars).

This program aims to help users evaluate their stock trading decisions effectively.
