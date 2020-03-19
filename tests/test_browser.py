import pytest
from syncer import sync

from pyppeteer import connect, Browser


@sync
@pytest.mark.usefixtures('browser')
async def test_browser_version(browser: Browser):
    version = await browser.version()
    assert version.startswith('Headless')


@sync
@pytest.mark.usefixtures('browser')
async def test_browser_ua(browser: Browser):
    ua = await browser.userAgent()
    assert 'WebKit' in ua or 'Gecko' in ua


@sync
@pytest.mark.usefixtures('browser')
async def test_browser_target(browser: Browser):
    target = browser.target
    assert target.type == 'browser'


@sync
@pytest.mark.usefixtures('browser')
async def test_browser_process(browser: Browser):
    proc = browser.process
    assert proc.pid


@sync
@pytest.mark.usefixtures('browser')
async def test_browser_remote_process(browser: Browser):
    browser_ws_endpoint = browser.wsEndpoint
    remote_browser = await connect(browserWSEndpoint=browser_ws_endpoint)
    assert remote_browser.process is None
    await remote_browser.disconnect()


@sync
@pytest.mark.usefixtures('browser')
async def test_browser_connected(browser: Browser):
    browser_ws_endpoint = browser.wsEndpoint
    remote_browser = await connect(browserWSEndpoint=browser_ws_endpoint)
    assert remote_browser.isConnected
    await remote_browser.disconnect()
    assert not remote_browser.isConnected
