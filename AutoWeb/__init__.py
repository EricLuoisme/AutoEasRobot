from selenium import webdriver
import AutoWeb.util as webutil

from AutoWeb.data import userinfo
import AutoWeb.operation

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# private全局变量browser
__browser = webdriver.Chrome(chrome_options=option)
__browser.maximize_window()
__browser.get(userinfo.url)

# 浏览器导航高度
__browser_navigation_panel_height = __browser.execute_script('return window.outerHeight - window.innerHeight;')


def get_browser():
    return __browser


def get_browser_navigation_height():
    return __browser_navigation_panel_height


def login():
    # 登录
    webutil.is_visible('backImgDiv_voice')
    webutil.move_and_click_by_css_selector('#backImgDiv_voice div.switch-btn-container a.account')

    # 校验数据中心
    if __browser.find_element_by_css_selector('#select_info_dataCenter').text != userinfo.data_center:
        webutil.move_and_click_by_id('select_dataCenter')
        # 选择数据中心
        webutil.is_visible('selected_dataCenter')
        data_centers = __browser.find_elements_by_css_selector('#options_dataCenter li')
        for center in data_centers:
            if center.get_property('title') == userinfo.data_center:
                webutil.move_and_click_elem(center, y_offset=10)
                break
        # 再次跳转到首页
        webutil.is_visible('backImgDiv_voice')
        webutil.move_and_click_by_css_selector('#backImgDiv_voice div.switch-btn-container a.account')

    webutil.is_visible('layoutDiv')
    # 选择账号密码登录
    if __browser.find_element_by_css_selector('div.user_cont').value_of_css_property('display') == 'none':
        webutil.move_and_click_by_css_selector('div.login-switch')

    webutil.is_visible_by_class('user_cont')
    username = __browser.find_element_by_id('username')
    if username.get_property('value') != userinfo.user_name:
        webutil.move_and_click_elem(username, y_offset=10)
        username.clear()
        webutil.send_text(username, userinfo.user_name)
    password = __browser.find_element_by_id('password')
    if password.get_property('value') != userinfo.password:
        webutil.move_and_click_elem(password, y_offset=10)
        password.clear()
        webutil.send_text(password, userinfo.password)
    webutil.move_and_click_by_id('loginSubmit')

    if 'loginCheck' in __browser.current_url:
        # 账号在线提示
        webutil.is_visible_by_class('ignore')
        webutil.move_and_click_by_css_selector('div.ignore')


def add_certification():
    """
    新增凭证
    :return:
    """
    operation.add_certification('凭证新增')


def submit_certification():
    """
    提交凭证
    :return:
    """
    return operation.certificate_submit('方案维护')


def show_submit_certification_fail_log():
    """
    查看提交凭证错误信息
    :return:
    """
    operation.show_add_certification_fail_log()


def close_submit_certification_fail_log():
    """
    关闭凭证信息
    :return:
    """
    operation.close_certification_log()


def show_submit_certification_setting():
    """
    查看提交凭证设置
    :return:
    """
    operation.certification_setting()
