import AutoWeb as _this
import AutoWeb.util as webutil
import AutoWeb.dotable as dotable
from AutoWeb.data import menu as dmanu
from AutoWeb.data import business
import re
#import AudioProcess.Recognition_process as rec


__operation_list = ['凭证新增', '方案维护', '执行日志']
__navigation_height = 0


# 新增凭证
def add_certification(operation):
    """
    新增凭证
    :param operation:
    :return:
    """
    if operation in __operation_list:
        select_menu(operation)
        __switch_to_current_frame()
        webutil.is_invisible('loading-body-overlay')

        # 确保是可操作界面
        __refresh_to('凭证新增')

        # 获得页面的iframe（表单元素在子iframe frame_tab_0中）
        # offset_top = _this.get_browser().execute_script('return $("#frame_tab_0").offset().top')
        _this.get_browser().switch_to.frame(_this.get_browser().find_element_by_id('frame_tab_0'))

        start_date = _this.get_browser().find_element_by_id('column_bookedDate')
        if start_date.get_attribute('value') != business.business_add_certification['start_date']:
            webutil.move_and_click_elem(start_date, y_offset=10)
            start_date.clear()
            webutil.send_text(start_date, business.business_add_certification['start_date'])
        end_date = _this.get_browser().find_element_by_id('column_bizDate')
        if end_date.get_attribute('value') != business.business_add_certification['end_date']:
            webutil.move_and_click_elem(end_date, y_offset=10)
            end_date.clear()
            webutil.send_text(end_date, business.business_add_certification['end_date'])

        # 操作表格
        operations = business.business_add_certification['data']
        op_tr = operations['tr']
        for op in operations['cells']:
            tr_no = str(op['tr_no'])
            td_no = str(op['td_no'])
            cell_selector = '#'+op_tr+tr_no+' td:nth-child('+td_no+')'
            if op['type'] == 'plain':       # 直接文本
                dotable.plain(cell_selector, op['word'], y_offset=10)
            elif op['type'] == 'do_search':     # 直接搜索
                dotable.do_search(
                    cell_selector, op['do_search_selector'], op['word'], op['until'], op['data_selector'],
                    op['word_selector'], op['search_selector'], op['ok_selector'], y_offset=10)

            if 'call_back' in op:
                # 回调操作:
                call_back = op['call_back']
                if call_back['type'] == 'asst':
                    for cb in call_back['cells']:
                        if cb['type'] == 'plain':    # 直接文本
                            # 考虑合并到dotable?
                            inp = _this.get_browser().execute_script('return document.querySelector("'+cb['selector']+'")')
                            if inp.get_attribute('value') != cb['word']:
                                inp.send_text(cb['word'])
                        elif cb['type'] == 'do_search':     # 直接搜索
                            dotable.do_search(None, cb['do_search_selector'], cb['word'], cb['until'], cb['data_selector'],
                                              cb['word_selector'], cb['search_selector'], cb['ok_selector'], y_offset=10)

        # 保存
        webutil.move_and_click_elem(_this.get_browser().find_element_by_id('toolBar_save'), y_offset=10)
        print('已经为您完成了提现凭证的制作，请查看凭证。')
        #rec.doing_voice_Comb('已经为您完成了提现凭证的制作，请查看凭证。')

        __switch_to_main()


