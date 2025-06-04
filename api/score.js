import { chromium } from '@sparticuz/chromium';
import playwright from 'playwright-core';
export default async function handler(req, res) {
 const matchUrl = req.query.url;
 if (!matchUrl) {
   return res.status(400).json({ error: "Missing 'url' query parameter" });
 }
 let browser = null;
 try {
   browser = await playwright.chromium.launch({
     args: chromium.args,
     executablePath: await chromium.executablePath,
     headless: chromium.headless,
   });
   const page = await browser.newPage();
   await page.goto(matchUrl, { timeout: 60000 });
   await page.waitForSelector('div.BoxStyle__BottomSection-xydo28-3.fTKnqN', { timeout: 10000 });
   const html = await page.$eval('div.BoxStyle__BottomSection-xydo28-3.fTKnqN', el => el.innerHTML);
   res.status(200).send(html);
 } catch (err) {
   res.status(500).json({ error: err.toString() });
 } finally {
   if (browser !== null) {
     await browser.close();
   }
 }
}
