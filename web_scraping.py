import pandas as pd
import os


link="https://en.wikipedia.org/wiki/Forbes_list_of_the_world%27s_highest-paid_athletes"
scraper = pd.read_html(link)
file_name = "Top Paid Players in 2024.csv"

# Create a new folder for the CSV files if it doesn't exist already
folder_name = 'CSV Files'
os.makedirs(folder_name, exist_ok=True)

# Check if the scraper function returned any data
if scraper:
    # # Print the tables retrieved from the webpage
    # for i, table in enumerate(scraper):
    #     print('----------------------------------------------------------------')
    #     print(f'Table {i+1}')
    #     print(table)

    # Select the first table
    df = scraper[0]
    file_path = ".\\"+folder_name+"\\"+file_name
    df.to_csv(file_path, index= False)
    
    print("Data saved successfully in the CSV file:")
    df_scraped_file = pd.read_csv(file_path)
    print(df_scraped_file)