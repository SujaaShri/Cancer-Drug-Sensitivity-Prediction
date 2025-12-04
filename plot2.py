import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("predictions.csv")
errors = np.abs(df["True_IC50"] - df["Predicted_IC50"])
plt.figure(figsize=(6,4))
plt.hist(errors, bins=50, color='lightcoral', edgecolor='black')
plt.xlabel("Absolute Error (|True - Pred|)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Distribution of Absolute Errors — IC50 Prediction", fontsize=14, weight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
