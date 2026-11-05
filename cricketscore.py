from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def capture_cricbuzz_score():
    with sync_playwright() as p:
        # Start browser in headed mode first as requested
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            print("Connecting to Cricbuzz...")
            page.goto("https://www.cricbuzz.com/", timeout=60000)
            
            # Selector for live match score widgets on Cricbuzz homepage
            # Note: Inspect the page if Cricbuzz updates its DOM structure.
            selector = ".cb-min-st-rw"
            
            print(f"Waiting for live score element ({selector})...")
            page.wait_for_selector(selector, timeout=15000)
            
            # Extract text from all matching live score blocks
            score_elements = page.locator(selector).all_inner_texts()
            
            if score_elements:
                print("\n=== LIVE CRICKET SCORES ===")
                for text in score_elements:
                    print(text.strip())
                    print("-" * 30)
            else:
                print("No active live scores found on the page.")
                
            # Save screenshot
            page.screenshot(path="score.png", full_page=False)
            print("\nsaved score.png successfully!")
            
        except PlaywrightTimeoutError:
            print("\n[Notice] Timed out waiting for live scores. Either no match is currently live, or the selector needs adjustment.")
            page.screenshot(path="score.png")
            print("Saved fallback screenshot as score.png")
            
        finally:
            browser.close()

if __name__ == "__main__":
    capture_cricbuzz_score()