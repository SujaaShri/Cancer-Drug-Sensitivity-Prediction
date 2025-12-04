import matplotlib.pyplot as plt

# Sample Data
samples = [1, 2, 3, 4, 5, 6, 7, 8]
true_ic50 = [4.4252, 1.6906, -0.5058, 1.5884, 3.2627, 3.0911, 0.0905, 4.6571]
pred_ic50 = [4.6585, 1.9638, 1.5936, 0.4522, 3.5485, 3.4753, -1.1746, 3.2946]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(samples, true_ic50, marker='o', label='True IC50', linewidth=2)
plt.plot(samples, pred_ic50, marker='s', label='Predicted IC50', linewidth=2)

# Labels & Title
plt.title('True vs Predicted IC50 Values', fontsize=14)
plt.xlabel('Sample Number', fontsize=12)
plt.ylabel('IC50 Value', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show plot
plt.show()
