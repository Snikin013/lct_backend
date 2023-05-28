from datetime import datetime, timedelta, date
from typing import Optional

from fastapi import Query, APIRouter

from app.database import session
from app.models import BookingBronIncrement, ClassBronSeason
from app.utils import (
    process_result_dynamic_single_data,
    process_result_dynamic_multiple_data,
    process_result_demand_forecast_data,
    process_result_season_data,
)

router = APIRouter(prefix='/api/v1/calculation', tags=['calculation'])


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
        booking_classes = booking_class.replace(" ", "").split(",")

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
            BookingBronIncrement.SEG_CLASS_CODE.in_(booking_classes),
            BookingBronIncrement.SDAT_S.between(booking_period_start_date, booking_period_end_date),
            BookingBronIncrement.DTD >= 0,

        )

        dates_receipt = []
        increments_days = []
        for result in query.all():
            sdat_s = result.SDAT_S
            increments_day = result.Increment_day

            increments_days.append(increments_day)
            dates_receipt.append(sdat_s)

        if not dates_receipt or not increments_days:
            return {'status': 400, 'error': 'Некорректные данные. Один или несколько списков пустые.'}

        series_data = [{'series': []}]

        for booking_class in booking_classes:

            pass_query = query.filter(
                BookingBronIncrement.SEG_CLASS_CODE == booking_class,
                BookingBronIncrement.DTD >= 0,
            )

            pass_bks = [result.PASS_BK for result in pass_query.all()]

            if pass_bks:
                series_data[0]['series'].append({
                    'name': f'Суммарное бронирование {booking_class}',
                    'type': 'line',
                    'data': pass_bks
                })
            else:
                series_data[0]['series'].append({
                    'name': f'Данных для класс {booking_class} не найдено',
                    'type': 'line',
                    'data': [0, 0, 0, 0, 0, 0, 0, 0]
                })

        if len(booking_classes) == 1:
            series_data[0]['series'].append({
                'name': 'Бронирование за день',
                'type': 'column',
                'data': increments_days
            })
            res_data = process_result_dynamic_single_data(series_data, dates_receipt)
        else:
            res_data = process_result_dynamic_multiple_data(series_data, dates_receipt)

        return {'status': 200, "data": res_data}

    except Exception as e:
        return {'status': 500, "error": str(e)}


@router.get("/seasonality")
async def get_seasonality(
        flight_number: str = Query(..., description="Номер рейса", example="1120"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_start: Optional[date] = Query(...,
                                              description="Период для просмотра стартовая дата",
                                              example='2018-05-29'),
        booking_end: Optional[date] = Query(...,
                                            description="Период для просмотра конечная дата",
                                            example='2019-12-31')

):
    """
    Определение динамики бронирований рейса в разрезе
    классов бронирования по вылетевшим рейсам.
    """
    try:

        query = session.query(
            ClassBronSeason.SDAT_S,
            ClassBronSeason.Increment_day,
        )

        query = query.filter(
            ClassBronSeason.FLT_NUM == flight_number,
            ClassBronSeason.SEG_CLASS_CODE == booking_class,
            ClassBronSeason.SDAT_S.between(booking_start, booking_end)
        )

        dates_receipt = []
        increments_days = []

        for result in query.all():
            sdat_s = result.SDAT_S
            increment_day = result.Increment_day

            dates_receipt.append(sdat_s)
            increments_days.append(increment_day)

        if not dates_receipt or not increments_days:
            return {'status': 400, 'error': 'Некорректные данные. Один или несколько списков пустые.'}

        res_data = process_result_season_data(dates_receipt, increments_days)

        return {'status': 200, "data": res_data}

    except Exception as e:
        return {'status': 500, 'error': str(e)}


@router.get("/demand-forecast")
async def get_demand_forecast(
        flight_number: int = Query(..., description="Номер рейса", example="1120"),
        flight_date: str = Query(..., description="Дата рейса", example="2018-05-29"),
        booking_class: str = Query(..., description="Класс бронирования", example="Y"),
        booking_period: Optional[int] = Query(1, ge=1, le=12,
                                              description="Период прогнозирования спроса для рейса (в месяцах)",
                                              example='1'),
):
    """
    Прогнозирование спроса в разрезе классов бронирования для продаваемых рейсов.
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

        res_data = process_result_demand_forecast_data(dates_receipt, increments_days, pass_bks)

        return {'status': 200, "data": res_data}

    except Exception as e:
        return {'status': 500, "error": str(e)}


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
    pass
