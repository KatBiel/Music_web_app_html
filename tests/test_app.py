import os
from playwright.sync_api import Page, expect

"""
os.environ['APP_ENV'] = 'test'
"""

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.goto(f"http://{test_web_address}/albums")
    li_tag = page.locator("li")
    paragraph_tags = page.locator("p")
    expect(li_tag).to_have_text([
        "Voyage",
        "Surfer Rosa"
        ])

def test_get_index_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.goto(f"http://{test_web_address}/albums/1")
    release_year_tag = page.locator(".t-release-year")
    h1_tags = page.locator("h1")
    
    paragraph_tags = page.locator("p")
    print(paragraph_tags)
    expect(h1_tags).to_have_text([
        "Voyage"
    ])
    expect(release_year_tag).to_have_text([
        "Release year: 2022"
    ])

"""
The page returned by GET/albums should contain a link for each album listed 
It should like to '/albums/<id>', where <id> is the corresponding albums's id
"""
def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tag = page.locator("h1")
    release_year_tag = page.locator(".t-release-year")
    expect(h1_tag).to_have_text("Surfer Rosa")
    expect(release_year_tag).to_have_text("Release year: 1988")

def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.goto(f"http://{test_web_address}/albums/1")
    page.click("text='Back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

def test_create_album(db_connection, page, test_web_address):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.fill("input[name=title]", "Bossanova")
    page.fill("input[name=release_year]", "1990")
    # page.fill("input[name=artist]", "Pixies")
    page.click("text='Add album'")
    h1_tag = page.locator("h1")
    release_year_tag = page.locator(".t-release-year")
    expect(h1_tag).to_have_text("Bossanova")
    expect(release_year_tag).to_have_text("Release year: 1990")

def test_attempt_create_album_with_errors(db_connection, page, test_web_address):
    db_connection.seed('seeds/music_web_app_html.sql')
    os.environ['APP_ENV'] = 'test'
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.click("text='Add album'")
    error_tag = page.locator(".t-errors")
    expect(error_tag).to_have_text("Your submission contains errors: Title can't be blank, Release year can't be blank")