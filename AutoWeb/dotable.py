"""
本模块使用原生JS定位表单（表格）元素。
"""
import AutoWeb as _this
import AutoWeb.util as webutil


def __find_element_by_document_selector(selector):
    return _this.get_browser().execute_script('return document.querySelector("' + selector + '")')


def __focus_cell(selector, click, x_offset, y_offset):
    cell = __find_element_by_document_selector(selector)
    try:
        _this.get_browser().execute_script('arguments[0].focus()', cell)
    except:
        print(cell)
        print(type(cell))
    if click:
        webutil.move_and_click_elem(cell, x_offset=x_offset, y_offset=y_offset, t=0.8)
    return cell


def plain(selector, text, click=True, x_offset=20, y_offset=20):
    try:
        cell = __focus_cell(selector, click, x_offset, y_offset)
        inp = cell.find_element_by_css_selector('input')
        inp.send_keys(text)
    except:
        cell = __find_element_by_document_selector(selector)
        cell.click()
        inp = cell.find_element_by_css_selector('input')
        inp.send_keys(text)
        pass


def do_search(selector, do_search_selector, word, until_id,
              data_selector, word_selector, search_selector, ok_selector,
              click=True, x_offset=20, y_offset=20):
    if selector is not None:
        __focus_cell(selector, click, x_offset, y_offset)
    __focus_cell(do_search_selector, click, x_offset, y_offset)
    webutil.is_visible(until_id)
    datas = _this.get_browser().execute_script('return document.querySelectorAll(\'' + data_selector + '\')')
    has_find = False
    for data in datas:
        if data.text == word:
            has_find = True
            webutil.move_and_click_elem(data, x_offset=x_offset, y_offset=y_offset, focus=False)
            __focus_cell(ok_selector, True, x_offset, y_offset)
            break
    if not has_find:
        # 输入查询条件
        word_inp = __focus_cell(word_selector, True, x_offset=x_offset, y_offset=y_offset)
        webutil.send_text(word_inp, word)
        __focus_cell(search_selector, True, x_offset=x_offset, y_offset=y_offset)
        webutil.is_visible(until_id)
        datas = _this.get_browser().execute_script('return document.querySelectorAll(\'' + data_selector + '\')')
        has_find = False
        for data in datas:
            if data.text == word:
                has_find = True
                webutil.move_and_click_elem(data, x_offset=x_offset, y_offset=y_offset, focus=False)
                __focus_cell(ok_selector, True, x_offset, y_offset)
                break
