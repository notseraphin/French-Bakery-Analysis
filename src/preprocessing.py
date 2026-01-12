import pandas as pd

def load_and_clean_data(path='../data/bakery_sales.csv'):
    # Load CSV
    df = pd.read_csv(path)
    
    # Fix column names
    df.columns = df.columns.str.strip().str.lower()
    
    # Convert date/time
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['time'] = pd.to_datetime(df['time'], format='%H:%M').dt.time
    
    # Clean unit_price (remove € and convert comma to dot)
    df['unit_price'] = df['unit_price'].str.replace('€','').str.replace(',','.').astype(float)
    
    # Convert quantity
    df['quantity'] = df['quantity'].astype(int)
    
    return df

if __name__ == "__main__":
    df = load_and_clean_data()
    print(df.head())
