from datetime import datetime, timedelta, date
from typing import Optional

from fastapi import Query, APIRouter

from app.database import session
from app.utils import process_result_data
from app.models import BookingBronIncrement

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
        flight_number: int = Query(..., description="Номер рейса", example="1120"),
        flight_date: str = Query(..., description="Дата рейса", example="2018-05-29"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_period: Optional[int] = Query(1, ge=1, le=12,
                                              description="Период прогнозирования спроса для рейса (в месяцах)",
                                              example='1'),
):
    """
    Определение динамики бронирований рейса в разрезе
    классов бронирования по вылетевшим рейсам.
    """
    try:
        flight_date_obj = datetime.strptime(flight_date, "%Y-%m-%d").date()

        booking_period_start_date = flight_date_obj - timedelta(days=booking_period * 30)
        booking_period_end_date = flight_date_obj

        query = session.query(
            BookingBronIncrement.SDAT_S,
            BookingBronIncrement.Increment_day,
            BookingBronIncrement.PASS_BK,
        )

        query = query.filter(
            BookingBronIncrement.FLT_NUM == flight_number,
            BookingBronIncrement.DD == flight_date,
            BookingBronIncrement.SEG_CLASS_CODE == booking_class,
            BookingBronIncrement.SDAT_S.between(booking_period_start_date, booking_period_end_date),
        )

        dates_receipt = []
        increments_days = []
        pass_bks = []

        for result in query.all():
            sdat_s = result.SDAT_S
            increment_day = result.Increment_day
            pass_bk = result.PASS_BK

            dates_receipt.append(sdat_s)
            increments_days.append(increment_day)
            pass_bks.append(pass_bk)

        res_data = process_result_data(dates_receipt, increments_days, pass_bks)

        return {'status': 200, "data": res_data}

    except Exception as e:
        return {'status': 500, "error": str(e)}


@router.get("/seasonality")
async def get_seasonality(
        direction: str = Query(..., description="Направление рейса", example="Москва - Сочи"),
        flight_number: str = Query(..., description="Номер рейса", example="1120"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_start: Optional[date] = Query(None,
                                              description="Период для просмотра динамики бронирования стартовая дата",
                                              example='2018-05-29'),
        booking_end: Optional[date] = Query(None,
                                            description="Период для просмотра динамики бронирования конечная дата",
                                            example='2019-12-31')
):
    """
    Определение динамики бронирований рейса в разрезе
    классов бронирования по вылетевшим рейсам.
    """
    return sample_data


@router.get("/demand-profile")
async def get_demand_profile(
        direction: str = Query(..., description="Направление рейса", example="Москва - Сочи"),
        flight_number: str = Query(..., description="Номер рейса", example="1120"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_start: Optional[date] = Query(None,
                                              description="Период для просмотра динамики бронирования стартовая дата",
                                              example='2018-05-29'),
        booking_end: Optional[date] = Query(None,
                                            description="Период для просмотра динамики бронирования конечная дата",
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
        booking_start: Optional[date] = Query(None,
                                              description="Период для просмотра динамики бронирования стартовая дата",
                                              example='2018-05-29'),
        booking_end: Optional[date] = Query(None,
                                            description="Период для просмотра динамики бронирования конечная дата",
                                            example='2019-12-31')
):
    """
    Прогнозирование спроса в разрезе классов бронирования для продаваемых рейсов.
    """

    return sample_data
