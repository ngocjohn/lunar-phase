"""The Moon Phase integration."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry, ConfigEntryNotReady
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_change

from .const import DOMAIN
from .coordinator import MoonUpdateCoordinator
from .moon import MoonCalc

_LOGGER = logging.getLogger(__name__)

# List the platforms that you want to support.
PLATFORMS = [
    Platform.SENSOR,
]
RELOAD_TASKS = {}


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up Moon Phase from a config entry."""

    hass.data.setdefault(DOMAIN, {})

    moon = MoonCalc(
        hass=hass,
        city=config_entry.data["city"],
        region=config_entry.data["region"],
        latitude=config_entry.data["latitude"],
        longitude=config_entry.data["longitude"],
        timezone=config_entry.data["time_zone"],
    )

    try:
        await hass.async_add_executor_job(moon.set_location)

        coordinator = MoonUpdateCoordinator(hass, moon)

        # Fetch initial data to ensure the coordinator is working
        await coordinator.async_config_entry_first_refresh()

        hass.data[DOMAIN][config_entry.entry_id] = {
            "coordinator": coordinator,
            "moon_calc": moon,
        }

        # Schedule a midnight reload
        async_track_time_change(
            hass,
            lambda _: hass.loop.call_soon_threadsafe(
                schedule_reload_once, hass, config_entry
            ),
            hour=0,
            minute=0,
            second=0,
        )

        await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)

    except Exception as err:
        _LOGGER.error("Error setting up Moon Phase: %s", err, exc_info=True)  # noqa: G201
        raise ConfigEntryNotReady from err

    return True


def schedule_reload_once(hass: HomeAssistant, config_entry: ConfigEntry) -> None:
    """Ensure reload is scheduled only once."""
    if config_entry.entry_id in RELOAD_TASKS:
        _LOGGER.debug("Reload already scheduled for entry: %s", config_entry.entry_id)
        return

    # Schedule the reload task
    task = hass.async_create_task(log_and_reload(hass, config_entry))
    RELOAD_TASKS[config_entry.entry_id] = task

    # Remove the task from tracking once done
    task.add_done_callback(lambda _: RELOAD_TASKS.pop(config_entry.entry_id, None))


async def log_and_reload(hass: HomeAssistant, config_entry: ConfigEntry) -> None:
    """Log and reload the integration."""
    _LOGGER.info("Reloading Moon Phase integration for: %s", config_entry.data["city"])
    await hass.config_entries.async_reload(config_entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.debug("Unloading entry: %s", config_entry.data["city"])
    unload_ok = await hass.config_entries.async_unload_platforms(
        config_entry, PLATFORMS
    )

    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)
        _LOGGER.debug("Successfully unloaded entry: %s", config_entry.data["city"])

    return unload_ok
