from homeassistant.helpers.entity import SensorEntity
from homeassistant.const import UnitOfTemperature
from .const import DOMAIN, CONF_MIN_TEMP, CONF_MAX_TEMP, CONF_STEP, CONF_POINTS

def parse_points(s):
    out=[]
    for p in s.split(","):
        a,b=p.strip().split(":"); out.append((float(a),float(b)))
    return sorted(out)
def interpolate(points,x):
    if x<=points[0][0]: return points[0][1]
    if x>=points[-1][0]: return points[-1][1]
    for (x1,y1),(x2,y2) in zip(points,points[1:]):
        if x1<=x<=x2: return y1+(y2-y1)*(x-x1)/(x2-x1)
async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([CurveSensor(entry)], True)
class CurveSensor(SensorEntity):
    _attr_native_unit_of_measurement=UnitOfTemperature.CELSIUS
    _attr_has_entity_name=True
    def __init__(self,e):
        self.entry=e; self._attr_name="Flow temperature"; self._attr_unique_id=e.entry_id+"_flow"; self._value=None
        self.points=parse_points(e.data[CONF_POINTS])
    async def async_update(self):
        weather=self.hass.states.get("sensor.outdoor_temperature")
        if weather and weather.state not in ("unknown","unavailable"):
            v=interpolate(self.points,float(weather.state)); d=self.entry.data
            v=max(float(d[CONF_MIN_TEMP]),min(float(d[CONF_MAX_TEMP]),v)); self._value=round(v)
    @property
    def native_value(self): return self._value
    @property
    def extra_state_attributes(self): return {"outdoor_temperature_entity":"sensor.outdoor_temperature","curve_points":self.entry.data[CONF_POINTS],"configured_step":self.entry.data[CONF_STEP]}
