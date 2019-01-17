business_add_certification = {
    'start_date': '2018-01-12',     # 记账日期
    'end_date': '2018-01-12',       # 业务日期
    'type': '记账',                 # 凭证字号
    'data': {
        'tr': 'jqg',
        'cells': [
            {
                'tr_no': 1,
                'td_no': 3,
                'type': 'plain',
                'word': '提现业务'
            },
            {
                'tr_no': 1,
                'td_no': 5,
                'type': 'do_search',
                'word': '人民币',
                'do_search_selector': '#asst .ui-f7-trigger',
                'until': 'accountpromptBox_table',
                'data_selector': '#accountpromptBox_table tr.ui-widget-content td[aria-describedby="accountpromptBox_table_name"]',
                'word_selector': '#accountpromptBox-searchInput',
                'search_selector': 'button.ui-promptSpecial-searchButton',
                'ok_selector': 'button.ui-promptSpecial-submit',
            },
            {
                'tr_no': 1,
                'td_no': 8,
                'type': 'plain',
                'word': '1500'
            },
            {
                'tr_no': 2,
                'td_no': 5,
                'type': 'do_search',
                'word': '商业银行存款',
                'do_search_selector': '#asst .ui-f7-trigger',
                'until': 'accountpromptBox_table',
                'data_selector': '#accountpromptBox_table tr.ui-widget-content td[aria-describedby="accountpromptBox_table_name"]',
                'word_selector': '#accountpromptBox-searchInput',
                'search_selector': 'button.ui-promptSpecial-searchButton',
                'ok_selector': 'button.ui-promptSpecial-submit',
                'call_back': {
                    'until': 'asst',
                    'type': 'asst',
                    'cells': [
                        {
                            'selector': '#asstBizDate',
                            'type': 'plain',
                            'word': '2018-01-12'
                        },
                        {
                            'do_search_selector': '#accbankAccountLb span.ui-f7-trigger',
                            'type': 'do_search',
                            'word': 'KINGDEE SOFTWARE (CHINA) CO., LTD',
                            'until': 'accbankAccount_table',
                            'data_selector': '#accbankAccount_table tr.ui-widget-content td[aria-describedby="accbankAccount_table_name"]',
                            'word_selector': '#accbankAccount-searchInput',
                            'search_selector': 'button.ui-promptStandard-searchButton',
                            'ok_selector': 'button.ui-promptStandard-submit'
                        }
                    ]
                }
            },
            {
                'tr_no': 2,
                'td_no': 9,
                'type': 'plain',
                'word': '1500'
            },
        ]
    }
}

business_certification_submit = {
    'scheme_name': '总账凭证提交机器人'
}

business_certification_check = {
    'scheme_name': '总账凭证审核机器人'
}
