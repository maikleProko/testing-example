import os

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

user_login = "tpotestmd@gmail.com"
user_password = "asjdhkasjdhka"

video_name = "video000"
video_description = "description hello world"
video_path = "D:\\Unik2\\Autolab\\videos\\bots_status2.mp4"


def test_case1():
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
                                        "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button")))
    createButton = driver.find_element(By.XPATH,
                                       "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button")

    hov = ActionChains(driver).move_to_element(createButton)
    hov.perform()
    assert createButton.get_attribute("aria-label") == "Создать"  # Всплывающая подсказка с текстом "Создать"
    sleep(1)

# Шаг 2
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button"))).click()

    uploadVideoButton = driver.find_element(By.XPATH,
                                            "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]")
    translationButton = driver.find_element(By.XPATH,
                                            "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[2]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]")

    assert uploadVideoButton.is_displayed() == True  # Наличие кнопки загрузки видео
    assert translationButton.is_displayed() == True  # Наличие кнопки проведения трансляции


# Шаг 3
    prevUrl = driver.current_url
    uploadVideoButton.click()
    WebDriverWait(driver, timeout=300).until(EC.url_changes(prevUrl))
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div")))
    modalViewLoad = driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div")
    assert modalViewLoad.is_displayed() == True  # Наличие модального окна для загрузки видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/div/ytcp-animatable/div")))
    modalViewLoadText = driver.find_element(By.XPATH,
                                            "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/div/ytcp-animatable/div")
    assert modalViewLoadText.text == "Загрузка видео"  # Проверка на текст для модального окна загрузки видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button")))
    loadButton = driver.find_element(By.XPATH,
                                     "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button")
    assert loadButton.is_displayed() == True  # Наличие кнопки для загрузки видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/div")))
    loadButtonText = driver.find_element(By.XPATH,
                                         "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/div")
    assert loadButtonText.text == "ВЫБРАТЬ ФАЙЛЫ"  # Проверка на текст для кнопки загрузки видео
    loadUrl = driver.current_url


# Шаги 4-5

    manager = driver.find_element(By.XPATH,
                                  "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input")
    manager.send_keys(video_path)  # Загрузка видео
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog")))
    modalEdit = driver.find_element(By.XPATH,
                                    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog")
    assert modalEdit.is_displayed() == True  # Наличие нового модального окна для редактирования после загрузки видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[1]/button")))
    modalMenuInfo = driver.find_element(By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[1]/button")
    assert modalMenuInfo.is_displayed() == True  # Наличие вкладки "Информация"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[2]/button")))
    modalMenuAdv = driver.find_element(By.XPATH,
                                       "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[2]/button")
    assert modalMenuAdv.is_displayed() == True  # Наличие вкладки "Дополнения"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[3]/button")))
    modalMenuChecks = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[3]/button")

    assert modalMenuChecks.is_displayed() == True  # Наличие вкладки "Проверки"
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[4]/button")))
    modalMenuAccess = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[4]/button")
    assert modalMenuAccess.is_displayed() == True  # Наличие вкладки "Доступ"

    assert modalMenuInfo.get_attribute("state") == "active"  # Выбрана вкладка "Информация"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")))
    infoTitle = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
    assert infoTitle.is_displayed() == True  # Наличие поля ввода текста для названия видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")))
    infoDescription = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
    assert infoDescription.is_displayed() == True  # Наличие поля ввода текста для описания видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]/ytcp-thumbnails-compact-editor")))
    infoThumbnail = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]/ytcp-thumbnails-compact-editor")
    assert infoThumbnail.is_displayed() == True  # Наличие настройки изменения значка видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[4]")))
    infoPlaylists = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[4]")
    assert infoPlaylists.is_displayed() == True  # Наличие настройки изменения плейлиста видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]")))
    infoAudience = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]")
    assert infoAudience.is_displayed() == True  # Наличие настройки изменения аудитории

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-video-info/div")))
    infoVideo = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-video-info/div")
    assert infoVideo.is_displayed() == True  # В правой части модального окна отображено видео


# Шаг 6
    textTitle = video_name
    numbTextTitle = len(textTitle)
    infoTitle.clear()
    infoTitle.send_keys(textTitle)
    infoTitle.click()
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/div/ytcp-animatable/div")))
    modalTitle = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/div/ytcp-animatable/div")

    assert modalTitle.text == textTitle  # Изменение названия видео

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/div/div")))
    infoTitleNumberSymbols = driver.find_element(By.XPATH,
                                          "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/div/div")
    strNumbTextTitle = str(numbTextTitle) + "/100"
    assert infoTitleNumberSymbols.text == strNumbTextTitle

