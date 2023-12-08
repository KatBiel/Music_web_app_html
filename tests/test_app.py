import os
from playwright.sync_api import Page, expect

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Voyage",
        "Surfer Rosa"
        ])
    expect(paragraph_tags).to_have_text([
        "Released: 2022",
        "Released: 1988"
        ])

def test_get_fist_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    paragraph_tags = page.locator("p")
    print(paragraph_tags)
    expect(h1_tags).to_have_text([
        "Voyage"
    ])
    expect(paragraph_tags).to_have_text([
        "Release year: 2022",
        "Artist: Pixies"
    ])