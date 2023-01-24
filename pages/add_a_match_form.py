from pages.base_page import BasePage


class MatchForm(BasePage):
    field_my_team = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    field_enemy_team = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    field_my_team_score = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    field_my_enemy_team_score = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    field_t_shirt_color = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    field_league = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div/input"
    time_played = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    number = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    general = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    rating = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
