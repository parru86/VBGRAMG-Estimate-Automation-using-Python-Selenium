from models.estimate import Estimate
from models.item import Item
from models.measurement import Measurement

estimate = Estimate(

    work_name="Recharge Shaft",

    block="Arang",

    gram_panchayat="Kukra"

)

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

        quantity=2.13

    )

)

estimate.add_item(item)

print(estimate)

print()

print("Items :", estimate.item_count)

print("Measurements :", estimate.measurement_count)

print("Total Qty :", estimate.total_quantity)

print()

print(estimate.find_item("79.03.01b"))

print()

print(estimate.to_dict())