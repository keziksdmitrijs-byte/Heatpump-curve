import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, CONF_MIN_TEMP, CONF_MAX_TEMP, CONF_STEP, CONF_POINTS
class Flow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION=1
    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title=user_input.get("name", "Weather curve"), data=user_input)
        schema=vol.Schema({vol.Required("name", default="Weather curve"): str,
            vol.Required(CONF_MIN_TEMP, default=25): vol.Coerce(float),
            vol.Required(CONF_MAX_TEMP, default=55): vol.Coerce(float),
            vol.Required(CONF_STEP, default=5): vol.All(vol.Coerce(float), vol.Range(min=0.1)),
            vol.Required(CONF_POINTS, default="-20:55,-15:52,-10:49,-5:46,0:43,5:40,10:35,15:30"): str})
        return self.async_show_form(step_id="user", data_schema=schema)
