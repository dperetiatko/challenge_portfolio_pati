from pages.base_page import BasePage


class Dashboard(BasePage):
    button_main_page = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    button_players = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    button_language = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    button_sign_out = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    tab_players_count = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div/div[1]"
    tab_matches_count = "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[1]"
    tab_reports_count = "//*[@id='__next']/div[1]/main/div[2]/div[3]/div/div[2]"
    tab_events_count = "//*[@id='__next']/div[1]/main/div[2]/div[4]/div/div[2]/b"
    button_add_player = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    button_contact = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"






