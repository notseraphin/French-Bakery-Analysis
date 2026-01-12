import pandas as pd

def abc_analysis(df):
    """
    Perform ABC classification based on revenue contribution
    """
    # Calculate revenue per article
    df['revenue'] = df['quantity'] * df['unit_price']
    revenue_by_article = df.groupby('article')['revenue'].sum().sort_values(ascending=False)
    
    # Calculate cumulative percentage
    total_revenue = revenue_by_article.sum()
    cumulative_percentage = (revenue_by_article.cumsum() / total_revenue) * 100
    
    # Classify A/B/C
    abc_class = pd.cut(cumulative_percentage, 
                       bins=[0, 80, 95, 100], 
                       labels=['A', 'B', 'C'])
    
    result = pd.DataFrame({
        'revenue': revenue_by_article,
        'cumulative_pct': cumulative_percentage,
        'ABC_class': abc_class
    })
    return result

if __name__ == "__main__":
    from preprocessing import load_and_clean_data
    df = load_and_clean_data()
    abc = abc_analysis(df)
    print(abc.head(10))
