from playwright.sync_api import sync_playwright


def test_admin_redirects_unauthenticated_user_to_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            response = page.goto(
                "http://localhost:8000/admin/",
                wait_until="domcontentloaded",
            )

            assert response is not None
            assert response.status == 200
            assert page.url.endswith("/admin/login/?next=/admin/")
            assert page.locator("#id_username").is_visible()
            assert page.locator("#id_password").is_visible()
        finally:
            browser.close()
