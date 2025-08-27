# hexyweb 🕸️

A simple desktop application for scraping websites, built with Python and Tkinter.

--- LINKS ---
https://www.iana.org/domains/example

--- HEADINGS ---
Example Domain

--- PARAGRAPHS ---
This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.
More information...

---

## Features

-   **Scrape Content:** Easily extract all links, headings (H1-H6), and paragraphs from any website.
-   **User-Friendly Interface:** A clean and simple GUI that is easy to navigate.
-   **Export to TXT:** Save your scraped results to a `.txt` file with a single click.
-   **Standalone Application:** No need to install Python or any libraries. Just download and run the `.exe`!

---

## How to Use

1.  **Download the Application:**
    -   Go to the [**Releases**](https://github.com/pbharatchandra/HeXyWeB/releases) page of this repository.
    -   Under the latest release, download the `hexyweb.exe` file.

2.  **Run the Application:**
    -   Double-click the `hexyweb.exe` file.
    -   If Windows shows a security warning, click **"More info"** and then **"Run anyway"**.

3.  **Scrape a Website:**
    -   Enter the full URL of the website you want to scrape (e.g., `https://example.com`).
    -   Click the **"Scrape Website"** button.
    -   The results will appear in the text box.

4.  **Export the Results:**
    -   Click the **"Export to TXT"** button.
    -   Choose a location on your computer to save the results as a text file.

---

## Development

Interested in running the project from the source code? Here's how:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/pbharatchandra/HeXyWeB.git](https://github.com/pbharatchandra/HeXyWeB.git)
    cd HeXyWeB
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install requests beautifulsoup4
    ```

4.  **Run the script:**
    ```bash
    python scrap.py
    ```
````
