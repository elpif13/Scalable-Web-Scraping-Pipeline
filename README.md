Scalable Web Scraping Pipeline

📌 Overview

This project is a scalable and modular web scraping pipeline developed to extract verified email addresses from company websites listed on the Europages directory. It was built as part of a challenge to demonstrate the ability to design a flexible scraping framework for lead generation.

🚀 Workflow

The pipeline targets a specific sector (e.g., wines) and filters suppliers by supplier type (e.g., producers). The main steps are:

Directory Scraping:
Navigate to the Europages search results.
Extract company names and corresponding detail page links.
Website Extraction:
Visit each company’s detail page.
Retrieve the company's official website URL.
Email Extraction:
Visit each website and attempt to extract valid email addresses from the homepage or linked contact pages.
Data Cleaning and Saving:
Store the structured output in CSV format.
Skip companies with no valid website.
⚠️ Challenges Faced

1. Website Extraction
Some companies did not provide website links on Europages.
Some provided invalid or broken links.
These companies were skipped to maintain data quality and avoid storing None values.
2. Email Extraction
Some websites do not list email addresses at all.
Manual verification confirmed that in some cases, the absence of email was intentional.
Many websites use pop-ups like “Accept Cookies” or age verification gates, which block the content until interacted with.
Some pop-ups were manageable, but others were in foreign languages (e.g., accepto instead of accept), making detection and interaction challenging.
A potential improvement could involve using an LLM to dynamically recognize and handle multi-language pop-ups.
On some websites, email addresses were hidden in subpages like Contact or About Us.
While some of these pages were handled, different language/localization terms for these pages posed an additional barrier.
Again, an LLM could help infer semantically similar navigation options across languages.
🧠 Design Considerations

The codebase is modular and scalable, allowing easy updates and reuse.
Functionality is split into methods for readability and maintenance.
Configuration values are centralized using a config.py file for better flexibility.
🗃️ Output

The final output is a CSV file with the following columns:

A two-part CSV dataset per sector:

1. `links_<sector>.csv` → List of company profile URLs
2. `emails_<sector>.csv` → List of emails with company names and countries (when available)

Companies without valid websites are excluded from the CSV.

🧩 What Could Be Improved

Performance Optimization:
The current implementation works reliably, but performance can be enhanced. Techniques such as asynchronous requests or concurrent scraping with threading or multiprocessing could significantly reduce runtime, especially for large-scale data collection.
Advanced Popup Handling:
Some websites present cookie consent forms or age verification popups in various languages or formats. While some were handled, a more comprehensive and multilingual solution could be developed—potentially by integrating a language-aware Large Language Model (LLM) or using heuristic-based UI interaction patterns.
Better Subpage Detection:
Emails are often hidden in subpages like "Contact", "About Us", or local-language equivalents. While a keyword-based approach was used, some were missed due to language or structural differences. A semantic component recognition system or an LLM-based link predictor could improve this.