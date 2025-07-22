from prac_09.silver_service_taxi import SilverServiceTaxi
sst = SilverServiceTaxi(2, name="Hummer", fuel=200)
sst.drive(18)
assert sst.get_fare() == 48.80
print(sst)