# Job Search Scraper

A small Flask app that scrapes **LinkedIn and Indeed** for a given job title and
location, then extracts contact details (emails and phone numbers) from each job
description so you can reach out directly.

- **Backend**: Flask (Python)
- **Scraping**: [python-jobspy](https://github.com/Bunsly/JobSpy) (LinkedIn, Indeed)
- **Parsing**: regex contact extraction + pandas

## Run it

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python app.py                  # http://localhost:5000
```

Open `http://localhost:5000`, enter a job title and location, and browse
paginated results (10 per page). Each result shows the extracted emails/phones
when present.

## Tests

```bash
pytest -q          # 6 tests
```

The suite covers the pure `extract_contacts` helper (emails, Indian mobile
numbers, combined extraction, dedup, empty/None inputs).

## Notes

- Scraping depends on LinkedIn/Indeed availability; results may be partial.
- Keep `RESULTS_PER_PAGE` small to avoid timeouts (default 10).
- Contact extraction is best-effort regex; verify before reaching out.

## License

MIT — see [LICENSE](LICENSE).
