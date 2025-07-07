import matplotlib.pyplot as plt

def generate_factor_importance(ndvi, rainfall, moisture):
    ndvi_weight = ndvi * 0.4
    rainfall_weight = rainfall * 0.3
    moisture_weight = moisture * 0.3

    factors = ['NDVI', 'Rainfall', 'Soil Moisture']
    values = [ndvi_weight, rainfall_weight, moisture_weight]

    plt.figure(figsize=(6, 4))
    bars = plt.bar(factors, values, color=['green', 'blue', 'brown'])
    plt.title("Factor Importance for Crop Recommendation")
    plt.ylabel("Weighted Influence")
    plt.ylim(0, max(values) + 10)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.2, yval + 1, round(yval, 2))

    plt.tight_layout()
    plt.savefig("static/factor_importance.png")
    plt.close()
