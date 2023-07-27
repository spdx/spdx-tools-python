# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from enum import Enum, auto

from beartype.typing import Optional


class SafetyRiskAssessmentType(Enum):
    """
    Lists the different safety risk type values that can be used to describe the safety risk of AI software according
    to [Article 20 of Regulation
    765/2008/EC](https://ec.europa.eu/docsroom/documents/17107/attachments/1/translations/en/renditions/pdf).
    """

    SERIOUS = auto()
    """
    The highest level of risk posed by an AI software.
    """
    HIGH = auto()
    """
    The second-highest level of risk posed by an AI software.
    """
    MEDIUM = auto()
    """
    The third-highest level of risk posed by an AI software.
    """
    LOW = auto()
    """
    Low/no risk is posed by the AI software.
    """

    def __str__(self) -> str:
        if self == SafetyRiskAssessmentType.SERIOUS:
            return "serious"
        if self == SafetyRiskAssessmentType.HIGH:
            return "high"
        if self == SafetyRiskAssessmentType.MEDIUM:
            return "medium"
        if self == SafetyRiskAssessmentType.LOW:
            return "low"
        return "unknown"

    @staticmethod
    def from_str(value: str) -> Optional["SafetyRiskAssessmentType"]:
        if value == "serious":
            return SafetyRiskAssessmentType.SERIOUS
        if value == "high":
            return SafetyRiskAssessmentType.HIGH
        if value == "medium":
            return SafetyRiskAssessmentType.MEDIUM
        if value == "low":
            return SafetyRiskAssessmentType.LOW
        return None
