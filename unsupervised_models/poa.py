import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('../Analytics_data.csv')

columns = ["Date", "Agent name", "Response", "uid", "Converted?", 
           "average payment delay before weekly", "revenue per day before weekly", "revenue per day after weekly"]

df = pd.DataFrame(data, columns=columns)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Date'].dropna(inplace=True)
df['Date'] = df['Date'].astype('datetime64[ns]')

# Calculate additional metrics
df['Revenue per day standard'] = 1500 / 30
df['Revenue per day with delay'] = df['revenue per day before weekly'] / (30 + df['average payment delay before weekly'])

# Streamlit app
st.title('Poa! Internet Subscription Pilot Analysis')

# Question 1: Analyze customer conversion, reachability, and agent performance
st.header('Question 1: Customer Conversion, Reachability, and Agent Performance')

# Conversion analysis
converted_customers = df[df['Converted?'] == 'Yes']
conversion_rate = len(converted_customers) / len(df) * 100

st.subheader('Conversion Analysis')
st.write(f"Total Number of Customers: {len(df)}")
st.write(f"Number of Converted Customers: {len(converted_customers)}")
st.write(f"Conversion Rate: {conversion_rate:.2f}%")

# Conversion trends over time
st.line_chart(df.set_index('Date')['Converted?'].eq('Yes').resample('M').mean())

# Reachability analysis by day of week
st.subheader('Reachability Analysis by Day of Week')
df['Day of Week'] = df['Date'].dt.day_name()
reachability_by_day = df.groupby('Day of Week')['Response'].value_counts().unstack().fillna(0)
st.bar_chart(reachability_by_day)

# Agent performance analysis
st.subheader('Agent Performance Analysis')
agent_performance = df.groupby('Agent name')['Converted?'].value_counts().unstack().fillna(0)
st.bar_chart(agent_performance)

# Findings
st.subheader('Findings')
st.write("1. **Conversion Rate Trends:** The conversion rate has been fluctuating over time. Further investigation is needed to understand the factors influencing these fluctuations.")
st.write("2. **Reachability Insights:** Customers are most reachable on specific days of the week. Consider optimizing the calling schedule based on this information.")
st.write("3. **Agent Performance:** Some agents show higher conversion rates than others. Identify and share best practices among agents for better overall performance.")

# Question 2: Uncover any other metrics
st.header('Question 2: Other Metrics')

# Additional metrics analysis
average_delay_by_agent = df.groupby('Agent name')['average payment delay before weekly'].mean()
st.bar_chart(average_delay_by_agent)

# Revenue analysis
st.subheader('Revenue Analysis')

# Revenue per day comparison
plt.figure(figsize=(10, 6))
sns.violinplot(x='Converted?', y='Revenue per day with delay', data=df)
plt.title('Revenue per Day Comparison')
fig, ax = plt.subplots()
st.pyplot(fig)


# Payment delay distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['average payment delay before weekly'], bins=20, kde=True)
plt.title('Payment Delay Distribution')
fig, ax = plt.subplots()
st.pyplot(fig)
# Question 3: Data Story and Recommendations
st.header('Question 3: Data Summary and Recommendations')

# Data story and recommendations
st.subheader('Data Story')

# Summary statistics
summary_stats = df.describe()
st.write(summary_stats)

# Recommendations
st.subheader('Recommendations')
st.write("- Continue offering flexible plans to customers with 1 to 7 days average payment delay.")
st.write("- Investigate reasons for low conversion rates on specific days.")
st.write("- Recognize and reward high-performing agents.")

# Explore further
st.subheader('Explore Further')
st.write("- Conduct customer surveys to understand reasons for plan declines.")
st.write("- Evaluate the impact of the periodic billing pilot on overall customer satisfaction.")


st.subheader('Poa Pilot project Data')
st.dataframe(df)


