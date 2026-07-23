"""
=========================================================
VBGRAMG AUTO ESTIMATE
VALIDATOR
=========================================================
"""

from models.estimate import Estimate
from models.validation_result import ValidationResult


class Validator:
    """
    Validate Estimate before Portal Upload.
    """

    # --------------------------------------------------

    def validate(
        self,
        estimate: Estimate
    ) -> ValidationResult:

        result = ValidationResult()

        # ----------------------------------------------
        # Estimate Level
        # ----------------------------------------------

        if estimate.item_count == 0:

            result.add_error(
                "Estimate contains no items."
            )

            return result

        # ----------------------------------------------
        # Duplicate Item Codes
        # ----------------------------------------------

        seen_codes = set()

        for item in estimate.items:

            # ------------------------------------------

            if not item.item_code.strip():

                result.add_error(

                    f"Item {item.item_no}: Empty Item Code"

                )

            # ------------------------------------------

            if item.item_code in seen_codes:

                result.add_warning(

                    f"Duplicate Item Code : {item.item_code}"

                )

            else:

                seen_codes.add(item.item_code)

            # ------------------------------------------

            if not item.description.strip():

                result.add_warning(

                    f"Item {item.item_code}: Description Missing"

                )

            # ------------------------------------------

            if item.measurement_count == 0:

                result.add_warning(

                    f"Item {item.item_code}: No Measurements"

                )

            # ------------------------------------------
            # Measurement Validation
            # ------------------------------------------

            sl_set = set()

            for m in item.measurements:

                # Duplicate SL

                if m.sl in sl_set:

                    result.add_error(

                        f"{item.item_code}: Duplicate SL {m.sl}"

                    )

                else:

                    sl_set.add(m.sl)

                # Quantity

                if m.quantity == 0:

                    result.add_warning(

                        f"{item.item_code}: SL {m.sl} Quantity = 0"

                    )

                # Negative Quantity

                if m.quantity < 0:

                    result.add_warning(

                        f"{item.item_code}: SL {m.sl} Negative Quantity"

                    )

                # Empty Description

                if not m.description.strip():

                    result.add_warning(

                        f"{item.item_code}: SL {m.sl} Description Missing"

                    )

        return result