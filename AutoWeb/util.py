import AutoWeb as _this

import pyautogui
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# 一直等待某元素可见，默认超时10秒
def is_visible(elem_id, timeout=10):
    try:
        ui.WebDriverWait(_this.get_browser(), timeout).until(EC.visibility_of_element_located((By.ID, elem_id)))
        return True
    except TimeoutException:
        return False


def is_visible_by_class(elem_class, timeout=10):
    try:
        ui.WebDriverWait(_this.get_browser(), timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, elem_class)))
        return True
    except TimeoutException:
        return False


def is_invisible(elem_id, timeout=10):
    try:
        ui.WebDriverWait(_this.get_browser(), timeout).until(EC.invisibility_of_element_located((By.ID, elem_id)))
        return True
    except TimeoutException:
        return False


def is_invisible_by_class(elem_class, timeout=10):
    try:
        ui.WebDriverWait(_this.get_browser(), timeout).until(EC.invisibility_of_element_located((By.CLASS_NAME, elem_class)))
        return True
    except TimeoutException:
        return False


def send_text(elem, text):
    """
    文本域输入（逐字输入）
    :param elem:可输入的Dom元素
    :param text:要输入的文本
    :return:
    """
    elem.clear()
    for i in range(len(text)):
        elem.send_keys(text[i])
        time.sleep(0.3)


def move_to_elem(elem, x_offset=20, y_offset=20, t=1):
    """
    移动鼠标到指定控件区域
    :param elem: 控件
    :param x_offset: 横向偏移（默认值为20）
    :param y_offset: 纵向偏移（默认值为20）
    :param t: 移动时间（单位：s，默认值为1s）
    :return:
    """
    pyautogui.moveTo(elem.location_once_scrolled_into_view['x']+x_offset, elem.location_once_scrolled_into_view['y']+_this.get_browser_navigation_height()+y_offset, t)


def move_and_click_elem(elem, x_offset=20, y_offset=20, t=1, focus=False):
    if focus:
        _this.get_browser().execute_script("arguments[0].scrollIntoView();", elem)
    pyautogui.moveTo(elem.location_once_scrolled_into_view['x']+x_offset, elem.location_once_scrolled_into_view['y']+_this.get_browser_navigation_height()+y_offset, t)
    elem.click()


def move_and_click_by_id(_id, x_offset=20, y_offset=20, t=1):
    elem = _this.get_browser().find_element_by_id(_id)
    move_and_click_elem(elem, x_offset, y_offset, t)


def move_and_click_by_css_selector(css, x_offset=20, y_offset=20, t=1):
    elme = _this.get_browser().find_element_by_css_selector(css)
    move_and_click_elem(elme, x_offset, y_offset, t)


def delay(t):
    time.sleep(t)
