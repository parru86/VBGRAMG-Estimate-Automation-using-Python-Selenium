from models.item_block import ItemBlock

block = ItemBlock(

    item_no=1,

    item_code="79.03.01b",

    description="Earth Work"

)

print(block)

print()

print("Rows :", block.row_count)

print("Measurement Rows :", block.measurement_count)

print("Rate Rows :", block.rate_count)