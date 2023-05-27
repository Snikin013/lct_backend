def process_result_dynamic_data(series_data, dates_receipt):
    """Формирование данных для построения графика."""

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
                "tooltip":
                    {
                        "enabled": True,
                        "offsetX": 0,
                        "crosshairs": {
                            "show": True,
                            "position": "front",
                            "stroke": {
                                "color": "#b6b6b6",
                                "width": 1,
                                "dashArray": 0
                            }
                        },
                        "tooltip": {
                            "fixed": {
                                "enabled": True,
                                "position": "topLeft",
                                "offsetY": 30,
                                "offsetX": 60
                            }
                        },
                        "legend": {
                            "horizontalAlign": "left",
                            "offsetX": 40
                        }
                    }
            },
    }

    return data


def get_airport_by_city():
    """Получение аэропорта по городу."""
    return {
        "Москва": "SVO",
        "Сочи": "AER",
        "Астрахань": "ASF"
    }


def get_city_by_airport_code():
    """Получение города по аэропорту."""
    return {
        "SVO": "Москва",
        "AER": "Сочи",
        "ASF": "Астрахань",
    }


def get_fly_numbers_by_direction():
    """Номер рейса в зависимости от маршрута."""
    data = {
        "Сочи - Москва": [1117, 1119, 1121, 1123, 1125, 1127, 1129, 1131, 1133, 1135, 1137, 1139, 1141, 1151, 1153,
                          1741, 1771, 1773, 1781, 1783, 1785, 1787, 1789, 1791, 1793, 1795, 1797, 1799, 2957, 2981,
                          2985, 6180, 6182, 6186],
        "Москва - Сочи": [1116, 1118, 1120, 1122, 1124, 1126, 1128, 1130, 1132, 1134, 1136, 1138, 1140, 1148, 1152,
                          1740, 1772, 1780, 1782, 1784, 1786, 1788, 1790, 1792, 1794, 1796, 1798, 2980, 2990, 6179,
                          6181, 6185],
        "Москва - Астрахань": [1172, 1174, 1642],
        "Астрахань - Москва": [1173, 1175, 1643, 1775],
    }

    return data


def get_fly_directions():
    """Направления полетов."""
    return ['Москва - Сочи', 'Сочи - Москва', 'Москва - Астрахань', 'Астрахань - Москва']


def get_airport_code_direction(direction: str):
    """Получение кода по аэропорту направления. """
    parts = direction.replace('"', '').split('-')
    departure_city, arrival_city = [part for part in parts]

    airports = get_airport_by_city()

    return airports.get(departure_city.strip()), airports.get(arrival_city.strip())
