import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Product': ['Phone', 'Laptop', 'Phone', 'Laptop', 'Phone', 'Laptop'],
    'Sales': [500, 1000, 600, 1200, 550, 1100]
}

df = pd.DataFrame(data)

print("Our Data:")
print(df)

print("\nTotal Sales by Product:")
result = df.groupby('Product')['Sales'].sum()
print(result)


result.plot(kind='bar')
plt.title('Sales by Product')
plt.show()

print("Done!")