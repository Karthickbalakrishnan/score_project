from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the script...")
print(f"Current date and time: {datetime.now()}")

#Daily weather forecast report generation bot
#chromium -> weather site -> Extract weather data -> Generate report -> Save as PDF
with sync_playwright() as p:
    print("Launching Chromium browser...")
    browser = p.chromium.launch(headless=False)  # Set headless=True for background execution
    page = browser.new_page()
    
    print("Navigating to the weather forecast website...")
    page.goto("https://weather.com/weather/today/l/USNY0996:1:US")  # Example location: New York, NY
    
    print("Extracting weather data...")
    temperature = page.locator('span[data-testid="TemperatureValue"]').inner_text()
    condition = page.locator('div[data-testid="wxPhrase"]').inner_text()
    
    print(f"Current temperature: {temperature}")
    print(f"Weather condition: {condition}")
    
    report_content = f"Weather Report for New York, NY\n\nTemperature: {temperature}\nCondition: {condition}\nGenerated on: {datetime.now()}"
    
    report_filename = "weather_report.txt"
    with open(report_filename, "w") as report_file:
        report_file.write(report_content)
    
    print(f"Weather report saved as {report_filename}")
    
    browser.close()