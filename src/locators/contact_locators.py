from src import utils as u


class ContactLocator:
    def __init__(self):
        locContact = dict()

        # Contact fields
        locContact['Contact_Email_fld'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[1]/input")
        locContact['Contact_Name_fld'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[2]/input")
        locContact['Message_fld'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[3]/textarea")

        # Contact buttons
        locContact['X_btn'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[1]/button/span")
        locContact['Close_btn'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[3]/button[1]")
        locContact['Send_Message_btn'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")
