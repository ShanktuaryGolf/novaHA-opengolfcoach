"""Constants for the NOVA by Open Launch integration."""
from __future__ import annotations

from dataclasses import dataclass
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfSpeed,
    UnitOfTime,
    DEGREE,
    REVOLUTIONS_PER_MINUTE,
)

DOMAIN = "nova_by_openlaunch"

DEFAULT_PORT = 2920
RECONNECT_INTERVAL = 10  # seconds

# SSDP Discovery
SSDP_ST = "urn:openlaunch:service:websocket:1"

CONF_HOST = "host"
CONF_PORT = "port"
CONF_NAME = "name"

# Device info from SSDP
CONF_MANUFACTURER = "manufacturer"
CONF_MODEL = "model"
CONF_SERIAL = "serial"


@dataclass(frozen=True)
class NovaByOpenLaunchSensorEntityDescription(SensorEntityDescription):
    """Describes a NOVA by Open Launch sensor entity."""

    json_key: str | None = None
    message_type: str | None = None  # "shot" or "status"
    precision: int | None = None  # Number of decimal places (None = no rounding)
    value_offset: int = 0  # Add this to the raw value (e.g., +1 for 0-indexed counts)


# Shot Data Sensors (from "type": "shot" messages)
SHOT_SENSORS: tuple[NovaByOpenLaunchSensorEntityDescription, ...] = (
    NovaByOpenLaunchSensorEntityDescription(
        key="session_shot_count",
        name="Session Shot Count",
        state_class=SensorStateClass.TOTAL_INCREASING,
        icon="mdi:counter",
        json_key="shot_number",
        message_type="shot",
        value_offset=1,  # shot_number is 0-indexed, display as 1-indexed
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="last_shot_time",
        name="Last Shot",
        device_class=SensorDeviceClass.TIMESTAMP,
        icon="mdi:clock-outline",
        json_key="_last_shot_timestamp",  # Special: set by coordinator
        message_type="shot",
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ball_speed",
        name="Ball Speed",
        native_unit_of_measurement=UnitOfSpeed.METERS_PER_SECOND,
        device_class=SensorDeviceClass.SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="ball_speed_meters_per_second",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="vertical_launch_angle",
        name="Vertical Launch Angle",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        icon="mdi:angle-acute",
        json_key="vertical_launch_angle_degrees",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="horizontal_launch_angle",
        name="Horizontal Launch Angle",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        icon="mdi:angle-acute",
        json_key="horizontal_launch_angle_degrees",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="total_spin",
        name="Total Spin",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        icon="mdi:rotate-right",
        json_key="total_spin_rpm",
        message_type="shot",
        precision=0,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="spin_axis",
        name="Spin Axis",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        icon="mdi:axis-arrow",
        json_key="spin_axis_degrees",
        message_type="shot",
        precision=0,
    ),
)

# OpenGolfCoach Derived Sensors (from "type": "shot" messages, processed by opengolfcoach)
OPEN_GOLF_COACH_SENSORS: tuple[NovaByOpenLaunchSensorEntityDescription, ...] = (
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_carry_distance_meters",
        name="OGC Carry Distance",
        native_unit_of_measurement="m", # Home Assistant does not have a UnitOfLength.METERS constant, using string
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="carry_distance_meters",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_total_distance_meters",
        name="OGC Total Distance",
        native_unit_of_measurement="m",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="total_distance_meters",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_offline_distance_meters",
        name="OGC Offline Distance",
        native_unit_of_measurement="m",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="offline_distance_meters",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_peak_height_meters",
        name="OGC Peak Height",
        native_unit_of_measurement="m",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="peak_height_meters",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_descent_angle",
        name="OGC Descent Angle",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        icon="mdi:angle-acute",
        json_key="descent_angle_degrees",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_hang_time",
        name="OGC Hang Time",
        native_unit_of_measurement=UnitOfTime.SECONDS,
        device_class=SensorDeviceClass.DURATION,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="hang_time_seconds",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_club_speed",
        name="OGC Club Speed",
        native_unit_of_measurement=UnitOfSpeed.METERS_PER_SECOND,
        device_class=SensorDeviceClass.SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="club_speed_meters_per_second",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_smash_factor",
        name="OGC Smash Factor",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=2,
        icon="mdi:golf-tee",
        json_key="smash_factor",
        message_type="shot",
        precision=2,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_backspin",
        name="OGC Backspin",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        icon="mdi:rotate-right",
        json_key="backspin_rpm",
        message_type="shot",
        precision=0,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_sidespin",
        name="OGC Sidespin",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        icon="mdi:rotate-3d-variant",
        json_key="sidespin_rpm",
        message_type="shot",
        precision=0,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_total_spin",
        name="OGC Total Spin",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        icon="mdi:rotate-right",
        json_key="total_spin_rpm",
        message_type="shot",
        precision=0,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_spin_axis",
        name="OGC Spin Axis",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=0,
        icon="mdi:axis-arrow",
        json_key="spin_axis_degrees",
        message_type="shot",
        precision=0,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_club_path",
        name="OGC Club Path",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        icon="mdi:golf-course",
        json_key="club_path_degrees",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_club_face_to_target",
        name="OGC Club Face to Target",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        icon="mdi:golf",
        json_key="club_face_to_target_degrees",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_club_face_to_path",
        name="OGC Club Face to Path",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        icon="mdi:golf-cart",
        json_key="club_face_to_path_degrees",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_shot_name",
        name="OGC Shot Name",
        icon="mdi:golf-ball",
        json_key="shot_name",
        message_type="shot",
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_shot_rank",
        name="OGC Shot Rank",
        icon="mdi:medal",
        json_key="shot_rank",
        message_type="shot",
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_shot_color_rgb",
        name="OGC Shot Color RGB",
        icon="mdi:palette",
        json_key="shot_color_rgb",
        message_type="shot",
    ),
    # US Customary Units
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_ball_speed_mph",
        name="OGC Ball Speed (MPH)",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="us_customary_units.ball_speed_mph",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_club_speed_mph",
        name="OGC Club Speed (MPH)",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="us_customary_units.club_speed_mph",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_carry_distance_yards",
        name="OGC Carry Distance (Yards)",
        native_unit_of_measurement="yd", # Home Assistant does not have a UnitOfLength.YARDS constant, using string
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="us_customary_units.carry_distance_yards",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_total_distance_yards",
        name="OGC Total Distance (Yards)",
        native_unit_of_measurement="yd",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="us_customary_units.total_distance_yards",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_offline_distance_yards",
        name="OGC Offline Distance (Yards)",
        native_unit_of_measurement="yd",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="us_customary_units.offline_distance_yards",
        message_type="shot",
        precision=1,
    ),
    NovaByOpenLaunchSensorEntityDescription(
        key="ogc_peak_height_yards",
        name="OGC Peak Height (Yards)",
        native_unit_of_measurement="yd",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        json_key="us_customary_units.peak_height_yards",
        message_type="shot",
        precision=1,
    ),
)


# Status Sensors (from "type": "status" messages)
STATUS_SENSORS: tuple[NovaByOpenLaunchSensorEntityDescription, ...] = (
    NovaByOpenLaunchSensorEntityDescription(
        key="uptime",
        name="Uptime",
        native_unit_of_measurement=UnitOfTime.SECONDS,
        device_class=SensorDeviceClass.DURATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
        suggested_display_precision=0,
        icon="mdi:timer-outline",
        json_key="uptime_seconds",
        message_type="status",
        precision=0,
    ),
)

ALL_SENSORS = SHOT_SENSORS + STATUS_SENSORS + OPEN_GOLF_COACH_SENSORS
