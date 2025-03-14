import { test, expect } from '@playwright/test';
import { fillTheField, assertCount, completeTask, removeFromList, filterByStatus } from './functions';
import { url } from './variables';


test('test', async ({ page }) => {
  await page.goto(url);
  await fillTheField(page, 'Get thing 1 done');
  await fillTheField(page, 'Get thing 2 done');
  await fillTheField(page, 'Get thing 3 done');
  await assertCount(page, 3);
  await completeTask(page, 'Get thing 1 done');
  await completeTask(page, 'Get thing 3 done');
  await filterByStatus(page, 'Active');
  await assertCount(page, 1);
  await filterByStatus(page, 'Completed');
  await assertCount(page, 2);
  await filterByStatus(page, 'All');
  await assertCount(page, 3);
  await removeFromList(page, 'Get thing 1 done');
  await assertCount(page, 2);
  await removeFromList(page, 'Get thing 3 done');
  await assertCount(page, 1);
});
