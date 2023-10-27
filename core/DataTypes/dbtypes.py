from aiogram.filters.callback_data import CallbackData
from dataclasses import dataclass


class BookingSelectionCallback(CallbackData, prefix="selection"):
    state: str
    court: int
    day: int
    time: int

# @dataclass
# class Badges_table:
#     badge_id: int
#     badge_name: str
#     badge_preview: str

# @dataclass
# class User_table:
#     user_id: int
#     user_name: str
#     user_register_date: str  # Consider using a proper date type
#     user_rating: float
#     user_view_badge: int
#     user_banned: bool
#     user_strikes: int

# @dataclass
# class UserBadges_table:
#     user_id: int
#     badge_id: int

# @dataclass
# class Time_table:
#     time_id: int
#     time_name: str

# @dataclass
# class Courts_table:
#     court_id: int
#     court_name: str
#     court_location: str

# @dataclass
# class Days_table:
#     day_id: int
#     day_date: str

# @dataclass
# class Booking_table:
#     book_id: int
#     court_id: int
#     user_id: int
#     book_day: int
#     book_time: int
