import { test, expect } from '@playwright/test';
import { Page } from '@playwright/test';

export async function fillTheField(page: Page, text: string) {
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill(text);
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
}
  
export async function assertCount(page: Page, count: number) {
  await expect(page.getByTestId('todo-title')).toHaveCount(count);
}

export async function completeTask(page: Page, text: string) {
  await page.getByRole('listitem').filter({ hasText: text }).getByLabel('Toggle Todo').check();
}

export async function removeFromList(page: Page, text: string) {
  await page.getByRole('listitem').filter({ hasText: text }).hover();
  await page.getByRole('listitem').filter({ hasText: text }).getByRole('button', { name: 'Delete' }).click();
}

export async function filterByStatus(page: Page, status: string) {
  await page.getByRole('link', { name: status }).click();
}