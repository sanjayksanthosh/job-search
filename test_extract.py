from app import extract_contacts


def test_none_input_returns_none_pair():
    assert extract_contacts(None) == (None, None)


def test_extracts_email():
    emails, phones = extract_contacts('Contact hr@acme.com for details')
    assert emails == ['hr@acme.com']
    assert phones == []


def test_extracts_indian_mobile():
    emails, phones = extract_contacts('Call 9876543210 today')
    assert '9876543210' in phones


def test_extracts_email_and_phone_together():
    text = 'Reach us at jobs@company.in or +91 98765 43210'
    emails, phones = extract_contacts(text)
    assert 'jobs@company.in' in emails
    assert any('98765' in p for p in phones)


def test_deduplicates():
    text = 'a@b.com and a@b.com again'
    emails, _ = extract_contacts(text)
    assert emails == ['a@b.com']


def test_empty_string():
    assert extract_contacts('') == ([], [])
