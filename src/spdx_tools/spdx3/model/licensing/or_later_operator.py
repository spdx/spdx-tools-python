# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from .any_license_info import AnyLicenseInfo
from .license import License

@dataclass_with_properties
class OrLaterOperator(AnyLicenseInfo):
    subject_license: License

    def __init__(self, subject_license: License):
        check_types_and_set_values(self, locals())