# Шаг 7
    textDescription = video_description
    numbTextDescription = len(textDescription)
    infoDescription.clear()
    infoDescription.send_keys(textDescription)
    infoDescription.click()

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/div/div")))
    infoDescriptionNumberSymbols = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/div/div")
    strNumbTextDescription = str(numbTextDescription) + "/5000"
    assert infoDescriptionNumberSymbols.text == strNumbTextDescription


# Шаг 8
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]/ytcp-thumbnails-compact-editor/div[3]/ytcp-still-cell[1]/button/div")))
    Thumbnail = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]/ytcp-thumbnails-compact-editor/div[3]/ytcp-still-cell[1]/button/div")
    assert Thumbnail.is_displayed() == True

# Шаг 10
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[4]/div[3]/div[1]/ytcp-video-metadata-playlists/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[2]/span")))
    playlistButton = driver.find_element(By.XPATH,
                                     "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[4]/div[3]/div[1]/ytcp-video-metadata-playlists/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[2]/span")
    playlistButton.click()
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog")))
    modalPlaylist = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog")
    assert modalPlaylist.is_displayed() == True  # Наличие маленького модального окна для выбора плейлиста отобразилось

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog/ytcp-checkbox-group/div/ul/tp-yt-iron-list/div/ytcp-ve/li/label/ytcp-checkbox-lit")))
    modalPlaylistRectangleSelect = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog/ytcp-checkbox-group/div/ul/tp-yt-iron-list/div/ytcp-ve/li/label/ytcp-checkbox-lit")
    assert modalPlaylistRectangleSelect.is_displayed() == True  # Наличие квадрата выбора напротив плейлиства

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog/div[2]/ytcp-button[1]/div")))
    modalPlaylistButtonNew = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog/div[2]/ytcp-button[1]/div")
    assert modalPlaylistButtonNew.is_displayed() == True  # Наличие кнопки создания нового плейлиста


    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog/div[2]/ytcp-button[3]/div")))
    modalPlaylistButtonOK = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog/div[2]/ytcp-button[3]/div")
    assert modalPlaylistButtonOK.is_displayed() == True  # Наличие кнопки "OK" при выборе плейлиста


# Шаг 11
    modalPlaylistRectangleSelect.click()
    assert modalPlaylistRectangleSelect.get_attribute("checked") == "true"


# Шаг 12
    modalPlaylistButtonOK.click()
    assert modalPlaylist.get_attribute("aria-hidden") == "true"


# Шаг 13
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")))
    buttonNotForKids = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")
    buttonNotForKids.click()
    sleep(2)
    modalMenuAdv.click()
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-video-elements/div[2]")))
    paramSubtitles = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-video-elements/div[2]")
    assert paramSubtitles.is_displayed() == True  # Наличие настройки субтитров

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-video-elements/div[3]")))
    paramAnScreen = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-video-elements/div[3]")
    assert paramAnScreen.is_displayed() == True  # Наличие настройки конечной заставки

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-video-elements/div[4]")))
    paramCards = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-video-elements/div[4]")
    assert paramCards.is_displayed() == True  # Наличие настройки подсказок


# Шаг 14
    modalMenuChecks.click()
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-checks")))
    FoundChecks = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-checks")
    assert FoundChecks.is_displayed() == True  # Наличие отображения нарушенных авторских прав, если они имеются


# Шаг 15
    modalMenuAccess.click()
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select")))
    paramVisibility = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select")
    assert paramVisibility.is_displayed() == True  # Наличие настройки публикации

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]")))
    selectSaveOrPublish = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]")
    assert selectSaveOrPublish.is_displayed() == True  # Наличие выбора "Сохранить или опубликовать"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]")))
    selectSchedule = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]")
    assert selectSchedule.is_displayed() == True  # Наличие выбора "Запланировать публикацию"


# Шаг 16
    selectSaveOrPublish.click()

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]")))
    buttonPrivateVideo = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]")
    assert buttonPrivateVideo.is_displayed() == True  # Наличие выбора "Ограниченный доступ"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")))
    buttonUnlistedVideo = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")
    assert buttonUnlistedVideo.is_displayed() == True  # Наличие выбора "Доступ по ссылке"

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]")))
    buttonPublicVideo = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]")
    assert buttonPublicVideo.is_displayed() == True  # Наличие выбора "Открытый доступ"


# Шаг 17
    buttonUnlistedVideo.click()
    assert buttonUnlistedVideo.get_attribute("aria-selected") == "true"  # Выбрано "Доступ по ссылке"


# Шаг 18
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]")))
    buttonSave = driver.find_element(By.XPATH,
                                                 "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]")
    buttonSave.click()

    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog")))
    modalSave = driver.find_element(By.XPATH,
                                     "/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog")

    assert modalSave.is_displayed() == True  # Показ окна о сохраненном видео