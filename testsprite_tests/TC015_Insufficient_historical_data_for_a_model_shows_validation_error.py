import asyncio
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",         # Set the browser window size
                "--disable-dev-shm-usage",        # Avoid using /dev/shm which can cause issues in containers
                "--ipc=host",                     # Use host-level IPC for better stability
                "--single-process"                # Run the browser in a single process mode
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        context.set_default_timeout(5000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> Navigate to http://localhost:8501/
        await page.goto("http://localhost:8501/")
        
        # -> Click the '🚀  Load & Analyze' button to load historical data for BTC-USD so the Forecast tab and model options appear.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div/div/div/div/div/section/div/div[2]/div/div/div[11]/div/button').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Click the '🔮 Forecast' tab to reveal forecast model options and related controls.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div/div/div/div/div/div/section/div/div/div[4]/div/div/div/button[5]').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Open the Time Settings period dropdown to set a very small historical window (e.g., 7d).
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div/div/div/div/div/section/div/div[2]/div/div/div[8]/div/div/div/div/div/div/div/div/div[2]/input').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Select the smallest available historical period (3mo) from the Period dropdown to create a reduced historical window.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div/div[2]/div/div/div/div/div/div/ul/div/div/li').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Click the '▶ Run Forecast' button and wait for the app to respond, then inspect the page for an insufficient-data validation error message.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div/div/div/div/div/div/section/div/div/div[4]/div/div[7]/div/div[3]/div/div[2]/div/div/div/button').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # --> Assertions to verify final state
        frame = context.pages[-1]
        assert await frame.locator("xpath=//*[contains(., 'Insufficient data')]").nth(0).is_visible(), "The app should display an 'Insufficient data' validation error because the selected forecasting model requires more historical data."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    