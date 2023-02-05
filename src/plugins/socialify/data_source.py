from os import getcwd

from aiohttp import ClientSession
from nonebot_plugin_htmlrender import get_new_page
from playwright.async_api import FloatRect, Page


def parse_dict(d: dict):
    for k, v in d.copy().items():
        if v is None or v is False:
            d.pop(k)
        if v is True:
            d[k] = 1
    return d


async def get_cover(repo, **kwargs):
    async with ClientSession() as s:
        async with s.get(
            f"https://socialify.git.ci/{repo}/image",
            params=parse_dict(
                {
                    "description": kwargs.get("description", 1),
                    "descriptionEditable": kwargs.get("descriptionEditable", None),
                    "font": kwargs.get("font", None),
                    "forks": kwargs.get("forks", 1),
                    "issues": kwargs.get("issues", 1),
                    "language": kwargs.get("language", 1),
                    "logo": kwargs.get("logo", None),
                    "name": kwargs.get("name", 1),
                    "owner": kwargs.get("owner", 1),
                    "pattern": kwargs.get("pattern", None),
                    "pulls": kwargs.get("pulls", 1),
                    "stargazers": kwargs.get("stargazers", 1),
                    "theme": kwargs.get("theme", None),
                }
            ),
        ) as resp:
            if resp.status != 200:
                raise Exception(await resp.text())
            ret = await resp.text()

    async with get_new_page() as page:  # type: Page
        zoom = 2.0

        await page.goto(f"file://{getcwd()}")
        await page.set_content(ret, wait_until="networkidle")
        svg = page.locator("svg")
        view_box = [
            int(x) * zoom for x in (await svg.get_attribute("viewBox")).split(" ")
        ]
        await page.evaluate(
            f"document.getElementsByTagName('svg')[0].style.zoom={zoom};"
        )
        img = await page.screenshot(
            clip=FloatRect(x=8, y=8, width=view_box[2], height=view_box[3])
        )

    return img
