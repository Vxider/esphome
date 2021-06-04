import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_PAGE_ID, CONF_ID
from . import nextion_ns
from .display import Nextion

DEPENDENCIES = ['display']

CONF_NEXTION_ID = 'nextion_id'

MultiNextionTouchComponent = nextion_ns.class_('MultiNextionTouchComponent', sensor.Sensor)

CONFIG_SCHEMA = sensor.SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(MultiNextionTouchComponent),
    cv.GenerateID(CONF_NEXTION_ID): cv.use_id(Nextion),

    cv.Required(CONF_PAGE_ID): cv.uint8_t,
})


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield sensor.register_sensor(var, config)

    hub = yield cg.get_variable(config[CONF_NEXTION_ID])
    cg.add(hub.register_multi_touch_component(var))

    cg.add(var.set_page_id(config[CONF_PAGE_ID]))
