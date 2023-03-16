import src.utils as u

class AboutUsLocator:

    abtloc = dict()

    abtloc['Play_Button'] = (u.By.XPATH, '/html/body/div[4]/div/div/div[2]/form/div/div/button')
    abtloc['Pause_Button'] = (u.By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/div[4]/button[1]")
