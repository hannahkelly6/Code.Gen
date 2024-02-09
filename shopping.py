import statistics
import pandas

df = pandas.read_csv('shopping_data.csv')

online_Amt = df['Amt_Online']
print(online_Amt)
InShop_Amt = df['Amt_InShop']
print(InShop_Amt)
SecondHand_Amt = df['Amt_SecondHand']
print(SecondHand_Amt)

mean_value_online = round(statistics.mean(online_Amt), 2)
print("Mean Value Online is ",mean_value_online)