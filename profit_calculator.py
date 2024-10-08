def stock_profile_calculator():
    # Function to get input with a default value
    def get_input(prompt, default):
        user_input = input(prompt)
        return user_input if user_input else default

    # Gather inputs from the user with default values
    stock_symbol = get_input("Ticker Symbol: ", "ADBE")
    allotment = int(get_input("Allotment: ", "100"))
    final_share_price = float(get_input("Final Share Price: ", "110"))
    sell_commission = float(get_input("Sell Commission: ", "15"))
    initial_share_price = float(get_input("Initial Share Price: ", "25"))
    buy_commission = float(get_input("Buy Commission: ", "10"))
    capital_gain_tax_rate = float(get_input("Capital Gain Tax Rate (%): ", "15"))

    # Calculate proceeds
    proceeds = allotment * final_share_price

    # Calculate total purchase price
    total_purchase_price = allotment * initial_share_price

    # Calculate capital gain
    capital_gain = proceeds - total_purchase_price - buy_commission - sell_commission

    # Calculate tax on capital gain
    tax_on_capital_gain = (capital_gain_tax_rate / 100) * capital_gain

    # Calculate total cost
    cost = total_purchase_price + buy_commission + sell_commission + tax_on_capital_gain

    # Calculate net profit
    net_profit = proceeds - cost

    # Calculate return on investment
    roi = (net_profit / cost) * 100

    # Calculate break-even price
    break_even_price = (total_purchase_price + buy_commission + sell_commission) / allotment

    # Output the results
    print("\nPROFIT REPORT:")
    print(f"Proceeds: ${proceeds:,.2f}")
    print(f"Cost: ${cost:,.2f}")
    print("\nCost details:")
    print(f"Total Purchase Price: {allotment} × ${initial_share_price} = ${total_purchase_price:,.2f}")
    print(f"Buy Commission = ${buy_commission:,.2f}")
    print(f"Sell Commission = ${sell_commission:,.2f}")
    print(f"Tax on Capital Gain = {capital_gain_tax_rate}% of ${capital_gain:,.2f} = ${tax_on_capital_gain:,.2f}")
    print(f"\nNet Profit: ${net_profit:,.2f}")
    print(f"Return on Investment: {roi:.2f}%")
    print(f"\nTo break even, you should have a final share price of ${break_even_price:,.2f}")

# Run the calculator
if __name__ == "__main__":
    stock_profile_calculator()
