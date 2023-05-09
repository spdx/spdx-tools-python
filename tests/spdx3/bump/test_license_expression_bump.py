# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
import pytest
from license_expression import LicenseExpression, get_spdx_licensing

from spdx_tools.spdx3.bump_from_spdx2.license_expression import (
    bump_license_expression,
    bump_license_expression_or_none_or_no_assertion,
)
from spdx_tools.spdx3.model.licensing import (
    ConjunctiveLicenseSet,
    CustomLicense,
    CustomLicenseAddition,
    DisjunctiveLicenseSet,
    ListedLicense,
    ListedLicenseException,
    NoAssertionLicense,
    NoneLicense,
    WithAdditionOperator,
)
from spdx_tools.spdx.model import SpdxNoAssertion, SpdxNone


@pytest.mark.parametrize(
    "element, expected_class",
    [
        (SpdxNoAssertion(), NoAssertionLicense),
        (SpdxNone(), NoneLicense),
        (get_spdx_licensing().parse("MIT"), ListedLicense),
    ],
)
def test_license_expression_or_none_or_no_assertion(element, expected_class):
    license_info = bump_license_expression_or_none_or_no_assertion(element)

    assert isinstance(license_info, expected_class)


@pytest.mark.parametrize(
    "license_expression, expected_element",
    [
        (get_spdx_licensing().parse("MIT"), ListedLicense("MIT", "MIT", "")),
        (get_spdx_licensing().parse("LGPL-2.0"), ListedLicense("LGPL-2.0-only", "LGPL-2.0-only", "")),
        (get_spdx_licensing().parse("LicenseRef-1"), CustomLicense("LicenseRef-1", "", "")),
        (
            get_spdx_licensing().parse("MIT AND LGPL-2.0"),
            ConjunctiveLicenseSet(
                [ListedLicense("MIT", "MIT", ""), ListedLicense("LGPL-2.0-only", "LGPL-2.0-only", "")]
            ),
        ),
        (
            get_spdx_licensing().parse("LicenseRef-1 OR LGPL-2.0"),
            DisjunctiveLicenseSet(
                [CustomLicense("LicenseRef-1", "", ""), ListedLicense("LGPL-2.0-only", "LGPL-2.0-only", "")]
            ),
        ),
        (
            get_spdx_licensing().parse("LGPL-2.0 WITH 389-exception"),
            WithAdditionOperator(
                ListedLicense("LGPL-2.0-only", "LGPL-2.0-only", ""), ListedLicenseException("389-exception", "", "")
            ),
        ),
        (
            get_spdx_licensing().parse("LicenseRef-1 WITH custom-exception"),
            WithAdditionOperator(
                CustomLicense("LicenseRef-1", "", ""), CustomLicenseAddition("custom-exception", "", "")
            ),
        ),
        (
            get_spdx_licensing().parse("MIT AND LicenseRef-1 WITH custom-exception"),
            ConjunctiveLicenseSet(
                [
                    ListedLicense("MIT", "MIT", ""),
                    WithAdditionOperator(
                        CustomLicense("LicenseRef-1", "", ""), CustomLicenseAddition("custom-exception", "", "")
                    ),
                ]
            ),
        ),
    ],
)
def test_license_expression_bump(license_expression: LicenseExpression, expected_element):
    license_info = bump_license_expression(license_expression)

    assert license_info == expected_element
