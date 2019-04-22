import json

result = '''
{
    "success": true,
    "id": "WF2019042010085224401496",
    "result_desc": {
        "DEFAULT_MODEL": {
            "b1a14f3fe5013fe3": {
                "credit_score": 0,
                "model_version": "1"
            }
        },
        "INFOANALYSIS": {
            "id_age": null,
            "address_detect": {
                "bank_card_address": null,
                "true_ip_address": null,
                "mobile_address_city": "晋城市",
                "id_card_city": null,
                "mobile_address": "山西省晋城市",
                "wifi_address": null,
                "id_card_province": null,
                "cell_address": null,
                "mobile_address_province": "山西省",
                "id_card_address": ""
            },
            "geoip_info": {
                "proxy_info": null,
                "isp": null,
                "latitude": null,
                "position": null,
                "longitude": null
            },
            "device_info": {
                "error": "参数缺失"
            },
            "geotrueip_info": {
                "isp": null,
                "latitude": null,
                "position": null,
                "longitude": null
            },
            "id_gender": null
        },
        "RENT": {
            "final_score": 25,
            "risk_items": [
                {
                    "rule_id": 34612084,
                    "policy_score": 25,
                    "score": 5,
                    "policy_mode": "Weighted",
                    "decision": "Accept",
                    "policy_decision": "Review",
                    "policy_name": "信用租赁_安卓",
                    "risk_name": "租赁人身份证命中中风险关注名单",
                    "risk_detail": [
                        {
                            "hit_type_display_name": "租赁人身份证",
                            "fraud_type_display_name": "异常绑卡、信用异常、异常借款、申请行为异常",
                            "grey_list_details": [
                                {
                                    "evidence_time": 1519096823000,
                                    "risk_level": "中",
                                    "fraud_type": "suspiciousBinding",
                                    "fraud_type_display_name": "异常绑卡",
                                    "value": "140581199410093914"
                                },
                                {
                                    "evidence_time": 1519054750000,
                                    "risk_level": "中",
                                    "fraud_type": "creditSuspicious",
                                    "fraud_type_display_name": "信用异常",
                                    "value": "140581199410093914"
                                },
                                {
                                    "evidence_time": 1555049811000,
                                    "risk_level": "中",
                                    "fraud_type": "suspiciousLoan",
                                    "fraud_type_display_name": "异常借款",
                                    "value": "140581199410093914"
                                },
                                {
                                    "evidence_time": 1555049811000,
                                    "risk_level": "中",
                                    "fraud_type": "applySuspicious",
                                    "fraud_type_display_name": "申请行为异常",
                                    "value": "140581199410093914"
                                }
                            ],
                            "description": "验证匹配字段是否在关注名单中",
                            "type": "grey_list"
                        }
                    ]
                },
                {
                    "rule_id": 34612114,
                    "policy_score": 25,
                    "score": 9,
                    "policy_mode": "Weighted",
                    "decision": "Accept",
                    "policy_decision": "Review",
                    "policy_name": "信用租赁_安卓",
                    "risk_name": "1个月内租赁人在多个平台申请借款",
                    "risk_detail": [
                        {
                            "platform_detail_dimension": [
                                {
                                    "count": 1,
                                    "detail": [
                                        {
                                            "count": 1,
                                            "industry_display_name": "一般消费分期平台"
                                        }
                                    ],
                                    "dimension": "租赁人手机"
                                },
                                {
                                    "count": 3,
                                    "detail": [
                                        {
                                            "count": 1,
                                            "industry_display_name": "一般消费分期平台"
                                        },
                                        {
                                            "count": 1,
                                            "industry_display_name": "网上银行"
                                        },
                                        {
                                            "count": 1,
                                            "industry_display_name": "综合类电商平台"
                                        }
                                    ],
                                    "dimension": "租赁人身份证"
                                }
                            ],
                            "platform_detail": [
                                {
                                    "count": 1,
                                    "industry_display_name": "一般消费分期平台"
                                },
                                {
                                    "count": 1,
                                    "industry_display_name": "网上银行"
                                },
                                {
                                    "count": 1,
                                    "industry_display_name": "综合类电商平台"
                                }
                            ],
                            "description": "在指定时间内，主属性关联的合作方或行业类型的个数",
                            "type": "platform_detail",
                            "platform_count": 3
                        }
                    ]
                },
                {
                    "rule_id": 34612124,
                    "policy_score": 25,
                    "score": 6,
                    "policy_mode": "Weighted",
                    "decision": "Accept",
                    "policy_decision": "Review",
                    "policy_name": "信用租赁_安卓",
                    "risk_name": "3个月内租赁人在多个平台申请借款",
                    "risk_detail": [
                        {
                            "platform_detail_dimension": [
                                {
                                    "count": 6,
                                    "detail": [
                                        {
                                            "count": 1,
                                            "industry_display_name": "一般消费分期平台"
                                        },
                                        {
                                            "count": 1,
                                            "industry_display_name": "银行消费金融公司"
                                        },
                                        {
                                            "count": 1,
                                            "industry_display_name": "网上银行"
                                        },
                                        {
                                            "count": 1,
                                            "industry_display_name": "小额贷款公司"
                                        },
                                        {
                                            "count": 1,
                                            "industry_display_name": "大型消费金融公司"
                                        },
                                        {
                                            "count": 1,
                                            "industry_display_name": "综合类电商平台"
                                        }
                                    ],
                                    "dimension": "租赁人身份证"
                                },
                                {
                                    "count": 1,
                                    "detail": [
                                        {
                                            "count": 1,
                                            "industry_display_name": "一般消费分期平台"
                                        }
                                    ],
                                    "dimension": "租赁人手机"
                                }
                            ],
                            "platform_detail": [
                                {
                                    "count": 1,
                                    "industry_display_name": "一般消费分期平台"
                                },
                                {
                                    "count": 1,
                                    "industry_display_name": "银行消费金融公司"
                                },
                                {
                                    "count": 1,
                                    "industry_display_name": "网上银行"
                                },
                                {
                                    "count": 1,
                                    "industry_display_name": "小额贷款公司"
                                },
                                {
                                    "count": 1,
                                    "industry_display_name": "大型消费金融公司"
                                },
                                {
                                    "count": 1,
                                    "industry_display_name": "综合类电商平台"
                                }
                            ],
                            "description": "在指定时间内，主属性关联的合作方或行业类型的个数",
                            "type": "platform_detail",
                            "platform_count": 6
                        }
                    ]
                },
                {
                    "rule_id": 34611884,
                    "policy_score": 25,
                    "score": 5,
                    "policy_mode": "Weighted",
                    "decision": "Accept",
                    "policy_decision": "Review",
                    "policy_name": "信用租赁_安卓",
                    "risk_name": "手机号命中中风险关注名单",
                    "risk_detail": [
                        {
                            "hit_type_display_name": "租赁人手机",
                            "fraud_type_display_name": "信用异常、异常借款",
                            "grey_list_details": [
                                {
                                    "evidence_time": 1519054750000,
                                    "risk_level": "中",
                                    "fraud_type": "creditSuspicious",
                                    "fraud_type_display_name": "信用异常",
                                    "value": "15934177737"
                                },
                                {
                                    "evidence_time": 1523851281000,
                                    "risk_level": "中",
                                    "fraud_type": "suspiciousLoan",
                                    "fraud_type_display_name": "异常借款",
                                    "value": "15934177737"
                                }
                            ],
                            "description": "验证匹配字段是否在关注名单中",
                            "type": "grey_list"
                        }
                    ]
                }
            ],
            "final_decision": "REVIEW"
        }
    }
}
'''

result = json.loads(result)