# 提交凭证
def certificate_submit(operation):
    """
    提交凭证
    :param operation:
    :return:
    """
    if operation in __operation_list:
        select_menu(operation)
        __switch_to_current_frame()
        webutil.is_invisible('loading-body-overlay')

        # 确保是可操作界面
        __refresh_to('智能核算方案序时簿')

        # 获得页面的iframe（表单元素在子iframe frame_tab_0中）
        # offset_top = _this.get_browser().execute_script('return document.querySelector("#breadCrumbs").offsetHeight')
        _this.get_browser().switch_to.frame(_this.get_browser().find_element_by_id('frame_tab_0'))

        webutil.is_visible('queryGrid')
        datas = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content td[aria-describedby=queryGrid_name]")')
        should_search = True
        for data in datas:
            if data.text == business.business_certification_submit['scheme_name']:
                should_search = False
                webutil.move_and_click_elem(data)
                break
        if should_search:
            pass

        webutil.move_and_click_by_id('executeSchema')
        # 获取弹窗
        # 切换到上一层iframe
        __switch_to_current_frame()
        webutil.is_visible_by_class('ui-dialog')
        webutil.move_and_click_elem(_this.get_browser().find_element_by_css_selector('.msgbox-content .ui-dialog-buttonset button.btn0'))

        # 获取执行结果
        webutil.delay(1)
        webutil.is_visible_by_class('msgbox-content', timeout=30)
        result = _this.get_browser().find_element_by_css_selector('.msgbox-content .ui-msgbox table div.content').text
        counts = re.findall('\d+', result)
        success_count = counts[0]
        fail_count = counts[1]
        # 汇报执行结果

        webutil.move_and_click_elem(_this.get_browser().find_element_by_css_selector('.msgbox-content button.btn0'))

        # 执行日志
        # __switch_to_main()
        # schema_log('执行日志')

        # 切换回当前窗口
        __switch_to_current_frame()
        _this.get_browser().switch_to.frame(_this.get_browser().find_element_by_id('frame_tab_0'))
        # 联查日志
        webutil.move_and_click_by_id('linkReport')
        __switch_to_current_frame()
        _this.get_browser().switch_to.frame(_this.get_browser().execute_script('return document.querySelectorAll("iframe[id^=frame_tab]")')[-1])
        webutil.is_visible('queryGrid')
        trs = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content")')
        should_search = True
        for tr in trs:
            data = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_schemaName]')
            if data.text == business.business_certification_submit['scheme_name']:
                should_search = False
                webutil.move_and_click_elem(data)
                # 查看状态
                status = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_status]')
                counts = re.findall('\d+', status.text)
                success_count = int(counts[0])
                fail_count = int(counts[1])
                __switch_to_main()
                # 场景：你好，本会计期间内填写正确凭证已经全部提交成功，填写错误的凭证提交失败，需要为您打开查看了解具体失败的原因吗？
                result = '你好，本会计期间内'
                code = 1
                if success_count > 0:
                    result += '填写的凭证已经全部提交完成，全部凭证提交成功。'
                if fail_count > 0:
                    code = 0
                    result += '填写无误的凭证已经全部提交成功，同时校验发现有'+str(fail_count)+'个凭证有错，提交失败，需要为您打开查看了解具体失败的原因吗？'
                print(result)
                return code, result
                #rec.doing_voice_Comb(result)
                # fail_btn = status.find_element_by_css_selector('a:nth-child(2)')
                # webutil.move_and_click_elem(fail_btn, x_offset=10)
                break
        if should_search:
            pass

        __switch_to_main()
    else:
        print('没有定义的操作')


# 展示凭证错误信息
def show_add_certification_fail_log():
    """
    展示凭证错误信息
    :return:
    """
    select_menu('方案维护')
    __switch_to_current_frame()
    webutil.is_invisible('loading-body-overlay')
    _this.get_browser().switch_to.frame(_this.get_browser().find_elements_by_css_selector('iframe[id^=frame_tab]')[-1])

    trs = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content")')
    for tr in trs:
        data = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_schemaName]')
        if data.text == business.business_certification_submit['scheme_name']:
            # 查看状态
            status = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_status]')
            counts = re.findall('\d+', status.text)
            success_count = int(counts[0])
            fail_count = int(counts[1])
            if fail_count > 0:
                fail_btn = status.find_element_by_css_selector('a:nth-child(2)')
                webutil.move_and_click_elem(fail_btn, x_offset=10, y_offset=10)
                print('已为你打开异常信息')
                #rec.doing_voice_Comb('已为你打开异常信息')
            else:
                print('本会计期间没有失败操作')
                #rec.doing_voice_Comb('本会计期间没有失败操作')
            break

    __switch_to_main()


# 关闭
def close_certification_log():
    __close_tab('方案维护')


