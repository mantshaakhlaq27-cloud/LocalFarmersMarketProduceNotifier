import pandas as pd
import numpy as np

# Create the final, extensive dictionary with 113 items
data = {
    'produce_name': [
        # Vegetables (35 items)
        'Tomato', 'Potato', 'Onion', 'Carrot', 'Spinach (Palak)', 'Cauliflower (Gobi)', 'Cabbage (Patta Gobi)',
        'Cucumber (Kheera)', 'Bell Pepper (Shimla Mirch)', 'Okra (Bhindi)', 'Bottle Gourd (Lauki)', 'Brinjal (Baingan)',
        'Ginger (Adrak)', 'Garlic (Lehsun)', 'Green Chilli (Hari Mirch)', 'Radish (Mooli)', 'Peas (Matar)',
        'Pumpkin (Kaddu)', 'Bitter Gourd (Karela)', 'Beetroot', 'Sweet Potato (Shakarkandi)', 'Broccoli',
        'Zucchini', 'Mushroom', 'French Beans', 'Ridge Gourd (Tori)', 'Tinda', 'Corn', 'Lettuce',
        'Leek', 'Turnip (Shalgam)', 'Ash Gourd (Petha)', 'Cluster Beans (Gawar)', 'Celery', 'Asparagus',
        # Fruits (25 items)
        'Mango', 'Apple', 'Banana', 'Orange', 'Watermelon', 'Grapes', 'Pomegranate', 'Guava', 'Papaya',
        'Pineapple', 'Lychee', 'Muskmelon (Kharbuja)', 'Chikoo', 'Kiwi', 'Strawberry', 'Cherry', 'Pear', 'Plum',
        'Blueberry', 'Raspberry', 'Peach', 'Apricot', 'Fig (Anjeer)', 'Coconut', 'Avocado',
        # Pulses (Dals) (10 items)
        'Toor Dal (Arhar)', 'Chana Dal', 'Moong Dal', 'Masoor Dal', 'Urad Dal', 'Kidney Beans (Rajma)',
        'Chickpeas (Kabuli Chana)', 'Black Eyed Peas (Lobia)', 'Soya Beans', 'Horse Gram (Kulthi)',
        # Cereals & Grains (10 items)
        'Basmati Rice', 'Brown Rice', 'Wheat Flour (Atta)', 'Millet (Bajra)', 'Sorghum (Jowar)', 'Oats',
        'Quinoa', 'Semolina (Suji)', 'Barley (Jau)', 'Buckwheat (Kuttu)',
        # Herbs & Spices (15 items)
        'Coriander Leaves (Dhania)', 'Mint Leaves (Pudina)', 'Curry Leaves', 'Turmeric (Haldi)',
        'Cumin Seeds (Jeera)', 'Mustard Seeds (Sarson)', 'Black Pepper (Kali Mirch)', 'Cinnamon (Dalchini)',
        'Cardamom (Elaichi)', 'Cloves (Laung)', 'Fenugreek Seeds (Methi Dana)', 'Bay Leaf', 'Asafoetida (Hing)',
        'Saffron (Kesar)', 'Basil (Tulsi)',
        # Nuts & Seeds (10 items)
        'Peanuts', 'Cashew Nuts', 'Almonds', 'Walnuts', 'Pistachios', 'Dates', 'Flax Seeds',
        'Sesame Seeds', 'Sunflower Seeds', 'Chia Seeds',
        # Dairy & Farm (8 items)
        'Cow Milk', 'Buffalo Milk', 'Yogurt (Dahi)', 'Paneer', 'White Eggs', 'Brown Eggs', 'Ghee', 'Butter'
    ],
    'category': (
        ['Vegetable'] * 35 + ['Fruit'] * 25 + ['Pulse'] * 10 + ['Cereal'] * 10 +
        ['Herb & Spice'] * 15 + ['Nut & Seed'] * 10 + ['Dairy & Farm'] * 8
    ),
    'season': (
        ['All-Year'] * 113
    )
}

# --- Data Generation for other columns ---
num_items = len(data['produce_name'])
data['is_available'] = np.random.choice([True, False], size=num_items, p=[0.8, 0.2])
prices = {
    'Vegetable': np.random.randint(30, 150, size=num_items), 'Fruit': np.random.randint(80, 250, size=num_items),
    'Pulse': np.random.randint(120, 200, size=num_items), 'Cereal': np.random.randint(50, 180, size=num_items),
    'Herb & Spice': np.random.randint(20, 500, size=num_items), 'Nut & Seed': np.random.randint(100, 1200, size=num_items),
    'Dairy & Farm': np.random.randint(50, 700, size=num_items)
}
data['price_per_unit'] = [prices[cat][i] for i, cat in enumerate(data['category'])]
vendors = [
    'Green Farms', 'Village Fresh', 'Himalayan Organics', 'Fresh Veggies',
    'Ratnagiri Fruits', 'Punjab Grains Co.', 'Healthy Pulses', 'Organic Roots', 'Dairy Delights'
]
data['vendor'] = np.random.choice(vendors, size=num_items)

# --- DataFrame Creation ---
market_df = pd.DataFrame(data)
market_df.loc[market_df['is_available'] == False, 'price_per_unit'] = 0
market_df.to_csv('market_data.csv', index=False)

print(f"✅ Success! Your dataset has been created and saved to market_data.csv.")
print(f"Total items in dataset: {len(market_df)}")

# --- Display the first 5 rows as a sample ---
print("\nDisplaying a sample of the market dataset:")
print(market_df.head())