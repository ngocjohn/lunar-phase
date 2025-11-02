import datetime
import math
import ephem


class MoonScript:
    # Constants kept for backward compatibility
    lunarDaysMs = 29.53058868 * 24 * 60 * 60 * 1000  # mean synodic month in ms
    firstNewMoon2000 = 947178840000  # base reference (Jan 6, 2000 18:14 UTC)

    @staticmethod
    def get_moon_illumination(date: datetime.datetime):
        """Return detailed moon illumination and phase data."""
        observer = ephem.Observer()
        observer.date = date

        moon = ephem.Moon(observer)
        fraction = moon.phase / 100.0

        # Current phase ID (simple classification)
        phase_angle = (moon.phase / 100.0) * 360.0
        if fraction < 0.03:
            phase_id = "new_moon"
        elif 0.03 <= fraction < 0.27:
            phase_id = "waxing_crescent"
        elif 0.27 <= fraction < 0.48:
            phase_id = "first_quarter"
        elif 0.48 <= fraction < 0.52:
            phase_id = "full_moon"
        elif 0.52 <= fraction < 0.73:
            phase_id = "waning_gibbous"
        elif 0.73 <= fraction < 0.97:
            phase_id = "third_quarter"
        else:
            phase_id = "waning_crescent"

        # Get accurate next phases using PyEphem
        next_new = ephem.next_new_moon(date)
        next_first = ephem.next_first_quarter_moon(date)
        next_full = ephem.next_full_moon(date)
        next_third = ephem.next_last_quarter_moon(date)

        # Build output dictionary
        return {
            "fraction": fraction,
            "phaseValue": fraction,
            "phase": {"id": phase_id},
            "next": {
                "newMoon": {
                    "date": next_new.datetime().isoformat() + "Z",
                },
                "firstQuarter": {
                    "date": next_first.datetime().isoformat() + "Z",
                },
                "fullMoon": {
                    "date": next_full.datetime().isoformat() + "Z",
                },
                "thirdQuarter": {
                    "date": next_third.datetime().isoformat() + "Z",
                },
                "type": phase_id,
                "date": next_full.datetime().isoformat() + "Z",
            },
        }

    @staticmethod
    def get_moon_position(date, latitude, longitude):
        """Return moon position data using PyEphem."""
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.date = date

        moon = ephem.Moon(observer)

        return {
            "altitudeDegrees": math.degrees(moon.alt),
            "azimuthDegrees": math.degrees(moon.az),
            "distance": moon.earth_distance * 149597870.7,  # AU → km
            "parallacticAngleDegrees": 0.0,  # not used in PyEphem directly
        }

    @staticmethod
    def get_moon_times(date, latitude, longitude, next_events_only=False):
        """Return rise, set, and highest (transit) times."""
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.date = date

        moon = ephem.Moon()

        try:
            rise = observer.next_rising(moon).datetime()
        except Exception:
            rise = None
        try:
            set_ = observer.next_setting(moon).datetime()
        except Exception:
            set_ = None
        try:
            highest = observer.next_transit(moon).datetime()
        except Exception:
            highest = None

        return {
            "rise": rise,
            "set": set_,
            "highest": highest,
        }