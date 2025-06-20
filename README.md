# 🚀 Scalable Web Scraping Pipeline

## 📌 Overview

This project is a **modular and scalable web scraping pipeline** designed to extract **verified email addresses** from company websites listed on the Europages directory.  
It was developed as part of a challenge to showcase the ability to build a flexible, industry-specific lead generation system using intelligent scraping techniques.

---

## 🔄 Workflow

The pipeline focuses on a selected **sector** (e.g., `wines`) and filters by **supplier type** (e.g., `producers`). The scraping process includes the following steps:

### 🧩 1. Directory Scraping
- Navigate to the Europages search results.
- Extract company names and their detail page links.

### 🌐 2. Website Extraction
- Visit each company’s profile page.
- Retrieve the official website URL if available.

### 📧 3. Email Extraction
- Visit each company’s website.
- Extract email addresses from the homepage or relevant subpages (e.g., `Contact`, `About Us`).

### 🧹 4. Data Cleaning & Storage
- Clean and validate extracted data.
- Store the results in well-structured CSV files.
- Skip companies with missing or invalid websites to avoid `None` values.

---

## ⚠️ Challenges Faced

### 🔗 Website Extraction
- Some companies do not provide website links.
- Others link to broken or invalid websites.
- These entries were skipped to ensure data integrity.

### 📭 Email Extraction
- Some websites do not list email addresses at all — verified manually.
- Pop-ups such as cookie consent or age verification gates often block access.
- Many pop-ups were in local languages (e.g., `"accepto"` instead of `"accept"`), making automation harder.
- Email addresses are often hidden in subpages (`Contact`, `About Us`), and their naming varies across languages.
- Handling these systematically would require more sophisticated logic or language models (LLMs).

---

## 🧠 Design Considerations

- ✅ **Modular Design**: Logic split across reusable, clear methods.
- 🔁 **Scalable Architecture**: Easily extensible for new sectors or directories.
- ⚙️ **Configuration File** (`config.py`): Centralizes sector names, filters, and constants.
- 🧪 **Debugging-Friendly**: Step-by-step logs and manageable function boundaries.

---

## 🗃️ Output Format

Two CSV outputs per sector:

- `links_<sector>.csv` → Contains company names and their website URLs.
- `emails_<sector>.csv` → Contains company names, countries, and extracted emails.

> Companies without valid **websites** are excluded from the final CSVs.

---

## 🧩 What Could Be Improved

### 🚅 1. Performance Optimization
- The current scraping logic is sequential.
- Could be enhanced using:
  - Asynchronous I/O (`aiohttp`, `asyncio`)
  - Multithreading or multiprocessing
- Especially helpful when scaling to scrape thousands of companies.

### 🧠 2. Smarter Popup Handling
- Some websites display pop-ups in various languages or formats.
- A language-aware LLM or a custom popup detector could:
  - Automatically detect and close cookie consent, age verification, or modal overlays.

### 🔍 3. Robust Subpage Detection
- Emails are often located on subpages like `"Contact Us"`, `"Über Uns"`, `"Contatti"`, etc.
- Current approach uses keyword matching.
- A semantic component recognition system or LLM-based classifier could improve multilingual accuracy.

---
