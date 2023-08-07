import os

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

user_login = "tpotestmd@gmail.com"
user_password = "asjdhkasjdhka"

def test_case2():
# Авторизация
    capabilities = DesiredCapabilities.CHROME.copy();
    capabilities["pageLoadStrategy"] = "eager"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=capabilities, chrome_options=options)
    driver.get('https://www.youtube.com/')
    prevUrl = driver.current_url
    WebDriverWait(driver, timeout=60).until(EC.presence_of_element_located((By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button")))
    autorizeButton = driver.find_element(By.XPATH,
                                       "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button")
    autorizeButton.click()
    WebDriverWait(driver, timeout=300).until(EC.url_changes(prevUrl))

# Логин
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
    inputLogin = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    inputLogin.send_keys(user_login)
    prevUrl = driver.current_url
    submitLogin = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    submitLogin.click()
    WebDriverWait(driver, timeout=300).until(EC.url_changes(prevUrl))

# Пароль
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div")))
    inputPassword = driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    inputPassword.send_keys(user_password)
    prevUrl = driver.current_url
    WebDriverWait(driver, timeout=60).until(
        EC.visibility_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")))
    sleep(1)
    submitPassword = driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    submitPassword.click()
    WebDriverWait(driver, timeout=300).until(EC.url_changes(prevUrl))

# Шаг 1
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-entry-renderer[2]/a/tp-yt-paper-item/yt-formatted-string")))
    videosButton = driver.find_element(By.XPATH,
                                       "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-entry-renderer[2]/a/tp-yt-paper-item/yt-formatted-string")
    prevUrl = driver.current_url
    window_before = driver.window_handles[0]
    videosButton.click()
    sleep(1)
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)


    WebDriverWait(driver, timeout=60).until(
        EC.visibility_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main")))
    videosTable = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main")
    assert videosTable.is_displayed() == True # Наличие таблицы видео

    rowVideo = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/div[1]/ytcp-table-header/div[2]/h3/span")
    assert rowVideo.get_attribute("class") == "style-scope ytcp-table-header"  # Наличие столбца "Видео"

    rowAccess = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/div[1]/ytcp-table-header/div[3]/h3/span")
    assert rowAccess.get_attribute("class") == "style-scope ytcp-table-header" # Наличие столбца "Доступ"

    rowRestrictions = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/div[1]/ytcp-table-header/div[4]/h3/span")
    assert rowRestrictions.get_attribute("class") == "style-scope ytcp-table-header"  # Наличие столбца "Ограничения"

    rowViews = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/div[1]/ytcp-table-header/div[6]/h3/ytcp-ve/button/span")
    assert rowViews.get_attribute("class") == "style-scope ytcp-table-header"  # Наличие столбца "Просмотры"

    rowComments = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/div[1]/ytcp-table-header/div[7]/h3/span")
    assert rowComments.get_attribute("class") == "style-scope ytcp-table-header"  # Наличие столбца "Количество комментариев"

    rowLikes = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/div[1]/ytcp-table-header/div[8]/h3/span")
    assert rowLikes.get_attribute("class") == "style-scope ytcp-table-header"  # Наличие столбца "Количество отметок 'Нравится'"

    iconVideo = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[1]/div/div[2]/ytcp-video-list-cell-video/div[1]/a/div/ytcp-thumbnail/div/ytcp-img-with-fallback/div")
    assert iconVideo.is_displayed() == True # Наличие иконки видео

    titleVideo = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[1]/div/div[2]/ytcp-video-list-cell-video/div[2]/h3")
    assert titleVideo.is_displayed() == True # Наличие названия видео

    descriptionVideo = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[1]/div/div[2]/ytcp-video-list-cell-video/div[2]/div")
    assert descriptionVideo.is_displayed() == True # Наличие описания видео


# Шаг 2
    assert titleVideo.is_displayed() == True  # Наличие названия видео
    assert descriptionVideo.is_displayed() == True  # Наличие описания видео
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[1]/div/div[4]/div")))
    cellVideo = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[1]/div/div[4]/div")

    hov = ActionChains(driver).move_to_element(cellVideo)
    hov.perform()


    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[1]/ytcp-icon-button")))
    buttonWithIconDetails = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[1]/ytcp-icon-button")
    assert buttonWithIconDetails.is_displayed() == True

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[2]/ytcp-icon-button")))
    buttonWithIconAnalytics = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[2]/ytcp-icon-button")
    assert buttonWithIconAnalytics.is_displayed() == True

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[3]/ytcp-icon-button")))
    buttonWithIconComments = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[3]/ytcp-icon-button")
    assert buttonWithIconComments.is_displayed() == True

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[4]/ytcp-icon-button")))
    buttonWithIconYoutube = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/a[4]/ytcp-icon-button")
    assert buttonWithIconYoutube.is_displayed() == True

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/ytcp-icon-button")))
    buttonWithIconOptions = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[2]/ytcp-icon-button")
    assert buttonWithIconOptions.is_displayed() == True
    sleep(1)


# Шаг 3
    hov = ActionChains(driver).move_to_element(buttonWithIconDetails)
    hov.perform()
    assert buttonWithIconDetails.get_attribute("tooltip-label") == "Сведения"  # Всплывающая подсказка с текстом "Сведения"
    sleep(1)


# Шаг 4
    prevUrl = driver.current_url
    buttonWithIconDetails.click()
    WebDriverWait(driver, timeout=300).until(EC.url_changes(prevUrl))
    sleep(1)
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-sticky-header/ytcp-entity-page-header/div/div[1]/h1")))
    videoDetailsText = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-sticky-header/ytcp-entity-page-header/div/div[1]/h1")
    assert videoDetailsText.text == "Сведения о видео"  # Наличие названия настройки "Сведения о видео"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")))
    editTitleVideo = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
    assert editTitleVideo.is_displayed() == True  # Наличие поля для изменения названия видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")))
    editDescriptionVideo = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
    assert editDescriptionVideo.is_displayed() == True  # Наличие поля для изменения описания видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]")))
    editThumbnailVideo = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]")
    assert editThumbnailVideo.is_displayed() == True  # Наличие поля для изменения значка видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[4]")))
    editPlaylistVideo = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[4]")
    assert editPlaylistVideo.is_displayed() == True  # Наличие поля для изменения плейлиста видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]")))
    editAudienceVideo = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]")
    assert editAudienceVideo.is_displayed() == True  # Наличие поля для изменения аудитории видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-video-info/div")))
    videoInfo = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-video-info/div")
    assert videoInfo.is_displayed() == True  # Наличие сведений о видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/div/ytcp-video-metadata-visibility/div")))
    paramAccess = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/div/ytcp-video-metadata-visibility/div")
    assert paramAccess.is_displayed() == True  # Наличие параметра доступа видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-video-metadata-restrictions/div")))
    paramRestrictions = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-video-metadata-restrictions/div")
    assert paramRestrictions.is_displayed() == True  # Наличие отображения ограничений видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-text-dropdown-trigger[2]/ytcp-dropdown-trigger")))
    paramAnScreen = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-text-dropdown-trigger[2]/ytcp-dropdown-trigger")
    assert paramAnScreen.is_displayed() == True  # Наличие параметра конечной заставки видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-text-dropdown-trigger[3]/ytcp-dropdown-trigger/div/div[2]/span")))
    paramCards = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-text-dropdown-trigger[3]/ytcp-dropdown-trigger/div/div[2]/span")
    assert paramCards.is_displayed() == True  # Наличие параметра подсказок видео


# Шаг 5
    paramAccess.click()
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog")))
    modalEditAccess = driver.find_element(By.XPATH,
                             "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog")
    assert modalEditAccess.is_displayed() == True  # Наличие модального окна для изменения доступа к видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-button")))
    selectSaveOrPublish = driver.find_element(By.XPATH,
                             "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-button")
    assert selectSaveOrPublish.is_displayed() == True  # Наличие выбора "Сохранить и опубликовать"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-button")))
    selectSchedule = driver.find_element(By.XPATH,
                             "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-button")
    assert selectSchedule.is_displayed() == True  # Наличие выбора "Запланировать публикацию"


# Шаг 6
    selectSaveOrPublish.click()

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]")))
    buttonPrivateVideo = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]")
    assert buttonPrivateVideo.is_displayed() == True  # Наличие выбора "Ограниченный доступ"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")))
    buttonUnlistedVideo = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")
    assert buttonUnlistedVideo.is_displayed() == True  # Наличие выбора "Доступ по ссылке"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]")))
    buttonPublicVideo = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]")
    assert buttonPublicVideo.is_displayed() == True  # Наличие выбора "Открытый доступ"


# Шаг 7
    buttonPrivateVideo.click()
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/div/ytcp-button[2]")))
    buttonSaveAccess = driver.find_element(By.XPATH,
                             "/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/div/ytcp-button[2]")
    buttonSaveAccess.click()

# Шаг 8
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-sticky-header/ytcp-entity-page-header/div/div[2]/ytcp-button[2]")))
    buttonSave = driver.find_element(By.XPATH,
                             "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-sticky-header/ytcp-entity-page-header/div/div[2]/ytcp-button[2]")
    buttonSave.click()