# def schema_log(operation):
#     if operation in __operation_list:
#         select_menu(operation)
#         __switch_to_current_frame()
#         webutil.is_invisible('loading-body-overlay')
#
#         # 切换回当前窗口
#         __switch_to_current_frame()
#         _this.get_browser().switch_to.frame(_this.get_browser().find_element_by_id('frame_tab_0'))
#         webutil.is_visible('queryGrid')
#         trs = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content")')
#         should_search = True
#         for tr in trs:
#             data = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_schemaName]')
#             if data.text == business.business_certification_submit['scheme_name']:
#                 should_search = False
#                 webutil.move_and_click_elem(data)
#                 # 查看状态
#                 status = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_status]')
#                 counts = re.findall('\d+', status.text)
#                 success_count = counts[0]
#                 fail_count = counts[1]
#                 fail_btn = status.find_element_by_css_selector('a:nth-child(2)')
#                 print('你好，本会计期间内填写正确凭证已经全部提交成功，填写错误的凭证提交失败，需要为您打开查看了解具体失败的原因吗？')
#                 if input() == '好的':
#                     webutil.move_and_click_elem(fail_btn, x_offset=10)
#                 else:
#                     __close_tab('执行日志')
#                 break
#         if should_search:
#             pass
#
#         __switch_to_main()
#     else:
#         print('没有定义的操作')


def certification_setting():
    select_menu('方案维护')
    __switch_to_current_frame()
    webutil.is_invisible('loading-body-overlay')

    # 确保是可操作界面
    __refresh_to('智能核算方案序时簿')

    # 获得页面的iframe（表单元素在子iframe frame_tab_0中）
    _this.get_browser().switch_to.frame(_this.get_browser().find_element_by_id('frame_tab_0'))

    webutil.is_visible('queryGrid')
    trs = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content")')
    should_search = True
    schema_code = 0
    for tr in trs:
        data = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_name]')
        if data.text == business.business_certification_submit['scheme_name']:
            should_search = False
            schema_link = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_number] a')
            schema_code = schema_link.text
            webutil.move_and_click_elem(schema_link, y_offset=10)
            break
    if should_search:
        pass

    # 任务详情
    __switch_to_current_frame()
    webutil.is_invisible('loading-body-overlay')
    _this.get_browser().switch_to.frame(_this.get_browser().execute_script('return document.querySelectorAll("iframe[id^=frame_tab]")')[-1])
    webutil.is_visible('queryGrid')
    trs = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content")')
    should_search = True
    for tr in trs:
        data = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_number] a')
        if data.text == schema_code:
            should_search = False
            webutil.move_and_click_elem(data, y_offset=10)
            # 查看状态
            __switch_to_current_frame()
            webutil.is_invisible('loading-body-overlay')
            # 处理错误页面（正在进行编辑）
            if _this.get_browser().find_elements_by_css_selector('#breadCrumbs ul li')[-1].text == '错误页面':
                print('错误页面')
                break
            _this.get_browser().switch_to.frame(_this.get_browser().execute_script('return document.querySelectorAll("iframe[id^=frame_tab]")')[-1])
            schema_code = _this.get_browser().find_element_by_css_selector('input#number').get_attribute('value')
            schema_name = _this.get_browser().find_element_by_css_selector('input#name').get_attribute('value')
            schema_schedule = _this.get_browser().find_element_by_css_selector('input#schedule').get_attribute('value')
            schema_company = ''
            for tr in _this.get_browser().find_elements_by_css_selector('#editGrid1 tr.ui-widget-content td[aria-describedby=editGrid1_companyname]'):
                schema_company += tr.text + '、'
            schema_business = []
            for tr in _this.get_browser().find_elements_by_css_selector('#editGrid tr.ui-widget-content'):
                print(tr.get_attribute('id'))
                schema_business.append(dict(
                    no=tr.find_element_by_css_selector('td[aria-describedby=editGrid_rn]').text,
                    system=tr.find_element_by_css_selector('td[aria-describedby=editGrid_subSystem]').text,
                    type=tr.find_element_by_css_selector('td[aria-describedby=editGrid_businessNumber]').text,
                    operator=tr.find_element_by_css_selector('td[aria-describedby=editGrid_operatorNumber]').text
                ))
            result = ''
            for sb in schema_business:
                result += '本页面的设置，可以保证'+sb['system']+sb['type']+'、'
            result = schema_company+schema_schedule+'进行'+result
            print(result)
            #rec.doing_voice_Comb(result)
            break
    if should_search:
        pass
    __switch_to_main()


