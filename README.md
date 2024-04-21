# Yellow Pages UAE Scraper

This Python script enables you to scrape business listings from Yellow Pages UAE. It extracts essential details such as business name, telephone number, website, address, and more.

## Features

- **Search by Keyword and Location:** You can specify a keyword and location to search for businesses matching your criteria.
- **Data Extraction:** The script extracts various details about each business, including its rank, name, contact information, website, address, and more.
- **CSV Export:** The scraped data is exported to a CSV file for further analysis or integration with other tools.

## Prerequisites

Make sure you have the following installed:

- Python 3
- Required Python libraries (`requests`, `parsel`, `slugify`, `csv`)

## Usage

1. Clone the repository or download the script `scrape_yellow_pages.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script with the following command:

    ```bash
    python3 scrape_yellow_pages.py <keyword> <location>
    ```

   Replace `<keyword>` with your desired search keyword and `<location>` with the location you want to search in (e.g., "Dubai, UAE").

5. Wait for the script to scrape the data. It will display a message once the process is complete.
6. Find the scraped data in a CSV file named `output_csv_file.csv` in the same directory.

## Example

```bash
python3 scrape_yellow_pages.py restaurants Dubai, UAE
```

This command will search for restaurants in Dubai, UAE, scrape the relevant data, and save it to a CSV file named `output_csv_file.csv`.

## Files

- **scrape_yellow_pages.py:** Python script for scraping Yellow Pages UAE.
- **process_data.py:** Script to process the scraped data, handle missing values, and export it to a CSV file.
- **requirements.txt:** List of required Python libraries.
- **result.csv:** Sample output file containing scraped data.

