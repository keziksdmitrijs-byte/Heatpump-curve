from homeassistant.components.number import NumberEntity
from homeassistant.const import UnitOfTemperature
from .const import DOMAIN, CONF_MIN_TEMP, CONF_MAX_TEMP, CONF_STEP
async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([Setting(entry,CONF_MIN_TEMP,"Minimum flow temperature"),Setting(entry,CONF_MAX_TEMP,"Maximum flow temperature"),Setting(entry,CONF_STEP,"Adjustment step")], True)
class Setting(NumberEntity):
    def __init__(self,e,key,name): self.e=e; self.key=key; self._attr_name=name; self._attr_unique_id=e.entry_id+"_"+key; self._value=float(e.data[key]); self._attr_native_min_value=0; self._attr_native_max_value=100; self._attr_native_step=1 if key!=CONF_STEP else .5; self._attr_native_unit_of_measurement=UnitOfTemperature.CELSIUS
    @property
    def native_value(self): return self._value
    async def async_set_native_value(self,value): self._value=value
