def process_result_dynamic_multiple_data(
        series_data: list, dates_receipt: list
) -> dict:
    """
    Формирование данных для построения графика
    динамики с множественным выбором.
    """

    data = {
        "series": series_data[0]['series'],

        "chart_options":
            {
                "chart": {
                    "height": 500,
                    "type": "line",
                    "stacked": False,
                },
                "dataLabels": {
                    "enabled": False,
                },
                "stroke": {
                    "width": [5, 5, 5, 5, 3],
                    "curve": "straight",
                },
                "colors": ["#02458d", "#f37b09", "#ce003d", "#8a8b99"],
                "grid":
                    {
                        "borderColor": "#e7e7e7",
                        "row": {
                            "colors": ["#f3f3f3", "transparent"],
                            "opacity": 0.5,
                        },
                    },

                "xaxis": {
                    "type": "datetime",
                    "categories": dates_receipt,
                },
                "yaxis": [
                    {
                        "show": True,
                        "showAlways": False,
                        "showForNullSeries": True,
                        "opposite": False,
                        "reversed": False,
                        "logarithmic": False,
                        "logBase": 10,
                        "tickAmount": 10,
                        "forceNiceScale": False,
                        "floating": False,
                        "labels": {
                            "show": True,
                            "minWidth": 0,
                            "maxWidth": 160,
                            "offsetX": 0,
                            "offsetY": 0,
                            "rotate": 0,
                            "padding": 20,
                            "style": {
                                "colors": "black",
                                "fontSize": "11px",
                                "fontWeight": 400,
                                "cssClass": "",
                            },
                            "tooltip": {
                                "enabled": True,
                            },
                        },
                        "axisBorder": {
                            "show": True,
                            "color": "black",
                            "width": 1,
                            "offsetX": 0,
                            "offsetY": 0,
                        },
                        "axisTicks": {
                            "show": True,
                            "color": "black",
                            "width": 6,
                            "offsetX": 0,
                            "offsetY": 0,
                        },
                        "title": {
                            "rotate": -90,
                            "offsetY": 0,
                            "offsetX": 0,
                            "style": {
                                "fontSize": "11px",
                                "fontWeight": 900,
                                "cssClass": "",
                            },
                        },
                    },
                ],
                "tooltip": {
                    "enabled": True,
                    "shared": True,
                    "intersect": False,
                    "followCursor": True,
                    "marker": {
                        "show": False,
                    },
                    "x": {
                        "format": "dd MMM yyyy",
                    },
                    "fixed": {
                        "enabled": True,
                        "position": "topLeft",
                        "offsetY": 30,
                        "offsetX": 60,
                    },
                },
                "legend": {
                    "horizontalAlign": "left",
                    "offsetX": 40,
                    "fontSize": "17px",
                },
            },
    }

    return data


def process_result_dynamic_single_data(
        series_data: list, dates_receipt: list
) -> dict:
    """
    Формирование данных для построения графика динамики
    с одиночным выбором.
    """

    data = {
        "series": series_data[0]['series'],
        "chart_options": {
            "chart": {
                "height": 500,
                "type": "line",
                "stacked": False,
            },
            "dataLabels": {
                "enabled": False,
            },
            "stroke": {
                "width": [6, 1, 3],
                "curve": "straight",
            },
            "colors": ["#f37b09", "#02458d"],
            "grid": {
                "borderColor": "#e7e7e7",
                "row": {
                    "colors": ["#f3f3f3", "transparent"],
                    "opacity": 0.5,
                },
            },

            "xaxis": {
                "type": "datetime",
                "categories": dates_receipt,
            },
            "yaxis": [
                {
                    "axisTicks": {
                        "show": True,
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#f37b09",
                    },
                    "labels": {
                        "style": {
                            "colors": "#f37b09",
                        },
                    },
                    "tooltip": {
                        "enabled": True,
                    },
                },
                {
                    "opposite": True,
                    "axisTicks": {
                        "show": True,
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#02458d",
                    },
                    "labels": {
                        "style": {
                            "colors": "#02458d",
                        },
                    },
                    "tooltip": {
                        "enabled": True,
                    },
                },
            ],
            "tooltip": {
                "enabled": True,
                "shared": True,
                "intersect": False,
                "followCursor": True,
                "marker": {
                    "show": False,
                },
                "x": {
                    "format": "dd MMM yyyy",
                },
                "fixed": {
                    "enabled": True,
                    "position": "topLeft",
                    "offsetY": 30,
                    "offsetX": 60,
                },
            },
            "legend": {
                "horizontalAlign": "left",
                "offsetX": 40,
                "fontSize": "17px",
            },
        },
    }

    return data


