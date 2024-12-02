from selenium.webdriver.common.by import By


class BasicAuthLocators:
    """
    <input type="button" class="button2 buttonspace" value="Display Image"
    id="displayImage" onclick="document.getElementById('downloadImg').src = GetImageURL();">
    """
    display_image = (By.ID, "displayImage")

    # input_alert = (By.XPATH, '//a[string()="Input Alert"]')
    # iframe = (By.XPATH, '//iframe[@src="alert/input-alert.html"]')
    #
    # input_box = (By.XPATH, '//button[contains(string(), "Input box")]')
    # # input_box = (By.TAG_NAME, 'button')
    #
    # # text = (By.ID, "demo")
    # # message = (By.TAG_NAME, "p")
    # # message = (By.XPATH, "//p[contains(text(),'How are you today?')]")
    # message = (By.XPATH, "/html/body/p")
