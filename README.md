🚀 Scalable Web Scraping Pipeline

📌 Overview

This project is a modular and scalable web scraping pipeline designed to extract verified email addresses from company websites listed on the Europages directory. It was developed as part of a challenge to showcase the ability to build a flexible, industry-specific lead generation system using intelligent scraping techniques.

🔄 Workflow

The pipeline focuses on a selected sector (e.g., wines) and filters by supplier type (e.g., producers). The steps are:

🧩 1. Directory Scraping
Navigate to Europages search results.
Extract company names and their detail page links.
🌐 2. Website Extraction
Visit each company's profile page.
Retrieve the official website URL if available.
📧 3. Email Extraction
Visit each company’s website.
Extract email addresses from the homepage or relevant subpages (e.g., Contact, About Us).
🧹 4. Data Cleaning & Storage
Clean and validate extracted data.
Store the results in well-structured CSV files.
Skip companies with missing or invalid websites to avoid None values.
⚠️ Challenges Faced

🔗 Website Extraction
Some companies do not provide website links.
Others link to broken or invalid websites.
These entries were skipped to ensure data integrity.
📭 Email Extraction
Some websites do not list email addresses at all — verified manually.
Pop-ups such as cookie consent or age verification gates often block access.
Many pop-ups were in local languages (e.g., "accepto" instead of "accept"), making automation harder.
Handling these systematically would require more sophisticated logic or language models.
Email addresses are often hidden in subpages (Contact, About Us), and their naming varies across languages.
Keyword matching handled some of them, but language-specific variations posed limitations.
🧠 Design Considerations

✅ Modular Design: Logic split across reusable, clear methods.
🔁 Scalable Architecture: Easily extensible for new sectors or directories.
⚙️ Configuration File (config.py): For customizable sector names, filters, and constants.
🧪 Debugging-Friendly: Step-by-step logs and manageable function boundaries.
🗃️ Output Format

Two CSV outputs per sector:

links_<sector>.csv
→ Contains company names and their Europages profile URLs.
emails_<sector>.csv
→ Contains company names, countries, websites, and extracted emails.
Companies without valid websites or emails are excluded from the final CSVs.
🧩 What Could Be Improved

🚅 1. Performance Optimization
Current scraping is sequential and could be sped up using:
Async I/O (aiohttp, asyncio)
Multithreading / Multiprocessing
Particularly useful when scaling to hundreds or thousands of companies.
🧠 2. Smarter Popup Handling
Some websites show pop-ups in different languages or unexpected formats.
A language-aware LLM or customized popup detector could help:
Detect and dismiss consent dialogs, age gates, and modal overlays more reliably.
🔍 3. Robust Subpage Detection
Email addresses are often on pages like "Contact Us", "Über Uns", "Contatti", etc.
Current logic uses keyword matching — but:
Using semantic analysis or an LLM-based classifier could improve accuracy and multilingual support.
