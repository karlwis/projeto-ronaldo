from playwright.sync_api import sync_playwright


def test_home_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            response = page.goto("http://localhost:8000/", wait_until="networkidle")

            assert response is not None
            assert response.status == 200
            assert page.locator("body").text_content() == "Projeto Ronaldo"
        finally:
            browser.close()
