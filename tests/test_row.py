from models.word import Word
from models.row import Row

row = Row(

    page=1,

    top=120,

    bottom=132

)

row.add_word(

    Word(

        page=1,

        text="Sl",

        x0=20,

        x1=30,

        top=120,

        bottom=132

    )

)

row.add_word(

    Word(

        page=1,

        text="No",

        x0=35,

        x1=50,

        top=120,

        bottom=132

    )

)

row.add_word(

    Word(

        page=1,

        text="Description",

        x0=70,

        x1=130,

        top=120,

        bottom=132

    )

)

row.sort()

print(row)

print()

print("Text :", row.text)

print("Left :", row.left)

print("Right :", row.right)

print("Width :", row.width)

print("Words :", row.word_count)

print()

print("Header :", row.is_header())

print("Item :", row.is_item())

print("Measurement :", row.is_measurement())

print("List :", row.is_list())

print("Total :", row.is_total())