def process_result_season_data(
        series_data: list, dates_receipt: list
) -> dict:
    """
    Формирование данных для построения графика сезонов.
    """
    data = {
        "graph": {
            "data": {
                "series": [
                    {
                        "name": "TE",
                        "type": "column",
                        "data": [40, 40, 30, 23, 59, 46, 20, 35, 45],
                    },
                    {
                        "name": "Servings",
                        "type": "line",
                        "data": [0, 10, 20, 30, 22, 43, 21, 33, 45],
                    },
                ],
                "chart_options": {
                    "annotations": {
                        "points": [
                            {
                                "x": "Январь",
                                "seriesIndex": 0,
                                "label": {
                                    "borderColor": "#775DD0",
                                    "offsetY": 0,
                                    "style": {
                                        "color": "#fff",
                                        "background": "#775DD0",
                                    },
                                    "text": "Зимний",
                                },
                            },
                            {
                                "x": "Февраль",
                                "seriesIndex": 0,
                                "label": {
                                    "borderColor": "#775DD0",
                                    "offsetY": 0,
                                    "style": {
                                        "color": "#fff",
                                        "background": "#775DD0",
                                    },
                                    "text": "Зимний",
                                },
                            },
                        ],
                    },
                    "chart": {
                        "height": 500,
                        "type": "bar",
                    },
                    "plotOptions": {
                        "bar": {
                            "borderRadius": 10,
                            "columnWidth": "100%",
                        },
                    },
                    "dataLabels": {
                        "enabled": False,
                    },
                    "stroke": {
                        "width": [1, 6, 3],
                        "curve": "straight",
                    },
                    "colors": ["#02458d", "#f37b09", "#237es9"],
                    "grid": {
                        "row": {
                            "colors": ["#fff", "#f2f2f2"],
                        },
                    },
                    "xaxis": {
                        "labels": {
                            "rotate": -45,
                        },
                        "categories": [
                            "Январь",
                            "Февраль",
                            "Март",
                            "Апрель",
                            "Май",
                            "Июнь",
                            "Июль",
                            "Август",
                            "Сентябрь",
                        ],
                    },
                    "yaxis": {
                        "title": {
                            "text": "Servings",
                        },
                    },
                    "fill": {
                        "type": "gradient",
                        "gradient": {
                            "shade": "light",
                            "type": "horizontal",
                            "shadeIntensity": 0.25,
                            "gradientToColors": "undefined",
                            "inverseColors": True,
                            "opacityFrom": 0.85,
                            "opacityTo": 0.85,
                            "stops": [50, 0, 100],
                        },
                    },
                },
            },
        },
    }

    return data


def process_result_demand_forecast_data(dates_receipt, increments_days, pass_bks):
    """
    Формирование данных для построения графика предсказаний.
    """
    data = {
        "series": [
            {
                "name": "Бронирование за день",
                "type": "column",
                "data": increments_days,
            },
            {
                "name": "Суммарное бронирование",
                "type": "line",
                "data": pass_bks,
            },
        ],
        "chart_options": {
            "chart": {
                "height": 350,
                "type": "line",
                "stacked": False,
            },
            "dataLabels": {
                "enabled": False,
            },
            "stroke": {
                "width": [1, 6, 3],
                "curve": "straight",
            },
            "colors": ["#02458d", "#f37b09"],
            "grid": {
                "borderColor": "#e7e7e7",
                "row": {
                    "colors": ["#f3f3f3", "transparent"],
                    "opacity": 0.5,
                },
            },
            "title": {
                "text": "Динамика бронирования рейса",
                "align": "left",
                "offsetX": 110,
            },
            "xaxis": {
                "categories": dates_receipt,
            },
            "yaxis": [
                {
                    "axisTicks": {
                        "show": True,
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#02458d",
                    },
                    "labels": {
                        "style": {
                            "colors": "#02458d",
                        },
                    },
                    "tooltip": {
                        "enabled": "true",
                    },
                },
                {
                    "opposite": True,
                    "axisTicks": {
                        "show": True,
                        "color": "#f37b09",
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#f37b09",
                    },
                    "labels": {
                        "style": {
                            "colors": "#f37b09",
                        },
                    },
                },
            ],
            "tooltip": {
                "fixed": {
                    "enabled": True,
                    "position": "topLeft",
                    "offsetY": 30,
                    "offsetX": 60,
                },
            },
            "legend": {
                "horizontalAlign": "left",
                "offsetX": 40,
            },
        },
    }

    return data


def get_fly_numbers_by_direction():
    """Номер рейса в зависимости от маршрута."""
    data = {
        "Сочи - Москва": [
            1117, 1119, 1121, 1123, 1125, 1127, 1129, 1131, 1133, 1135, 1137, 1139, 1141, 1151, 1153,
            1741, 1771, 1773, 1781, 1783, 1785, 1787, 1789, 1791, 1793, 1795, 1797, 1799, 2957, 2981,
            2985, 6180, 6182, 6186
        ],
        "Москва - Сочи": [
            1116, 1118, 1120, 1122, 1124, 1126, 1128, 1130, 1132, 1134, 1136, 1138, 1140, 1148, 1152,
            1740, 1772, 1780, 1782, 1784, 1786, 1788, 1790, 1792, 1794, 1796, 1798, 2980, 2990, 6179,
            6181, 6185
        ],
        "Москва - Астрахань": [1172, 1174, 1642],
        "Астрахань - Москва": [1173, 1175, 1643, 1775],
    }

    return data


def get_fly_directions():
    """Направления полетов."""
    return ['Москва - Сочи', 'Сочи - Москва', 'Москва - Астрахань', 'Астрахань - Москва']
