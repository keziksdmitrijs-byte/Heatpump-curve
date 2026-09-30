import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig
from .const import *
class Flow(config_entries.ConfigFlow, domain=DOMAIN):
 VERSION=1
 async def async_step_user(self,user_input=None):
  if user_input: return self.async_create_entry(title=user_input["name"],data=user_input)
  schema=vol.Schema({vol.Required("name",default="Heat pump curve"):str,vol.Required(CONF_OUTDOOR_ENTITY):EntitySelector(EntitySelectorConfig(domain="sensor",device_class="temperature")),vol.Optional(CONF_TARGET_ENTITY):EntitySelector(EntitySelectorConfig(domain=["number","input_number","sensor"])),vol.Required(CONF_MIN_TEMP,default=25):vol.Coerce(float),vol.Required(CONF_MAX_TEMP,default=55):vol.Coerce(float),vol.Required(CONF_STEP,default=5):vol.All(vol.Coerce(float),vol.Range(min=1)),vol.Required(CONF_POINTS,default="-20:55,-10:49,0:43,10:35,15:30"):str})
  return self.async_show_form(step_id="user",data_schema=schema)
