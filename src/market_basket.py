import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def prepare_basket(df):
    basket = (df.groupby(['ticket_number', 'article'])['quantity']
                .sum().unstack().fillna(0))
    # Convert to 1/0 for presence
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)
    return basket

def run_market_basket_analysis(df, min_support=0.01, min_confidence=0.3):
    basket = prepare_basket(df)
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=min_confidence)
    return rules.sort_values('lift', ascending=False)

if __name__ == "__main__":
    from preprocessing import load_and_clean_data
    df = load_and_clean_data()
    rules = run_market_basket_analysis(df)
    print(rules.head(10))
