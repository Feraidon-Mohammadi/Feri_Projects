# Re-establishing the variables and performing the calculations
import pandas as pd

# Defining the constants based on the provided information
papers_per_week = 5
paper_cost_per_sheet = 0.10
scanner_cost_per_week = 0.50
instructor_cost_per_hour = 20
staff_cost_per_hour = 20
data_transmission_cost_per_week = 7.00
number_of_external_instructors = 10
number_of_iad_staff = 2
weeks_per_month = 4  # Average number of weeks per month

# Calculating the costs before the project implementation
weekly_paper_cost1 = papers_per_week * paper_cost_per_sheet * number_of_external_instructors
weekly_scanner_cost1 = scanner_cost_per_week * number_of_external_instructors
weekly_instructor_time_cost1 = (7 / 60) * instructor_cost_per_hour * number_of_external_instructors
weekly_iad_staff_time_cost1 = (7 / 60) * staff_cost_per_hour * number_of_iad_staff
weekly_data_transmission_cost1 = data_transmission_cost_per_week * number_of_external_instructors

# Calculating monthly costs based on the weekly costs
monthly_paper_cost = weekly_paper_cost1 * weeks_per_month
monthly_scanner_cost = weekly_scanner_cost1 * weeks_per_month
monthly_instructor_time_cost = weekly_instructor_time_cost1 * weeks_per_month
monthly_iad_staff_time_cost = weekly_iad_staff_time_cost1 * weeks_per_month
monthly_data_transmission_cost = weekly_data_transmission_cost1* weeks_per_month

# Summing all monthly costs
total_monthly_costs = (monthly_paper_cost + monthly_scanner_cost + monthly_instructor_time_cost +
                       monthly_iad_staff_time_cost + monthly_data_transmission_cost)

# The project implementation should reduce these costs to zero
monthly_savings = total_monthly_costs  # Monthly savings due to project implementation

# Daily savings are the monthly savings divided by the average number of working days in a month
average_work_days_per_month = 20  # Assuming 5 work days per week
daily_savings = monthly_savings / average_work_days_per_month

# Creating a DataFrame to display the information
savings_table = pd.DataFrame({
    "Cost Type": [
        "Paper (monthly)", "Scanner (monthly)", "Instructor Time (monthly)",
        "IAD Staff Time (monthly)", "Data Transmission (monthly)", "Total Monthly Savings", "Total Daily Savings"
    ],
    "Cost Before Project (€)": [
        monthly_paper_cost, monthly_scanner_cost, monthly_instructor_time_cost,
        monthly_iad_staff_time_cost, monthly_data_transmission_cost, total_monthly_costs, daily_savings
    ],
    "Cost After Project (€)": [
        0, 0, 0, 0, 0, 0, 0
    ],
    "Savings (€)": [
        monthly_paper_cost, monthly_scanner_cost, monthly_instructor_time_cost,
        monthly_iad_staff_time_cost, monthly_data_transmission_cost, monthly_savings, daily_savings
    ]
})

savings_table
print(savings_table)


print()

