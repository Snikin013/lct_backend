from datetime import date

from fastapi import Query, APIRouter

router = APIRouter(prefix='/api/v1/calculation', tags=['calculation'])

sample_data = {
    "series": [
        {
            "name": "TEAM A",
            "type": "column",
            "data": [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
        },
        {
            "name": "TEAM B",
            "type": "area",
            "data": [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
        },
        {
            "name": "TEAM C",
            "type": "line",
            "data": [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
        },
    ],
}


@router.get("/booking-dynamics")
async def get_booking_dynamics(
        direction: str = Query(..., description="Направление рейса", example="Москва - Сочи"),
        flight_number: int = Query(..., description="Номер рейса", example="1120"),
        flight_date: date = Query(..., description="Дата рейса", example="2018-05-29"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_period: int = Query(1, description="Период прогнозирования спроса для рейса (в месяцах)", example='1'),

        booking_start: date = Query(..., description="Период для просмотра динамики бронирования стартовая дата",
                                    example='2018-05-29'),
        booking_end: date = Query(..., description="Период для просмотра динамики бронирования конечная дата",
                                  example='2019-12-31')
):
    """
    Определение динамики бронирований рейса в разрезе
    классов бронирования по вылетевшим рейсам.
    """
    return sample_data


@router.get("/seasonality")
async def get_seasonality(
        direction: str = Query(..., description="Направление рейса", example="Москва - Сочи"),
        flight_number: str = Query(..., description="Номер рейса", example="1120"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_start: date = Query(..., description="Период для просмотра динамики бронирования стартовая дата",
                                    example='2018-05-29'),
        booking_end: date = Query(..., description="Период для просмотра динамики бронирования конечная дата",
                                  example='2019-12-31')
):
    """
    Определение сезонности спроса по классам бронирования, по вылетевшим рейсам.
    """

    return sample_data


@router.get("/demand-profile")
async def get_demand_profile(
        direction: str = Query(..., description="Направление рейса", example="Москва - Сочи"),
        flight_number: str = Query(..., description="Номер рейса", example="1120"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_start: date = Query(..., description="Период для просмотра динамики бронирования стартовая дата",
                                    example='2018-05-29'),
        booking_end: date = Query(..., description="Период для просмотра динамики бронирования конечная дата",
                                  example='2019-12-31')
):
    """
    Определение профилей спроса в разрезе классов бронирования, по вылетевшим рейсам.
    """
    return sample_data


@router.get("/demand-forecast")
async def get_demand_forecast(
        direction: str = Query(..., description="Направление рейса", example="Москва - Сочи"),
        flight_number: str = Query(..., description="Номер рейса", example="1120"),
        booking_start: date = Query(..., description="Период для просмотра динамики бронирования стартовая дата",
                                    example='2018-05-29'),
        booking_end: date = Query(..., description="Период для просмотра динамики бронирования конечная дата",
                                  example='2019-12-31')
):
    """
    Прогнозирование спроса в разрезе классов бронирования для продаваемых рейсов.
    """

    return sample_data
