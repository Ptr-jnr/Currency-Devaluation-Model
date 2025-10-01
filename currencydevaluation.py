import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Impact of Currency Devaluation on Zimbabwe's Informal Economy")

# Sidebar inputs
st.sidebar.header("Simulation Settings")
devaluation_rate = st.sidebar.slider("Devaluation Rate (%)", 0, 100, 25) / 100
initial_exchange_rate = st.sidebar.number_input("Initial Exchange Rate (ZWL per USD)", value=13000)
initial_informal_income = st.sidebar.number_input("Initial Informal Monthly Income (ZWL)", value=300000)
formal_job_loss_rate = st.sidebar.slider("Formal Job Loss Rate (%)", 0, 100, 10) / 100
migration_to_informal = st.sidebar.slider("Migration to Informal (%)", 0, 100, 60) / 100

# Zimbabwe-specific inflation coefficients
initial_inflation_rate = 0.15  # 15% monthly
devaluation_pass_through = 0.9  # 90%

# Calculations
new_exchange_rate = initial_exchange_rate * (1 + devaluation_rate)
new_inflation_rate = initial_inflation_rate + (devaluation_pass_through * devaluation_rate)
real_income = initial_informal_income / (1 + new_inflation_rate)

# Demand effect
price_elasticity = -0.4
demand_change = (real_income - initial_informal_income) / initial_informal_income
informal_demand_multiplier = 1 + (price_elasticity * demand_change)

# Labor supply
added_informal_workers = formal_job_loss_rate * migration_to_informal

# Display
st.subheader("Simulation Results")
st.write(f"**New Exchange Rate:** {new_exchange_rate:.2f} ZWL/USD")
st.write(f"**New Inflation Rate:** {new_inflation_rate*100:.2f}%")
st.write(f"**Real Informal Income:** {real_income:,.0f} ZWL")
st.write(f"**Change in Informal Demand:** {informal_demand_multiplier:.2f}x")
st.write(f"**Increase in Informal Labor Supply:** {added_informal_workers*100:.2f}%")

# Visualization
labels = ['Before', 'After']
income_values = [initial_informal_income, real_income]
demand_values = [1, informal_demand_multiplier]
labor_supply = [1, 1 + added_informal_workers]

fig, axs = plt.subplots(1, 3, figsize=(14, 4))
axs[0].bar(labels, income_values, color='skyblue')
axs[0].set_title('Informal Income')

axs[1].bar(labels, demand_values, color='lightgreen')
axs[1].set_title('Informal Demand')

axs[2].bar(labels, labor_supply, color='salmon')
axs[2].set_title('Informal Labor Supply')

for ax in axs:
    ax.set_ylim(0, max(ax.get_yticks()) * 1.2)

st.pyplot(fig)