def certification_check():
    select_menu('方案维护')
    __switch_to_current_frame()
    webutil.is_invisible('loading-body-overlay')

    # 确保是可操作界面
    __refresh_to('智能核算方案序时簿')

    # 获得页面的iframe（表单元素在子iframe frame_tab_0中）
    _this.get_browser().switch_to.frame(_this.get_browser().find_element_by_id('frame_tab_0'))

    webutil.is_visible('queryGrid')
    datas = _this.get_browser().execute_script(
        'return document.querySelectorAll("#queryGrid tr.ui-widget-content td[aria-describedby=queryGrid_name]")')
    should_search = True
    for data in datas:
        if data.text == business.business_certification_check['scheme_name']:
            should_search = False
            webutil.move_and_click_elem(data)
            break
    if should_search:
        pass

    webutil.move_and_click_by_id('executeSchema')
    # 获取弹窗
    # 切换到上一层iframe
    __switch_to_current_frame()
    webutil.is_visible_by_class('ui-dialog')
    webutil.move_and_click_elem(
        _this.get_browser().find_element_by_css_selector('.msgbox-content .ui-dialog-buttonset button.btn0'))

    # 获取执行结果
    webutil.delay(1)
    webutil.is_visible_by_class('msgbox-content', timeout=30)
    result = _this.get_browser().find_element_by_css_selector('.msgbox-content .ui-msgbox table div.content').text
    counts = re.findall('\d+', result)
    success_count = counts[0]
    fail_count = counts[1]
    # 汇报执行结果

    webutil.move_and_click_elem(_this.get_browser().find_element_by_css_selector('.msgbox-content button.btn0'))

    # 切换回当前窗口
    __switch_to_current_frame()
    _this.get_browser().switch_to.frame(_this.get_browser().find_element_by_id('frame_tab_0'))
    # 联查日志
    webutil.move_and_click_by_id('linkReport')
    __switch_to_current_frame()
    _this.get_browser().switch_to.frame(_this.get_browser().execute_script('return document.querySelectorAll("iframe[id^=frame_tab]")')[-1])
    webutil.is_visible('queryGrid')
    trs = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content")')
    should_search = True
    for tr in trs:
        data = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_schemaName]')
        if data.text == business.business_certification_check['scheme_name']:
            should_search = False
            webutil.move_and_click_elem(data)
            # 查看状态
            status = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_status]')
            counts = re.findall('\d+', status.text)
            success_count = int(counts[0])
            fail_count = int(counts[1])
            # 你好，本会计期间内提交的凭证已经全部审核成功，需要为您打开查看下已经审核成功的凭证信息吗？
            if success_count == 0 and fail_count == 0:
                print('抱歉，本会计期间没有需要审核的凭证')
                #rec.doing_voice_Comb('抱歉，本会计期间没有需要审核的凭证')
            if success_count > 0 and fail_count == 0:
                print('你好，本会计期间内提交的凭证已经全部审核成功，需要为您打开查看下已经审核成功的凭证信息吗？')
                #rec.doing_voice_Comb('你好，本会计期间内提交的凭证已经全部审核成功，需要为您打开查看下已经审核成功的凭证信息吗？')
            if success_count == 0 and fail_count > 0:
                print('抱歉，本会计期间内提交的凭证全部审核失败，需要为您打开查看下审核失败的凭证信息吗？')
                #rec.doing_voice_Comb('抱歉，本会计期间内提交的凭证全部审核失败，需要为您打开查看下审核失败的凭证信息吗？')
            break
    if should_search:
        pass
    __switch_to_main()


def show_check_certification_success_log():
    select_menu('方案维护')
    __switch_to_current_frame()
    webutil.is_invisible('loading-body-overlay')
    _this.get_browser().switch_to.frame(_this.get_browser().find_elements_by_css_selector('iframe[id^=frame_tab]')[-1])

    trs = _this.get_browser().execute_script('return document.querySelectorAll("#queryGrid tr.ui-widget-content")')
    for tr in trs:
        data = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_schemaName]')
        if data.text == business.business_certification_check['scheme_name']:
            # 查看状态
            status = tr.find_element_by_css_selector('td[aria-describedby=queryGrid_status]')
            counts = re.findall('\d+', status.text)
            success_count = int(counts[0])
            fail_count = int(counts[1])
            if success_count == 0 and fail_count == 0:
                print('抱歉，本会计期间没有审核记录')
                #rec.doing_voice_Comb('抱歉，本会计期间没有审核记录')
            if success_count > 0 and fail_count == 0:
                success_btn = status.find_element_by_css_selector('a:nth-child(1)')
                webutil.move_and_click_elem(success_btn, x_offset=10, y_offset=10)
                print('已为你打开成功信息')
                #rec.doing_voice_Comb('已为你打开成功信息')
            if success_count == 0 and fail_count > 0:
                fail_btn = status.find_element_by_css_selector('a:nth-child(2)')
                webutil.move_and_click_elem(fail_btn, x_offset=10, y_offset=10)
                print('已为你打开异常信息')
                #rec.doing_voice_Comb('已为你打开异常信息')
            break

    __switch_to_main()


