from unittest import IsolatedAsyncioTestCase
import httpx as httpx

BASE_URL = 'https://python.astrotech.io'


async def request(method='GET', path='/', data=None):
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        return await client.request(method=method, url=path, data=data)


class PyBookTest(IsolatedAsyncioTestCase):
    async def test_index(self):
        resp = await request('GET', '/index.html')
        self.assertEqual(resp.status_code, 200)

    async def test_license(self):
        resp = await request('GET', '/LICENSE.html')
        self.assertEqual(resp.status_code, 200)
        text = 'Creative Commons Attribution-ShareAlike 4.0 International Public License'
        self.assertIn(text, resp.text)

    async def test_install(self):
        resp = await request('GET', '/install.html')
        self.assertEqual(resp.status_code, 200)

        with self.subTest(msg='Python Version'):
            self.assertIn('3.11', resp.text)
            self.assertIn('3.10', resp.text)
            self.assertIn('3.9', resp.text)
            self.assertNotIn('3.8', resp.text)
            self.assertNotIn('3.7', resp.text)
            self.assertNotIn('3.6', resp.text)

        with self.subTest(msg='PyCharm Version'):
            self.assertIn('2022.3', resp.text)
            self.assertIn('2022.2', resp.text)
            self.assertIn('2022.1', resp.text)
            self.assertNotIn('2021.3', resp.text)
            self.assertNotIn('2021.2', resp.text)
            self.assertNotIn('2021.1', resp.text)

        with self.subTest(msg='Git Version'):
            self.assertIn('2.33', resp.text)
