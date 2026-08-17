import random

def generate_insight(df):
    if df.empty:
        return "No data available for this region."

    top_product = df.groupby("product")["total_sales"].sum().idxmax()
    total = df["total_sales"].sum()
    avg_order = df["total_sales"].mean()

    options = [
        f"💰 Total sales in this region: ${total:.2f}",
        f"🔥 Best-seller: {top_product}",
        f"📦 Average order value: ${avg_order:.2f}"
    ]
    return random.choice(options)
