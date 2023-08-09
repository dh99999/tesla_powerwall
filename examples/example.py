import os
from tesla_powerwall import Powerwall, Meter


def getenv(var):
    val = os.getenv(var)
    if val is None:
        raise ValueError(f"{var} must be set")
    return val


def print_meter_row(meter_data: Meter):
    print(
        "{:>8} {:>8} {:>17} {:>17} {!r:>8} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12} {!r:>12}".format(
       
            meter_data.meter.value,
            meter_data.get_power(),
            meter_data.get_energy_exported(),
            meter_data.get_energy_imported(),
            meter_data.is_active(),
            meter_data.is_drawing_from(),
            meter_data.is_sending_to(),
            meter_data.i_a_current,
            meter_data.i_b_current,
            meter_data.i_c_current,
            meter_data.real_power_a,
            meter_data.real_power_b,
            meter_data.real_power_c,
            meter_data.reactive_power_a,
            meter_data.reactive_power_b,
            meter_data.reactive_power_c,
            meter_data.v_l1n,
            meter_data.v_l2n,
            meter_data.v_l3n
        )
    )


ip = getenv("POWERWALL_IP")
password = getenv("POWERWALL_PASSWORD")

power_wall = Powerwall(ip)
power_wall.login(password)
site_name = power_wall.get_site_info().site_name
meters_agg = power_wall.get_meters()
meter_site = power_wall.get_meters_site()

print(f"{site_name}:\n")

row_format = "{:>18}: {}"

values = [
    ("Charge (%)", round(power_wall.get_charge())),
    ("Capacity", power_wall.get_capacity()),
    ("Nominal Energy", power_wall.get_energy()),
    ("Grid Status", power_wall.get_grid_status().value),
    ("Backup Reserve (%)", round(power_wall.get_backup_reserve_percentage())),
    ("Device Type", power_wall.get_device_type().value),
    ("Software Version", power_wall.get_version())
]


for val in values:
    print(row_format.format(*val))

print("\n")

print(
    "{:>8} {:>8} {:>17} {:>17} {:>8} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}".format(
        "Meter",
        "Power",
        "Energy exported",
        "Energy imported",
        "Active",
        "Drawing from",
        "Sending to",
        "Current-A",
        "Current-B",
        "Current-C",
        "RealPower-A",
        "RealPower-B",
        "RealPower-C",
        "ReactivePower-A",
        "ReactivePower-B",
        "ReactivePower-C",
        "Voltage-1",
        "Voltage-2",
        "Voltage-3",
    )
)
#for meter in meters_agg.meters:
#    print_meter_row(meters_agg.get_meter(meter))

print_meter_row(meter_site)
