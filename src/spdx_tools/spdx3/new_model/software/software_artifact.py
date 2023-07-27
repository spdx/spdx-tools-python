# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from abc import abstractmethod
from dataclasses import field

from beartype.typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties

from ..core import Artifact
from ..licensing import AnyLicenseInfo
from ..software import SoftwarePurpose


@dataclass_with_properties
class SoftwareArtifact(Artifact):
    """
    A software artifact is a distinct article or unit related to software such as a package, a file, or a snippet.
    """

    content_identifier: Optional[str] = None
    """
    The contentIdentifier provides a canonical, unique, immutable artifact identifier for each software artifact. SPDX
    3.0 describes software artifacts as Snippet, File, or Package Elements. The ContentIdentifier can be calculated for
    any software artifact and can be recorded for any of these SPDX 3.0 Elements using Omnibor, an attempt to
    standardize how software artifacts are identified independent of which programming language, version control
    system, build tool, package manager, or software distribution mechanism is in use.

    The contentIdentifier is defined as the [Git Object
    Identifier](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) (gitoid) of type `blob` of the software
    artifact. The use of a git-based version control system is not necessary to calculate a contentIdentifier for any
    software artifact.

    The gitoid is expressed in the ContentIdentifier property by using the IANA [gitoid URI
    scheme](https://www.iana.org/assignments/uri-schemes/prov/gitoid).

    ```
    Scheme syntax: gitoid":"<git object type>":"<hash algorithm>":"<hash value>
    ```

    The OmniBOR ID for the OmniBOR Document associated with a software artifact should not be recorded in this field.
    Rather, OmniBOR IDs should be recorded in the SPDX Element's ExternalIdentifier property. See
    [https://omnibor.io](https://omnibor.io) for more details.
    """
    primary_purpose: Optional[SoftwarePurpose] = None
    """
    primaryPurpose provides information about the primary purpose of the software artifact.
    """
    additional_purpose: List[SoftwarePurpose] = field(default_factory=list)
    """
    Additional purpose provides information about the additional purposes of the software artifact in addition to the
    primaryPurpose.
    """
    concluded_license: Optional[AnyLicenseInfo] = None
    """
    A concludedLicense is the license identified by the SPDX data creator, based on analyzing the license information
    in the software Package, File or Snippet and other information to arrive at a reasonably objective conclusion as to
    what license governs it.

    If a concludedLicense has a NONE value (NoneLicense), this indicates that the SPDX data creator has looked and did
    not find any license information for this software Package, File or Snippet.

    If a concludedLicense has a NOASSERTION value (NoAssertionLicense), this indicates that one of the following
    applies:
    * the SPDX data creator has attempted to but cannot reach a reasonable objective determination;
    * the SPDX data creator has made no attempt to determine this field; or
    * the SPDX data creator has intentionally provided no information (no meaning should be implied by doing so).

    A written explanation of a NOASSERTION value (NoAssertionLicense) MAY be provided in the licenseComment field.

    If the concludedLicense for a software Package, File or Snippet is not the same as its declaredLicense, a written
    explanation SHOULD be provided in the licenseComment field.

    If the declaredLicense for a software Package, File or Snippet is a choice of more than one license (e.g. a license
    expression combining two licenses through use of the `OR` operator), then the concludedLicense may either retain
    the license choice or identify which license was chosen.
    """
    declared_license: Optional[AnyLicenseInfo] = None
    """
    A declaredLicense is the license identified in text in the software package, file or snippet as the license
    declared by its authors.

    This field is not intended to capture license information obtained from an external source, such as a package's
    website. Such information can be included, as needed, in a concludedLicense field.

    A declaredLicense may be expressed differently in practice for different types of artifacts. For example:

    * for Packages:
      * would include license info describing the license of the Package as a whole, when it is found in the Package
        itself (e.g., LICENSE file, README file, metadata in the repository, etc.)
      * would not include any license information that is not in the Package itself (e.g., license information from the
        project’s website or from a third party repository or website)
    * for Files:
      * would include license info found in the File itself (e.g., license header or notice, comments,
        SPDX-License-Identifier expression)
      * would not include license info found in a different file (e.g., LICENSE file in the top directory of a
        repository)
    * for Snippets:
      * would include license info found in the Snippet itself (e.g., license notice, comments, SPDX-License-Identifier
        expression)
      * would not include license info found elsewhere in the File or in a different File (e.g., comment at top of File
        if it is not within the Snippet, LICENSE file in the top directory of a repository)

    If a declaredLicense has a NONE value (NoneLicense), this indicates that the corresponding Package, File or Snippet
    contains no license information whatsoever.

    If a declaredLicense has a NOASSERTION value (NoAssertionLicense), this indicates that one of the following
    applies:
    * the SPDX data creator has attempted to but cannot reach a reasonable objective determination;
    * the SPDX data creator has made no attempt to determine this field; or
    * the SPDX data creator has intentionally provided no information (no meaning should be implied by doing so).
    """
    copyright_text: Optional[str] = None
    """
    A copyrightText consists of the text(s) of the copyright notice(s) found for a software Package, File or Snippet,
    if any.

    If a copyrightText contains text, then it may contain any text related to one or more copyright notices (even if
    not complete) for that software Package, File or Snippet.

    If a copyrightText has a "NONE" value, this indicates that the software Package, File or Snippet contains no
    copyright notice whatsoever.

    If a copyrightText has a "NOASSERTION" value, this indicates that one of the following applies:
    * the SPDX data creator has attempted to but cannot reach a reasonable objective determination;
    * the SPDX data creator has made no attempt to determine this field; or
    * the SPDX data creator has intentionally provided no information (no meaning should be implied by doing so).
    """
    attribution_text: Optional[str] = None
    """
    An attributionText for a software Package, File or Snippet provides a consumer of SPDX data with acknowledgement
    content, to assist redistributors of the Package, File or Snippet with reproducing those acknowledgements.

    For example, this field may include a statement that is required by a particular license to be reproduced in
    end-user documentation, advertising materials, or another form.

    This field may describe where, or in which contexts, the acknowledgements need to be reproduced, but it is not
    required to do so. The SPDX data creator may also explain elsewhere (such as in a licenseComment field) how they
    intend for data in this field to be used.

    An attributionText is is not meant to include the software Package, File or Snippet’s actual complete license text
    (see concludedLicense to identify the corresponding license).
    """

    @abstractmethod
    def __init__(self):
        pass