def select_menu(operation):
    __switch_to_main()
    # 判断是否已经打开菜单
    lis = _this.get_browser().find_elements_by_css_selector('ul.portal-tabbar-menus li')
    should_click_app = True
    for li in reversed(lis):
        p = li.find_element_by_css_selector('a p')
        if p.get_attribute('_title') == operation:
            if 'transition' not in li.find_element_by_css_selector('a').get_attribute('class'):
                webutil.move_and_click_elem(p)
            return
        if p.get_attribute('_title') == '应用':
            if 'on' not in li.get_attribute('class'):
                webutil.move_and_click_elem(p)
            should_click_app = False

    first, second, third = dmanu.get_path_by_operation(operation)

    if should_click_app:
        webutil.move_and_click_by_id('appcenter')

    __switch_to_current_frame()

    # 一级菜单
    webutil.is_visible_by_class('viewTmpl-leftNav')
    for menu in _this.get_browser().find_elements_by_css_selector('.viewTmpl-leftNav .KdAccordion dt'):
        if menu.text == first:
            first = menu
            if 'on' not in menu.get_attribute('class'):
                # _this.get_browser().execute_script("arguments[0].scrollIntoView();", menu)
                webutil.move_and_click_elem(menu)
            break
    # 二级菜单
    for menu in _this.get_browser().find_elements_by_css_selector('#'+first.get_attribute('id')+' + dd ul.appCenter-leftTreeUL li'):
        if menu.text == second:
            if 'chosed' not in menu.get_attribute('class'):
                # _this.get_browser().execute_script("arguments[0].scrollIntoView();", menu)
                webutil.move_and_click_elem(menu)
            break
    # 三级菜单
    webutil.delay(1)
    for menu in _this.get_browser().find_elements_by_css_selector('#appCenter-content ul.appCenter-tabul li'):
        if menu.get_attribute('displayname') == third:
            # _this.get_browser().execute_script("arguments[0].scrollIntoView();", menu)
            webutil.move_and_click_elem(menu)
            break

    __switch_to_main()


def __switch_to_current_frame():
    """
    定位到当前IFrame
    :return:
    """
    webutil.delay(1)
    __switch_to_main()
    for ifame in _this.get_browser().find_elements_by_css_selector('#pageContainer iframe.portal-page'):
        if 'hide' not in ifame.get_attribute('class'):
            # 主页导航栏高度
            _this.get_browser().switch_to.default_content()
            global __navigation_height
            __navigation_height = _this.get_browser().execute_script('return document.getElementById("header").offsetHeight+document.getElementById("tabbar").offsetHeight')

            # 切换iframe
            _this.get_browser().switch_to.frame(ifame)
            break


def __switch_to_main():
    """
    切换到主窗口
    :return:
    """
    _this.get_browser().switch_to.default_content()


def __close_tab(name):
    webutil.delay(1)
    __switch_to_main()
    lis = _this.get_browser().find_elements_by_css_selector('ul.portal-tabbar-menus li')
    for li in lis:
        p = li.find_element_by_css_selector('a p')
        if p.text == name:
            webutil.move_to_elem(p)
            em = li.find_element_by_css_selector('a em')
            webutil.move_and_click_elem(em, x_offset=5, y_offset=10)
            break


def __get_current_path():
    crumbs = _this.get_browser().find_elements_by_css_selector('#breadCrumbs ul.ui-breadcrumbs li')
    return crumbs[-1].text


def __refresh_to(path):
    if __get_current_path() != path:
        __switch_to_main()
        webutil.move_and_click_elem(_this.get_browser().find_element_by_css_selector('#portalTabbarWrapper .icon-shuaxin'), x_offset=10)
        __switch_to_current_frame()
