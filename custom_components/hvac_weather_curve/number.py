from homeassistant.components.number import NumberEntity
from homeassistant.const import UnitOfTemperature
from .const import *
async def async_setup_entry(hass,e,add): add([N(e,CONF_MIN_TEMP,"Minimum flow temperature"),N(e,CONF_MAX_TEMP,"Maximum flow temperature"),N(e,CONF_STEP,"Curve adjustment step")],True)
class N(NumberEntity):
 def __init__(self,e,k,n):self.e=e;self.k=k;self._attr_name=n;self._attr_unique_id=e.entry_id+k;self._v=float(e.data[k]);self._attr_native_min_value=0;self._attr_native_max_value=100;self._attr_native_step=1
 @property
 def native_value(self):return self._v
 async def async_set_native_value(self,v):self._v=v
