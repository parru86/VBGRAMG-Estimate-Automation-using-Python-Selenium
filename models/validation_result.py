"""
=========================================================
VBGRAMG AUTO ESTIMATE
VALIDATION RESULT MODEL
=========================================================
"""

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class ValidationResult:
    """
    Validation Report
    """

    passed: bool = True

    errors: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    # --------------------------------------------------

    def add_error(self, message: str):

        self.errors.append(message)

        self.passed = False

    # --------------------------------------------------

    def add_warning(self, message: str):

        self.warnings.append(message)

    # --------------------------------------------------

    @property
    def error_count(self):

        return len(self.errors)

    # --------------------------------------------------

    @property
    def warning_count(self):

        return len(self.warnings)

    # --------------------------------------------------

    def clear(self):

        self.errors.clear()

        self.warnings.clear()

        self.passed = True

    # --------------------------------------------------

    def __repr__(self):

        return (

            f"ValidationResult("

            f"Passed={self.passed}, "

            f"Errors={self.error_count}, "

            f"Warnings={self.warning_count}"

            f")"

        )