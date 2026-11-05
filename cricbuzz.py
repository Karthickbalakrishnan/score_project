from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Go directly to the Live Scores page to avoid click/navigation race conditions
    page.goto("https://www.cricbuzz.com/cricket-match/live-scores", timeout=60000)
    
    # Use a broad fallback selector that captures match containers on Cricbuzz
    match_selector = "div.cb-mtch-lst, div.cb-lv-scrs-well, div.cb-col-rt"
    
    print("Waiting for match elements...")
    try:
        page.wait_for_selector(match_selector, timeout=10000)
        score = page.locator(match_selector).first.inner_text()
        print("\n--- Live Score ---")
        print(score)
    except Exception:
        print("\nNo specific match card container found, printing page title/main content instead:")
        print(page.title())
        
    page.screenshot(path="score.png")
    print("\nSaved screenshot as score.png")
    browser.close()