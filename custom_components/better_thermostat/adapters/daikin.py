import asyncio
import logging

from .generic import (
    set_hvac_mode as generic_set_hvac_mode,
    set_temperature as generic_set_temperature,
)

_LOGGER = logging.getLogger(__name__)


async def get_info(self, entity_id):
    """Get info from TRV."""
    _LOGGER.debug(
        f"better_thermostat {self.name}: get_info {entity_id}"
    )
    return {"support_offset": True, "support_valve": False}


async def init(self, entity_id):
    _LOGGER.debug(
        f"better_thermostat {self.name}: init {entity_id}"
    )
    return None


async def get_current_offset(self, entity_id):
    _LOGGER.debug(
        f"better_thermostat {self.name}: get_current_offset {entity_id}"
    )
    """Get current offset."""
    return None


async def get_offset_steps(self, entity_id):
    """Get offset steps."""
    _LOGGER.debug(
        f"better_thermostat {self.name}: get_offset_steps {entity_id}"
    )
    return float(0.5)


async def set_temperature(self, entity_id, temperature):
    """Set new target temperature."""
    _LOGGER.debug(
        f"better_thermostat {self.name}: set_temperature {entity_id}: {temperature}"
    )
    return await generic_set_temperature(self, entity_id, temperature)


async def set_hvac_mode(self, entity_id, hvac_mode):
    """Set new target hvac mode."""
    _LOGGER.debug(
        f"better_thermostat {self.name}: set_hvac_mode {entity_id}: {hvac_mode}"
    )
    await generic_set_hvac_mode(self, entity_id, hvac_mode)
    await asyncio.sleep(5)


async def set_offset(self, entity_id, offset):
    """Set new target offset."""
    _LOGGER.debug(
        f"better_thermostat {self.name}: set_offset {entity_id}: {offset}"
    )
    return  # Not supported


async def set_valve(self, entity_id, valve):
    """Set new target valve."""
    _LOGGER.debug(
        f"better_thermostat {self.name}: set_valve {entity_id}: {valve}"
    )
    return  # Not supported
