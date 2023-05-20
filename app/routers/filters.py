from app.database import session
from app.models import Cabin, BookingClass

from fastapi import Query, APIRouter
from sqlalchemy import distinct, func

router = APIRouter(prefix='/api/v1/filters', tags=['filters'])


@router.get("/directions/")
async def get_directions():
    """Направления рейсов"""
    try:
        query = session.query(Cabin.SEG_ORIG, Cabin.SEG_DEST).distinct().all()
        city = get_city_by_airport_code()

        flight_directions = [f'{city.get(orig.strip(), " ")} - {city.get(dest.strip(), " ")}' for orig, dest in
                             query]

        return {'status': 200, 'directions': flight_directions}
    except Exception as e:
        return {'status': 500, 'error': str(e)}


@router.get("/flight_numbers/")
async def get_flight_numbers(
        direction: str = Query(..., description='Направление рейс', example="Москва - Сочи"),
):
    """
    Номера рейсов
    """

    try:
        departure_airport, arrival_airport = get_airport_code_direction(direction)

        query = session.query(distinct(Cabin.FLT_NUM)).filter(
            func.trim(Cabin.SEG_ORIG) == departure_airport.strip(),
            func.trim(Cabin.SEG_DEST) == arrival_airport.strip()
        ).all()

        flights = [row[0] for row in query]

        return {'status': 200, 'flight_numbers': flights}

    except Exception as e:
        return {'status': 500, 'error': str(e)}


@router.get("/booking_classes")
async def get_booking_classes():
    """Классы бронирования"""
    query = session.query(distinct(BookingClass.SEG_CLASS_CODE)).all()
    classes = [row[0] for row in query]

    return {"status": 200, "booking_classes": classes}


def get_airport_code_direction(direction: str):
    parts = direction.replace('"', '').split('-')
    departure_city, arrival_city = [part for part in parts]

    airports = get_airport_by_city()

    return airports.get(departure_city.strip()), airports.get(arrival_city.strip())


def get_airport_by_city():
    return {
        "Москва": "SVO",
        "Сочи": "AER",
        "Астрахань": "ASF"
    }


def get_city_by_airport_code():
    return {
        "SVO": "Москва",
        "AER": "Сочи",
        "ASF": "Астрахань",
    }
