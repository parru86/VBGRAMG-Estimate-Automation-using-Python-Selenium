from models.item import Item
from models.measurement import Measurement

item = Item(

    item_no=1,

    item_code="79.03.01b",

    description="Earth Work"

)

item.add_measurement(

    Measurement(

        sl=1,

        no=3.14,

        length=3.35,

        breadth=0.45,

        depth=0.45,

        cf=1,

        quantity=2.13

    )

)

item.add_measurement(

    Measurement(

        sl=2,

        no=3.14,

        length=1.05,

        breadth=1.05,

        depth=1.50,

        cf=1,

        quantity=5.193

    )

)

print(item)

print()

print("Measurements :", item.measurement_count)

print("Total Qty :", item.total_quantity)

print("Total Volume :", item.total_volume)

print()

print(item.get_measurement(2))

print()

print(item.to_dict())