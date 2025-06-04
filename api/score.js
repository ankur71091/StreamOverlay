import { chromium } from 'playwright-core';
export default async function handler(req, res) {
 const matchUrl = req.query.url;
 if (!matchUrl) {
   return res.status(400).json({ error: "Missing 'url' query parameter" });
 }
 let browser;
 try {
   browser = await chromium.launch({
     headless: true,
     args: ['--no-sandbox', '--disable-setuid-sandbox'],
   });
   const page = await browser.newPage();
   await page.goto(matchUrl, { waitUntil: 'networkidle', timeout: 60000 });
   await page.waitForSelector('div.BoxStyle__BottomSection-xydo28-3.fTKnqN', { timeout: 10000 });
   const html = await page.$eval('div.BoxStyle__BottomSection-xydo28-3.fTKnqN', el => el.innerHTML);
   res.status(200).send(html);
 } catch (err) {
   res.status(500).json({ error: err.toString() });
 } finally {
   if (browser) await browser.close();
 }
}
