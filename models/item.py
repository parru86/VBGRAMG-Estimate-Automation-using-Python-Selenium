"""
=========================================================
VBGRAMG AUTO ESTIMATE
ITEM MODEL
=========================================================
"""

from dataclasses import dataclass, field
from typing import List, Optional

from models.measurement import Measurement


@dataclass(slots=True)
class Item:
    """
    Represents one Estimate Item.
    """

    item_no: int

    item_code: str

    description: str

    measurements: List[Measurement] = field(default_factory=list)

    # --------------------------------------------------

    def add_measurement(self, measurement: Measurement):

        """
        Add one measurement row.
        """

        self.measurements.append(measurement)

    # --------------------------------------------------

    @property
    def measurement_count(self) -> int:

        return len(self.measurements)

    # --------------------------------------------------

    @property
    def total_quantity(self) -> float:

        return round(

            sum(

                m.quantity

                for m in self.measurements

            ),

            3

        )

    # --------------------------------------------------

    @property
    def total_volume(self) -> float:

        return round(

            sum(

                m.volume

                for m in self.measurements

            ),

            4

        )

    # --------------------------------------------------

    def get_measurement(

        self,

        sl: int

    ) -> Optional[Measurement]:

        """
        Find Measurement by Sl No.
        """

        for m in self.measurements:

            if m.sl == sl:

                return m

        return None

    # --------------------------------------------------

    def clear(self):

        """
        Remove all measurements.
        """

        self.measurements.clear()

    # --------------------------------------------------

    def to_dict(self):

        return {

            "item_no": self.item_no,

            "item_code": self.item_code,

            "description": self.description,

            "measurement_count": self.measurement_count,

            "total_quantity": self.total_quantity,

            "measurements": [

                m.to_dict()

                for m in self.measurements

            ]

        }

    # --------------------------------------------------

    def __repr__(self):

        return (

            f"Item("

            f"{self.item_code}, "

            f"Measurements={self.measurement_count}, "

            f"Qty={self.total_quantity}"

            f")"

        )