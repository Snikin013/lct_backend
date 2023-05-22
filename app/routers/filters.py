from enum import Enum
from fastapi import Query, APIRouter
from sqlalchemy import distinct

from app.database import session
from app.models import BookingClass
from app.utils import get_fly_directions, get_fly_numbers_by_direction

router = APIRouter(prefix='/api/v1/filters', tags=['filters'])


@router.get("/directions/")
async def get_directions():
    """Направления рейсов."""
    try:
        # query = session.query(Cabin.SEG_ORIG, Cabin.SEG_DEST).distinct().all()
        # city = get_city_by_airport_code()
        #
        # flight_directions = [f'{city.get(orig.strip(), " ")} - {city.get(dest.strip(), " ")}' for orig, dest in
        #                      query]

        flight_directions = get_fly_directions()

        return {'status': 200, 'directions': flight_directions}
    except Exception as e:
        return {'status': 500, 'error': str(e)}


class UserRoute(str, Enum):
    DYNAMICS = "Динамический"
    SEASONALITY = "Сезонный"
    PROFILE = "Профильный"
    FORECAST = "Прогноз"


@router.get("/flight_numbers/")
async def get_flight_numbers(
        direction: str = Query(..., description='Направление рейс', example="Москва - Сочи"),
        user_route: UserRoute = Query(..., description="Маршрут пользователя")
):
    """
    Номера рейсов
    """

    try:
        # departure_airport, arrival_airport = get_airport_code_direction(direction)
        standard_directions = get_fly_numbers_by_direction()

        if user_route == UserRoute.PROFILE:
            flights = standard_directions.get(direction, None)

            # query = session.query(distinct(BookingBronIncrement.FLT_NUM).filter(
            #     func.trim(Cabin.SEG_ORIG) == departure_airport.strip(),
            #     func.trim(Cabin.SEG_DEST) == arrival_airport.strip()
            # )).all()

        else:
            flights = standard_directions.get(direction, None)

            # query = session.query(distinct(Cabin.FLT_NUM)).filter(
            #     func.trim(Cabin.SEG_ORIG) == departure_airport.strip(),
            #     func.trim(Cabin.SEG_DEST) == arrival_airport.strip()
            # ).all()

        # flights = [row[0] for row in query]

        return {'status': 200, 'flight_numbers': flights}

    except Exception as e:
        return {'status': 500, 'error': str(e)}


@router.get("/booking_classes/")
async def get_booking_classes():
    """Классы бронирования"""
    query = session.query(distinct(BookingClass.SEG_CLASS_CODE)).all()
    classes = [row[0] for row in query]

    return {"status": 200, "booking_classes": classes}
